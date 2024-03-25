# Interactive Seating Chart / Map Widget 
Team A7 Members: [Upasana Lamsal](https://github.com/upasanal), [Jake Rogers](https://github.com/Jakerogers1), [Ellie Kim](https://github.com/ellieekimm), [Saishreeya Kantamsetty](https://github.com/skanta04)

## Overview: 
The current seat reservation within the CSXL allows students to choose between three general sections: standing desks, sitting desks, or communal area seats. With the creation of an interactive seating chart and map widget, this feature enables students to reserve certain seats within the XL Coworking Space and Pair Programming Labs. By enabling students to reserve specific seats, the mapping of students to seats enforces that students only sit in spaces reserved specifically for them. Furthermore, CSXL ambassadors and administrators can better track space usage, ensuring students stay within their reserved times and make improvements upon the space if needed.
## Key Personas:
1. Ajay Ambassador has the ability to organize and keep track of students coming into the CSXL based on their designated seats reserved through the interactive seating widget, ensuring students do not overstay their reservations, along with all the abilities of Saishreeya Student. 
2. Rumplestiltskin Root can manage the seats available across the CSXL and Pair Programming labs available to students and faculty by editing seats as needed on the interactive seating widget, along with all the abilities of both Saishreeya Student and Ajay Ambassador. 
3. Saishreeya Student can reserve a specific seat in the CSXL or Pair Programming Labs for both themselves and up to a certain number of group-mates through the interactive seating widget by seeing which seats are available or reserved. Students must be signed in to their authenticated UNC account beforehand.
## User Stories: 
* As Saishreeya Student, I want to see which seats in the CSXL and Pair Programming Labs are available so that I know which seats I am able to reserve for myself or, if needed, groupmates.
* As Saishreeya Student, I want to see a list of the current seats I have reserved and the time at which the reservation for these seats ends so that I’m aware of when I should leave those seats.
* As Rumplestiltskin Root, I want to see an interactive seating chart of the CSXL and Pair Programming Labs, as well as have the ability to edit seats in order to manage and update the seat's category and coordinates, if needed.
* As Ajay Ambassador, I want to see the countdown of time an individual has left in their reserved seat so I can notify them if they have extended their stay beyond their time slot. 
* As Ajay Ambassador, I want to see the name of each person for every seat reservation to make sure everyone is accounted for and verify that reserved seats are occupied by the correct person. 
## Wireframes / Mockups: 
## Technical Implementation Opportunities and Planning:
### Existing Codebase: 
  ##### Dependencies
  * Users: When a reservation is made, we will need to track who made the reservation by connecting it to a user object
  * Roles: Functionality will differ between roles. For example, a student should only see their reservations, ambassadors should have access to a page to control check-ins/check-outs, root should be able to oversee everything and override reservations, and change hours, and limits if needed.
  ##### Extensions
  * Existing database tables and data schemas for coworking reservations may be useful, however, an entirely new database will most likely be needed to reserve specific locations in the CSXL, whereas the current one is generic and broad and encompasses all similar typed area reservations. 
  * There will be tables that include specific seating areas, check-ins/check-outs further allowing users to a user history
  * These reservation check-ins and check-outs will point a user to a specific seating area in the CSXL (one-to-one)
  * The front end will need to be augmented to implement a seating chart with clickable features that allow users to select a reservation area.
  * The current ambassador coworking component will also need to be updated to accommodate the features of reserving specific seats.
### Page Components and Widgets:
* Reservation Component: Side-nav route accessible for all user stories. Displays seating chart, user checkouts, and user reservations. 
* XL Ambassador Reservation Component: create a new tab for reservations for XL Ambassador. Create a table of check-in widgets so Ambassadors can check in or check out students.
* XL Ambassador Check-in widget: Form for checking in/out students.
* XL Ambassador Seating Reservation Widget: Table row widget for individual entries in the seating library, with the corresponding ID and check-in/check-out functionality.
* User Admin Seating Deletion Widget: Table row widget for individual entries in the seating library, with the corresponding ID, name, and deletion functionality.
* User Admin Seat View/Edit Widget: Form for viewing/editing seats.
* User Admin Seat Creating Widget: Form for creating seat entries.
* User Admin Seat Management Component: New route so that admins can add/delete items from the seat library.
* User Admin View/Edit Component: Interface for viewing/editing existing seating.
* User Admin Seating Creation Component: Interface for adding new seats to the seating library.
* Seating Card Widget: Cards for seats in the CSXL. Displays availability status, ID number, seat type, reservation time frame, and a button to reserve.
### Models: 
* Reservation Model: Model stores the necessary reservation information, including the seat reserved ID, the PID of the user, the total time the reservation is reserved for, the start and end times, and a unique reservation ID.
* Seat Model: A model that stores all the information about a given seat in the system. There will be identifiable unique IDs per seating, the seat category (standing/sitting), the room it is in (unique room ID), the X and Y coordinates of the seat, if a seat is reserved/occupied, and the specific reservation instance that is connected with the given seat if the seat has been reserved (an optional reservation ID)
* Room Model: This will store a room ID, room name, the floorplan SVG, and the seats associated with the room. Creating the model will make it so in the future, new room floorplans can be added more easily.
* User Model: This will have the user's PID (unique identifier), their first name, and their last name. 
### API and Routes:
* Get Seats (/seating): Returns all the current seats we have available at the CSXL to eventually display them in the interactive seating chart. Used by every persona.
* Get All Rooms (/seating/room): Get all the rooms that are in the overall CSXL environment. Used by every persona.
* Get Specific Room Details/Floorplan (/seating/room/{room_id}): Return the specific Room's floorplan, name, and associated seats. Used by every persona.
* Get all seats given a room (seating/room/{room_id}/seats): Returns all of the unique seats in a certain room. Used by every persona.
* Get specific seat details (/seating/seat/{seat_id}): Allows the user to see the information of a current existing seat given its preassigned seat ID, including the seat category, the room it is in, the X and Y coordinates of the seat, and if a seat is reserved/occupied. Used by all personas. 
* Put Seat (/seating/seat/{seat_id}): Allows the root user to edit a pre-existing seat in the CSXL, including its seat category, X Coordinate, and Y coordinate. Used by Rumpelstiltskin Root.
* Get all reservations (/seating/reservation): Returns all current reservations that have been made by any user. Used by Rumpelstiltskin Root and Ajay Ambassador.
* Get A User’s Seat Reservations (/seating/reservations/{user_pid}): Returns the time left of a person’s reservation(s), the start and stop times, and their first and last name. Used by all the personas.
* Post Seat Reservation (/seating/reservations): This will receive all information pertaining to a new seat reservation in order to update which seat is taken or not. Used by all personas.
* Delete Seat Reservation (/seating/reservation/{reservation_id}): Deletes a seat reservation to update the database with the most current and correct seat reservation status. Used by all personas.
* Put Seat Reservation (/seating/reservation/{reservation_id}): Updates a current seat reservation to update the database with the most current and correct seat reservation status. Used by all personas.
* Get reservations (/seating/reservations): Returns all of the current reservations so the Ambassador has a list of names of reservation users, time left, and seat location. Used by Ajay Ambassador and Rumpelstiltskin Root.
  
### Security and Privacy of Data:
* Only XL Ambassadors and Root can edit/create check-ins and check-outs.
* Root is the only persona that can update seat entries
* Saishreeya Student should not be able to cancel Sam Student's reservation
