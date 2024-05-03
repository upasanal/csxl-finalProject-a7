import {
  Component,
  Input,
  OnInit,
  OnChanges,
  SimpleChanges
} from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Room, SeatAvailability } from 'src/app/coworking/coworking.models';
import { AdminSeatMapWidgetComponent } from '../seat-map/seat-map.widget';
import { SeatAdminService } from '../../seats/admin-seats-service';
import { Router } from '@angular/router';
import { windowWhen } from 'rxjs';
import {MatFormFieldModule} from '@angular/material/form-field';
import {FormsModule} from '@angular/forms';
import {MatInputModule} from '@angular/material/input';

@Component({
  selector: 'seat-change',
  templateUrl: './seat-change.widget.html',
  styleUrls: ['./seat-change.widget.css']
})
export class AdminSeatChangeWidgetComponent implements OnInit {
  @Input() selectedSeat: SeatAvailability | undefined;
  seatForm!: FormGroup;
  constructor(
    private seatAdminService: SeatAdminService,
    public router: Router
  ) {}

  ngOnInit(): void {
    this.seatForm = new FormGroup({
      seatId: new FormControl(''),
      seatType: new FormControl('sitting'),
      xCoordinate: new FormControl(0),
      yCoordinate: new FormControl(0)
    });

    if (this.selectedSeat) {
      this.populateForm(this.selectedSeat);
    }
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['selectedSeat'] && this.seatForm) {
      const seat = changes['selectedSeat'].currentValue;
      this.populateForm(seat);
    }
  }

  private populateForm(seat: SeatAvailability): void {
    this.seatForm.patchValue({
      seatId: seat.id,
      seatType: this.seatType(seat.sit_stand, seat.has_monitor),
      xCoordinate: seat.x,
      yCoordinate: seat.y
    });
  }

  onSubmit(): void {
    console.log(this.seatForm.value);
    // Check if the form is valid and if a seat and room are selected
    if (this.seatForm.valid && this.selectedSeat) {
      // Extract new coordinates from the form
      const newX = this.seatForm.value.xCoordinate;
      const newY = this.seatForm.value.yCoordinate;

      // Pass the new coordinates along with the selectedSeat and room ID to the updateSeat method
      this.seatAdminService
        .updateSeat(this.selectedSeat, 'SN156', newX, newY)
        .subscribe({
          next: (updatedSeat) => {
            console.log('Updated seat:', updatedSeat);
            window.location.reload(); //Found on chatgpt and https://www.w3schools.com/jsref/met_loc_reload.asp
          },
          error: (err) => console.error('Failed to update seat:', err)
        });
    }
  }

  private seatType(seatingType: boolean, monitorStatus: boolean): string {
    if (monitorStatus == false) {
      return 'communal';
    } else if (seatingType == false) {
      return 'sitting';
    } else {
      return 'standing';
    }
  }
}
