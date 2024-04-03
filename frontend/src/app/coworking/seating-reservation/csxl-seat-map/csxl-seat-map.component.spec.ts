import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CsxlSeatMapComponent } from './csxl-seat-map.component';

describe('CsxlSeatMapComponent', () => {
  let component: CsxlSeatMapComponent;
  let fixture: ComponentFixture<CsxlSeatMapComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CsxlSeatMapComponent]
    }).compileComponents();

    fixture = TestBed.createComponent(CsxlSeatMapComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
