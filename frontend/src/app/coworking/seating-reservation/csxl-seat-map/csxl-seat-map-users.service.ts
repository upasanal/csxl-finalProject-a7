import { Injectable } from '@angular/core';
import { PublicProfile } from 'src/app/profile/profile.service';

@Injectable({
  providedIn: 'root'
})
export class SeatMapUserService {
  private users: PublicProfile[] = [];

  constructor() {}

  setUsers(users: PublicProfile[]) {
    this.users = users;
  }

  getUsers(): PublicProfile[] {
    return this.users;
  }

  clearUsers() {
    this.users = [];
  }
}
