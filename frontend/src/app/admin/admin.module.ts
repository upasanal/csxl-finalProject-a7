import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

import { MatTableModule } from '@angular/material/table';
import { MatTabsModule } from '@angular/material/tabs';
import { MatDialogModule } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import { MatListModule } from '@angular/material/list';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { AdminComponent } from './admin.component';
import { AdminRoutingModule } from './admin-routing.module';
import { MatSelectModule } from '@angular/material/select';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatInputModule } from '@angular/material/input';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { MatCard, MatCardModule } from '@angular/material/card';

import { AdminUsersListComponent } from './users/list/admin-users-list.component';
import { AdminRolesListComponent } from './roles/list/admin-roles-list.component';
import { AdminRoleDetailsComponent } from './roles/details/admin-role-details.component';
import { AdminOrganizationListComponent } from './organization/list/admin-organization-list.component';
import { AdminSeatsListComponent } from './seats/list/list/admin-seats-list.component';
import { AdminSeatMapWidgetComponent } from './widgets/seat-map/seat-map.widget';
import { AdminSeatChangeWidgetComponent } from './widgets/seat-change/seat-change.widget';

@NgModule({
  declarations: [
    AdminComponent,
    AdminUsersListComponent,
    AdminRolesListComponent,
    AdminRoleDetailsComponent,
    AdminOrganizationListComponent,
    AdminSeatsListComponent,
    AdminSeatMapWidgetComponent, 
    AdminSeatChangeWidgetComponent

    ],
  imports: [
    CommonModule,
    AdminRoutingModule,
    MatTabsModule,
    MatTableModule,
    MatDialogModule,
    MatButtonModule,
    MatSelectModule,
    MatFormFieldModule,
    MatInputModule,
    MatPaginatorModule,
    MatListModule,
    MatAutocompleteModule,
    FormsModule,
    ReactiveFormsModule,
    MatCardModule, 
    ]
})
export class AdminModule {}
