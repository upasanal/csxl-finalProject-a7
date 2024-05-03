import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { catchError, map, Observable, of, tap } from 'rxjs';
import { CircleTable, RectangleTable, Seat } from '../../coworking.models';
import { ReservationService } from '../../reservation/reservation.service';
import { SeatAvailability } from '../../coworking.models';
import { Router } from '@angular/router';
import { PublicProfile } from 'src/app/profile/profile.service';
import { SeatMapUserService } from './csxl-seat-map-users.service';

const ONE_HOUR = 60 * 60 * 1000;

@Injectable({
  providedIn: 'root'
})
export class CsxlSeatMapService {
  public clickedSeats: Seat[] = [];
  private seats: Seat[] = [];
  public seatAvailability: SeatAvailability[] = [];
  public availableSeatsFromBackend: Number[] = [];

  constructor(
    protected http: HttpClient,
    private router: Router,
    private reserveService: ReservationService,
    private seatMapUserService: SeatMapUserService
  ) {}

  navigateToSeatMap(users?: PublicProfile[]) {
    this.seatMapUserService.setUsers(users || []);
    this.router.navigateByUrl('/coworking/seat-map');
  }

  getAvailableSeats(seat_id: Number) {
    this.availableSeatsFromBackend.push(seat_id);
  }

  getBoundaries(id: string): Observable<String> {
    return this.http.get<String>(`/api/room/${id}/boundaries`);
  }

  getCircleTables(id: string): Observable<[CircleTable]> {
    return this.http.get<[CircleTable]>(`/api/room/${id}/circle_tables`);
  }

  getRectangleTables(id: string): Observable<[RectangleTable]> {
    return this.http.get<[RectangleTable]>(`/api/room/${id}/rectangle_tables`);
  }

  getSeats(id: string): Observable<Seat[]> {
    let url = `/api/room/${id}/seats`;
    return this.http.get<Seat[]>(url).pipe(
      map((seatDetailsArray: Seat[]) => {
        return seatDetailsArray.map((seatDetails) => {
          let seat: Seat = {
            title: seatDetails.title,
            shorthand: seatDetails.shorthand,
            reservable: seatDetails.reservable,
            has_monitor: seatDetails.has_monitor,
            sit_stand: seatDetails.sit_stand,
            x: seatDetails.x,
            y: seatDetails.y,
            id: seatDetails.id
          };
          return seat;
        });
      }),
      tap((seats: Seat[]) => {
        this.seats = seats;
      })
    );
  }

  getStoredSeats(): Seat[] {
    return this.seats;
  }

  getClickedSeats() {
    let seaty: SeatAvailability[] = [];
    seaty = this.convertSeatsToSeatAvailability(this.clickedSeats);
    return seaty;
  }

  isSeatClicked(seat: Seat): boolean {
    return this.clickedSeats.includes(seat);
  }

  addClickedSeat(seat: Seat) {
    return this.clickedSeats.push(seat);
  }

  removeClickedSeat(seat: Seat) {
    this.clickedSeats = this.clickedSeats.filter(
      (clickedSeat) => clickedSeat !== seat
    );
  }

  getSeatById(seatid: number) {
    for (let i = 0; i < this.getStoredSeats().length; i++) {
      if ((this.getStoredSeats()[i].id = seatid)) {
        return this.getStoredSeats()[i];
      }
    }
    return null;
  }

  reserveSeats(seats: Seat[]) {
    for (let i = 0; i < seats.length; i++) {
      seats[i].reservable = false;
    }
  }

  convertSeatsToSeatAvailability(seats: Seat[]) {
    let seatAvails: SeatAvailability[] = [];
    let currentTime = new Date();

    for (let i = 0; i < seats.length; i++) {
      let seat = seats[i];
      let seatAvail: SeatAvailability = {
        ...seat,
        availability: [
          {
            start: currentTime,
            end: new Date(currentTime.getTime() + 2 * 60 * 60 * 1000)
          }
        ]
      };
      seatAvails.push(seatAvail);
    }
    return seatAvails;
  }

  clearReservations() {
    this.clickedSeats = [];
    this.seats = [];
  }
}
