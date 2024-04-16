import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import {
  CircleTable,
  RectangleTable,
  Seat,
  SeatAvailability
} from 'src/app/coworking/coworking.models';
import { CsxlSeatMapService } from '../../seating-reservation/csxl-seat-map/csxl-seat-map.service';
import { CoworkingService } from '../../coworking.service';
import { ReservationService } from '../../reservation/reservation.service';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'seat-map',
  templateUrl: './seat-map.widget.html',
  styleUrls: ['./seat-map.widget.css']
})
export class SeatMapWidgetComponent implements OnInit {
  seats: Seat[] = [];
  seatsClicked: Seat[] = [];
  seatsReserved: SeatAvailability[] = []; // seats only become reserved once user presses reserved button
  @Output() reservationDrafted = new EventEmitter<SeatAvailability[]>();
  boundaries: String = '';
  rectangleTables: RectangleTable[] = [];
  circleTables: CircleTable[] = [];

  roomId = 'SN156';

  constructor(
    public mapService: CsxlSeatMapService,
    private coworkService: CoworkingService,
    private reserveService: ReservationService,
    private snackBar: MatSnackBar
  ) {}
  // seats only become reserved once user presses reserved button

  ngOnInit(): void {
    this.getSeats();
    this.getBoundaries(this.roomId);
    this.getCircleTables(this.roomId);
    this.getRectangleTables(this.roomId);
    this.getBoundaries(this.roomId);
    this.getCircleTables(this.roomId);
    this.getRectangleTables(this.roomId);
  }

  getSeats(): void {
    this.mapService.getSeats(this.roomId).subscribe((seats) => {
      this.seats = seats;
    });
  }

  seatClicked(seat: Seat) {
    if (seat.reservable) {
      if (this.mapService.isSeatClicked(seat)) {
        this.mapService.removeClickedSeat(seat);
        this.seatsClicked = this.seatsClicked.filter((s) => s !== seat);
      } else {
        if (this.seatsClicked.length < 4) {
          this.mapService.addClickedSeat(seat);
          this.seatsClicked.push(seat);
        } else {
          this.snackBar.open('You can only select up to 4 seats.', 'Close', {
            duration: 3000 // Duration in milliseconds
          });
        }
      }
    }
  }

  getBoundaries(id: string) {
    this.mapService.getBoundaries(id).subscribe((boundaries) => {
      this.boundaries = boundaries;
    });
  }

  getCircleTables(id: string) {
    this.mapService.getCircleTables(id).subscribe((circleTables) => {
      this.circleTables = circleTables;
    });
    console.log(this.circleTables);
  }

  getRectangleTables(id: string) {
    this.mapService.getRectangleTables(id).subscribe((rectangleTables) => {
      this.rectangleTables = rectangleTables;
    });
  }

  isReservable(seat: Seat) {
    return seat.reservable;
  }

  isButtonActive(): boolean {
    return this.mapService.getClickedSeats().length > 0;
  }

  seatPressed(seat: Seat) {
    return this.mapService.isSeatClicked(seat);
  }

  reserveSeats() {
    const clickedSeats = this.mapService.getClickedSeats();
    const reservations: SeatAvailability[] = clickedSeats.map((seat) => ({
      id: seat.id,
      availability: seat.availability,
      title: seat.title,
      shorthand: seat.shorthand,
      reservable: seat.reservable,
      has_monitor: seat.has_monitor,
      sit_stand: seat.sit_stand,
      x: seat.x,
      y: seat.y
    }));
    this.reservationDrafted.emit(reservations);
    this.mapService.clearReservations();
  }

  clearReserves() {
    this.mapService.clearReservations();
    this.seatsClicked = [];
  }

  getSeatColor(seat: Seat): string {
    if (!seat.reservable) {
      return 'grey';
    } else if (this.mapService.isSeatClicked(seat)) {
      return 'red';
    } else if (seat.sit_stand) {
      return 'orange';
    } else if (seat.has_monitor) {
      return 'green';
    } else {
      return '#3479be'; // Assuming you want to use the primary color defined in your theme
    }
  }
}
