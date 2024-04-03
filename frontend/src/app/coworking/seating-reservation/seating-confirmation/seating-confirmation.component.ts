import { Component } from '@angular/core';
import {
  ActivatedRoute,
  ActivatedRouteSnapshot,
  ResolveFn,
  Route,
  Router
} from '@angular/router';
import { isAuthenticated } from 'src/app/gate/gate.guard';
import { profileResolver } from 'src/app/profile/profile.resolver';

@Component({
  selector: 'app-seating-confirmation',
  templateUrl: './seating-confirmation.component.html',
  styleUrls: ['./seating-confirmation.component.css']
})
export class SeatingConfirmationComponent {
  public static Route: Route = {
    path: 'confirm-seat',
    title: 'CSXL Seat Confirmation',
    component: SeatingConfirmationComponent,
    canActivate: [isAuthenticated],
    resolve: { profile: profileResolver }
  };
}
