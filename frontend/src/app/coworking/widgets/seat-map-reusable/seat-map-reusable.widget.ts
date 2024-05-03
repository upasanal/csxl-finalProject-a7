import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import {
  CircleTable,
  RectangleTable,
  Reservation,
  Seat,
  SeatAvailability
} from 'src/app/coworking/coworking.models';
import { CsxlSeatMapService } from '../../seating-reservation/csxl-seat-map/csxl-seat-map.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Observable } from 'rxjs';

@Component({
  selector: 'seat-map-reusable',
  templateUrl: './seat-map-reusable.widget.html',
  styleUrls: ['./seat-map-reusable.widget.css']
})
export class SeatMapWidgetReusableComponent implements OnInit {
  seats: Seat[] = [];
  seatsClicked: Seat[] = [];
  seatsReserved: SeatAvailability[] = []; // seats only become reserved once user presses reserved button
  @Output() reservationDrafted = new EventEmitter<SeatAvailability[]>();
  boundaries: String = '';
  rectangleTables: RectangleTable[] = [];
  circleTables: CircleTable[] = [];
  public reservations: Reservation[] = [];
  currentlySeatsReserved: Seat[] = [];
  currentSeats: Seat[] = [];
  public upcomingReservations$!: Observable<Reservation[]>;
  public status: any;
  public availableSeatIds: Number[] = [];

  roomId = 'SN156';

  constructor(
    public mapService: CsxlSeatMapService,
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

  getAvailableSeats(): Number[] {
    return this.mapService.availableSeatsFromBackend;
  }

  isSeatReserved(seat: Seat): Boolean {
    return !this.getAvailableSeats().some((id: any) => id === seat.id);
  }

  seatClicked(seat: Seat) {
    if (!this.isSeatReserved(seat)) {
      if (this.mapService.isSeatClicked(seat)) {
        this.mapService.removeClickedSeat(seat);
        this.seatsClicked = this.seatsClicked.filter((s) => s !== seat);
      } else {
        if (this.seatsClicked.length < 4) {
          this.mapService.addClickedSeat(seat);
          this.seatsClicked.push(seat);
        } else {
          this.snackBar.open('You can only select up to 4 seats.', 'Close', {
            duration: 3000
          });
        }
      }
    } else {
      this.snackBar.open('This seat is currently reserved.', 'Close', {
        duration: 3000
      });
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

  getSeatColor(seat: Seat): string {
    if (!seat.reservable) {
      return '#B0BEC5';
    } else if (this.mapService.isSeatClicked(seat)) {
      return '#FF5252';
    } else if (seat.sit_stand) {
      return 'orange';
    } else if (seat.has_monitor) {
      return '#689F38';
    } else {
      return '#3479be'; // Assuming you want to use the primary color defined in your theme
    }
  }
}
