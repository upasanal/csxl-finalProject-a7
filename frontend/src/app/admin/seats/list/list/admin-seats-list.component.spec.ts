import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminSeatsListComponent } from './admin-seats-list.component';

describe('AdminSeatsListComponent', () => {
  let component: AdminSeatsListComponent;
  let fixture: ComponentFixture<AdminSeatsListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AdminSeatsListComponent]
    }).compileComponents();

    fixture = TestBed.createComponent(AdminSeatsListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
