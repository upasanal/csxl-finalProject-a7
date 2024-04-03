import { Component, inject } from '@angular/core';
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
  selector: 'app-csxl-seat-map',
  templateUrl: './csxl-seat-map.component.html',
  styleUrls: ['./csxl-seat-map.component.css']
})
export class CsxlSeatMapComponent {
  constructor() {}

  public static Route: Route = {
    path: 'seat-map',
    title: 'CSXL Seat Map',
    component: CsxlSeatMapComponent,
    canActivate: [isAuthenticated],
    resolve: { profile: profileResolver }
  };
}
