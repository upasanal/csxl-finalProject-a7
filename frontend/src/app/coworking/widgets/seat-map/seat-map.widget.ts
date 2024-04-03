import { Component, OnInit } from '@angular/core';
import { Seat, SeatAvailability } from 'src/app/coworking/coworking.models';
import { CsxlSeatMapService } from '../../seating-reservation/csxl-seat-map/csxl-seat-map.service';
import { CoworkingService } from '../../coworking.service';
import { ReservationService } from '../../reservation/reservation.service';

@Component({
  selector: 'seat-map',
  templateUrl: './seat-map.widget.html',
  styleUrls: ['./seat-map.widget.css']
})
export class SeatMapWidgetComponent implements OnInit {
  seats: Seat[] = [];
  seatsClicked: Seat[] = [];
  seatsReserved: Seat[] = []; // seats only become reserved once user presses reserved button

  constructor(
    private mapService: CsxlSeatMapService,
    private coworkService: CoworkingService,
    private reserveService: ReservationService
  ) {}
  // seats only become reserved once user presses reserved button

  ngOnInit(): void {
    this.seats = this.mapService.getSeats();
  }

  seatClicked(seat: Seat) {
    if (this.mapService.isSeatClicked(seat)) {
      this.mapService.removeClickedSeat(seat);
    } else {
      this.mapService.addClickedSeat(seat);
    }
  }

  isButtonActive(): boolean {
    return this.mapService.getClickedSeats().length > 0;
  }

  seatPressed(seat: Seat) {
    return this.mapService.isSeatClicked(seat);
  }

  reserveSeats() {
    this.seatsReserved = this.mapService.getClickedSeats();
    this.mapService.reserveSeats(this.seatsReserved);
    let reservedSeatAvails: SeatAvailability[] =
      this.mapService.convertSeatsToSeatAvailability(this.seatsReserved);
    this.coworkService.draftReservation(reservedSeatAvails).subscribe({
      next: (value) => this.reserveService.confirm(value)
    });
  }

  clearReserves() {
    this.mapService.clearReservations();
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
