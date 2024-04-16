import { Component } from '@angular/core';
import { Route, Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar'; // Import MatSnackBar
import { isAuthenticated } from 'src/app/gate/gate.guard';
import { profileResolver } from 'src/app/profile/profile.resolver';
import { CoworkingService } from '../../coworking.service';
import { Seat, SeatAvailability } from '../../coworking.models';
import { Profile } from 'src/app/models.module';
import { SeatMapUserService } from './csxl-seat-map-users.service';
import { AmbassadorXlService } from '../../ambassador-home/ambassador-xl/ambassador-xl.service';
import { Subscription, tap, timer } from 'rxjs';

const FIVE_SECONDS = 5 * 1000;

@Component({
  selector: 'app-csxl-seat-map',
  templateUrl: './csxl-seat-map.component.html',
  styleUrls: ['./csxl-seat-map.component.css']
})
export class CsxlSeatMapComponent {
  profile: Profile | undefined;
  constructor(
    private coworkingService: CoworkingService,
    private router: Router,
    private snackBar: MatSnackBar, // Inject MatSnackBar
    private seatMapUserService: SeatMapUserService,
    private ambassadorService: AmbassadorXlService
  ) {
    this.profile = this.coworkingService.getProfile();
  }

  public static Route: Route = {
    path: 'seat-map',
    title: 'CSXL Seat Map',
    component: CsxlSeatMapComponent,
    canActivate: [isAuthenticated],
    resolve: { profile: profileResolver }
  };

  private refreshSubscription!: Subscription;

  onSeatsSelected(seatSelection: SeatAvailability[]): void {
    if (!this.profile) {
      throw new Error('Only allowed for logged in users.');
    }
    const selectedUsers = this.seatMapUserService.getUsers();
    if (selectedUsers.length === 0) {
      this.coworkingService.draftReservation(seatSelection).subscribe({
        error: (error) =>
          this.snackBar.open(
            'Error. There may be a conflicting upcoming reservation. Please check upcoming reservations.',
            '',
            { duration: 8000 }
          ),
        next: (reservation) => {
          this.router.navigateByUrl(`/coworking/reservation/${reservation.id}`);
        }
      });
    } else {
      this.ambassadorService
        .makeDropinReservation(seatSelection, selectedUsers)
        .subscribe({
          next: (reservation) => {
            this.seatMapUserService.clearUsers();
            this.beginReservationRefresh();
            alert(
              `Walk-in reservation made for ${
                reservation.users[0].first_name
              } ${
                reservation.users[0].last_name
              }!\nReservation ends at ${reservation.end.toLocaleTimeString()}`
            );
          },
          error: (e) => {
            this.seatMapUserService.clearUsers();
            alert(e.message + '\n\n' + e.error.message);
          }
        });
    }
  }

  beginReservationRefresh(): void {
    if (this.refreshSubscription) {
      this.refreshSubscription.unsubscribe();
    }
    this.refreshSubscription = timer(0, FIVE_SECONDS)
      .pipe(tap((_) => this.ambassadorService.fetchReservations()))
      .subscribe();
  }
}
