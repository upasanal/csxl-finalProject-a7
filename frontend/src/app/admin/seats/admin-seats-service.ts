import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Role, RoleDetails } from 'src/app/role';
import { Permission, Profile } from 'src/app/profile/profile.service';
import { Observable, firstValueFrom } from 'rxjs';
import {
  Room,
  Seat,
  SeatAvailability,
  SeatDetails
} from 'src/app/coworking/coworking.models';
import { CsxlSeatMapService } from 'src/app/coworking/seating-reservation/csxl-seat-map/csxl-seat-map.service';
import { AcademicsService } from 'src/app/academics/academics.service';
import { AdminSeatMapWidgetComponent } from '../widgets/seat-map/seat-map.widget';
import { of } from 'rxjs';
import { map, catchError } from 'rxjs/operators';

@Injectable({ providedIn: 'root' })
export class SeatAdminService {
  constructor(
    protected http: HttpClient,
    private roomService: AcademicsService
  ) {}

  updateSeat(
    seatAvailability: SeatAvailability,
    room_id: string,
    x: number,
    y: number
  ): Observable<SeatDetails> {
    // Mapping the SeatAvailability to SeatDetails if necessary
    const seat_id: number = seatAvailability.id;
    const params = new HttpParams()
      .set('x', x.toString())
      .set('y', y.toString());
    // Prepare the payload as expected by the backend---
    //Found through research about HTTP Params and CHAT GPT,
    //as well as within existing code base in reservation table service!

    const payload = {
      room_id: 'SN156',
      seat_id: seatAvailability.id
      // make sure 'room' contains all the necessary fields expected by the backend
    };

    return this.http.put<SeatDetails>(
      `/api/room/${room_id}/seats/${seat_id}`,
      payload,
      { params }
    );
  }
}
