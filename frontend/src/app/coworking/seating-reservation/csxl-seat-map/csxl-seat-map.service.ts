import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { catchError, map, Observable, of } from 'rxjs';
import { Seat } from '../../coworking.models';
import { ReservationService } from '../../reservation/reservation.service';
import { SeatAvailability } from '../../coworking.models';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class CsxlSeatMapService {
  private allSeats: Seat[] = [];
  private clickedSeats: Seat[] = [];

  constructor(
    private router: Router,
    private reserveService: ReservationService
  ) {
    this.allSeats = [
      {
        id: 1,
        title: 'Seat 1',
        shorthand: 'S1',
        reservable: true,
        has_monitor: true,
        sit_stand: true,
        x: 9,
        y: 10
      },
      {
        id: 2,
        title: 'Seat 2',
        shorthand: 'S2',
        reservable: true,
        has_monitor: true,
        sit_stand: true,
        x: 9,
        y: 30
      },
      {
        id: 3,
        title: 'Seat 3',
        shorthand: 'S3',
        reservable: true,
        has_monitor: true,
        sit_stand: false,
        x: 40,
        y: 10
      },
      {
        id: 4,
        title: 'Seat 4',
        shorthand: 'S4',
        reservable: true,
        has_monitor: true,
        sit_stand: false,
        x: 40,
        y: 30
      },
      {
        id: 5,
        title: 'Seat 5',
        shorthand: 'S5',
        reservable: true,
        has_monitor: true,
        sit_stand: false,
        x: 40,
        y: 50
      },
      {
        id: 6,
        title: 'Seat 6',
        shorthand: 'S6',
        reservable: true,
        has_monitor: true,
        sit_stand: false,
        x: 56,
        y: 10
      },
      {
        id: 7,
        title: 'Seat 7',
        shorthand: 'S7',
        reservable: true,
        has_monitor: true,
        sit_stand: false,
        x: 56,
        y: 30
      },
      {
        id: 8,
        title: 'Seat 8',
        shorthand: 'S8',
        reservable: true,
        has_monitor: true,
        sit_stand: false,
        x: 56,
        y: 50
      },
      {
        id: 9,
        title: 'Seat 9',
        shorthand: 'S9',
        reservable: true,
        has_monitor: true,
        sit_stand: false,
        x: 85,
        y: 10
      },
      {
        id: 10,
        title: 'Seat 10',
        shorthand: 'S10',
        reservable: true,
        has_monitor: true,
        sit_stand: false,
        x: 85,
        y: 30
      },
      {
        id: 11,
        title: 'Seat 11',
        shorthand: 'S11',
        reservable: true,
        has_monitor: true,
        sit_stand: false,
        x: 85,
        y: 50
      },
      {
        id: 12,
        title: 'Seat 12',
        shorthand: 'S12',
        reservable: true,
        has_monitor: true,
        sit_stand: false,
        x: 101,
        y: 10
      },
      {
        id: 13,
        title: 'Seat 13',
        shorthand: 'S13',
        reservable: true,
        has_monitor: true,
        sit_stand: false,
        x: 101,
        y: 30
      },
      {
        id: 14,
        title: 'Seat 14',
        shorthand: 'S14',
        reservable: true,
        has_monitor: true,
        sit_stand: false,
        x: 101,
        y: 50
      },
      {
        id: 15,
        title: 'Seat 15',
        shorthand: 'S15',
        reservable: true,
        has_monitor: true,
        sit_stand: true,
        x: 142,
        y: 10
      },
      {
        id: 16,
        title: 'Seat 16',
        shorthand: 'S16',
        reservable: true,
        has_monitor: true,
        sit_stand: true,
        x: 142,
        y: 30
      },
      {
        id: 17,
        title: 'Seat 17',
        shorthand: 'S17',
        reservable: true,
        has_monitor: true,
        sit_stand: true,
        x: 142,
        y: 50
      },
      {
        id: 18,
        title: 'Seat 18',
        shorthand: 'S18',
        reservable: true,
        has_monitor: true,
        sit_stand: true,
        x: 142,
        y: 70
      },
      {
        id: 19,
        title: 'Seat 19',
        shorthand: 'S19',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 15,
        y: 80
      },
      {
        id: 20,
        title: 'Seat 20',
        shorthand: 'S20',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 25,
        y: 70
      },
      {
        id: 21,
        title: 'Seat 21',
        shorthand: 'S21',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 35,
        y: 80
      },
      {
        id: 22,
        title: 'Seat 22',
        shorthand: 'S22',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 25,
        y: 90
      },
      {
        id: 23,
        title: 'Seat 23',
        shorthand: 'S23',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 50,
        y: 105
      },
      {
        id: 24,
        title: 'Seat 24',
        shorthand: 'S24',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 60,
        y: 95
      },
      {
        id: 25,
        title: 'Seat 25',
        shorthand: 'S25',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 70,
        y: 105
      },
      {
        id: 26,
        title: 'Seat 26',
        shorthand: 'S26',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 60,
        y: 115
      },
      {
        id: 27,
        title: 'Seat 27',
        shorthand: 'S27',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 15,
        y: 130
      },
      {
        id: 28,
        title: 'Seat 28',
        shorthand: 'S28',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 25,
        y: 120
      },
      {
        id: 29,
        title: 'Seat 29',
        shorthand: 'S29',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 35,
        y: 130
      },
      {
        id: 30,
        title: 'Seat 30',
        shorthand: 'S30',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 25,
        y: 140
      },
      {
        id: 31,
        title: 'Seat 31',
        shorthand: 'S31',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 112.5,
        y: 90
      },
      {
        id: 32,
        title: 'Seat 32',
        shorthand: 'S32',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 100,
        y: 98
      },
      {
        id: 33,
        title: 'Seat 33',
        shorthand: 'S33',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 100,
        y: 114
      },
      {
        id: 34,
        title: 'Seat 34',
        shorthand: 'S34',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 100,
        y: 129
      },
      {
        id: 35,
        title: 'Seat 35',
        shorthand: 'S35',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 100,
        y: 144
      },
      {
        id: 36,
        title: 'Seat 36',
        shorthand: 'S36',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 125,
        y: 98
      },
      {
        id: 37,
        title: 'Seat 37',
        shorthand: 'S37',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 125,
        y: 114
      },
      {
        id: 38,
        title: 'Seat 38',
        shorthand: 'S38',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 125,
        y: 129
      },
      {
        id: 39,
        title: 'Seat 39',
        shorthand: 'S39',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 125,
        y: 144
      },
      {
        id: 40,
        title: 'Seat 40',
        shorthand: 'S40',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 112.5,
        y: 150
      },
      {
        id: 41,
        title: 'Seat 41',
        shorthand: 'S41',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 50,
        y: 162
      },
      {
        id: 42,
        title: 'Seat 42',
        shorthand: 'S42',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 30,
        y: 162
      },
      {
        id: 43,
        title: 'Seat 43',
        shorthand: 'S43',
        reservable: true,
        has_monitor: false,
        sit_stand: false,
        x: 10,
        y: 162
      }
    ];
  }

  navigateToSeatMap() {
    this.router.navigateByUrl('/coworking/seat-map');
  }

  getSeats() {
    console.log('Service method for get seats.');
    console.log(this.allSeats);
    return this.allSeats;
  }

  getClickedSeats() {
    console.log('Service method for clicked seats');
    console.log(this.clickedSeats);
    return this.clickedSeats;
  }

  isSeatClicked(seat: Seat): boolean {
    console.log('Is Seat clicked method in Service');
    console.log(this.clickedSeats.includes(seat));
    return this.clickedSeats.includes(seat);
  }

  addClickedSeat(seat: Seat) {
    console.log(
      `This is about to be pushed to clicked seats through addClickedSeat in service: ${seat}`
    );
    return this.clickedSeats.push(seat);
  }

  removeClickedSeat(seat: Seat) {
    this.clickedSeats = this.clickedSeats.filter(
      (clickedSeat) => clickedSeat !== seat
    );
    console.log('removeClickedSeat has executed!');
  }

  getSeatById(seatid: number) {
    console.log(
      `this.allSeats after clearReservations() in service: ${this.allSeats.length}`
    );
    for (let i = 0; i < this.allSeats.length; i++) {
      if ((this.allSeats[i].id = seatid)) {
        return this.allSeats[i];
      }
    }
    return null;
  }

  reserveSeats(seats: Seat[]) {
    for (let i = 0; i < seats.length; i++) {
      seats[i].reservable = false;
    }
    console.log('Reserve seats has executed in service');
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
    console.log('seatAvails:', seatAvails);
    return seatAvails;
  }

  clearReservations() {
    for (let i = 0; i < this.allSeats.length; i++) {
      this.reserveService
        .get(this.allSeats[i].id)
        .subscribe((val) => this.reserveService.cancel(val));
    }
    console.log(
      `this.allSeats after clearReservations() in service: ${this.allSeats.length}`
    );
  }
}
