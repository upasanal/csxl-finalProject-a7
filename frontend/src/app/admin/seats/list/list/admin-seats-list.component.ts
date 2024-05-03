import { Component, inject } from '@angular/core';
import { SeatAdminService } from '../../admin-seats-service';
import { Seat, SeatAvailability } from 'src/app/coworking/coworking.models';
import { permissionGuard } from 'src/app/permission.guard';
import { NavigationService } from 'src/app/navigation/navigation.service';
import {
  ActivatedRoute,
  ActivatedRouteSnapshot,
  CanActivateFn,
  Router,
  RouterStateSnapshot
} from '@angular/router';
import { FormBuilder } from '@angular/forms';
import { Profile } from 'src/app/models.module';
import { PermissionService } from 'src/app/permission.service';
import { profileResolver } from 'src/app/profile/profile.resolver';
import { roomResolver } from 'src/app/academics/academics.resolver';

const canActivateEditor: CanActivateFn = (
  route: ActivatedRouteSnapshot,
  state: RouterStateSnapshot
) => {
  /** Determine if page is viewable by user based on permissions */

  let id: string = 'SN156';
  return inject(PermissionService).check('room.update', `room/${id}`);
};

@Component({
  selector: 'app-admin-seats-list',
  templateUrl: './admin-seats-list.component.html',
  styleUrls: ['./admin-seats-list.component.css']
})
export class AdminSeatsListComponent {
  public selectedSeat: SeatAvailability | undefined;

  public static Route = {
    path: 'seats',
    component: AdminSeatsListComponent,
    title: 'Seat Administration',
    canActivate: [canActivateEditor],
    resolve: {
      profile: profileResolver
    }
  };

  constructor(
    private seatService: SeatAdminService,
    private navService: NavigationService,
    private router: Router,
    route: ActivatedRoute
  ) {
    let data = route.snapshot.data as { seats: Seat[] };
  }

  onSeatsSelected(seatSelection: SeatAvailability[]): void {
    this.selectedSeat = seatSelection.length > 0 ? seatSelection[0] : undefined;
  }
}
