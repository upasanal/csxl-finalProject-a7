import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SeatingConfirmationComponent } from './seating-confirmation.component';

describe('SeatingConfirmationComponent', () => {
  let component: SeatingConfirmationComponent;
  let fixture: ComponentFixture<SeatingConfirmationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SeatingConfirmationComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SeatingConfirmationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
