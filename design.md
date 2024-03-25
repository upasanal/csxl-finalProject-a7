# Interactive Seating Chart / Map Widget 
Team A7 Members: [Upasana Lamsal](https://github.com/upasanal), [Jake Rogers](https://github.com/Jakerogers1), [Ellie Kim](https://github.com/ellieekimm), [Saishreeya Kantamsetty](https://github.com/skanta04)

## Overview: 
The current seat reservation within the CSXL allows students to choose between three general sections: standing desks, sitting desks, or communal area seats. With the creation of an interactive seating chart and map widget, this feature enables students to reserve certain seats within the XL Coworking Space and Pair Programming Labs. By enabling students to reserve specific seats, the mapping of students to seats enforces that students only sit in spaces reserved specifically for them. Furthermore, CSXL ambassadors and administrators can better track space usage, ensuring students stay within their reserved times and make improvements upon the space if needed.
## Key Personas:
1. Ajay Ambassador has the ability to organize and keep track of students coming into the CSXL based on their designated seats reserved through the interactive seating widget, ensuring students do not overstay their reservations, along with all the abilities of Saishreeya Student. 
2. Rumplestiltskin Root can manage the seats available across the CSXL and Pair Programming labs available to students and faculty by adding, removing, or editing seats as needed on the interactive seating widget, along with all the abilities of both Saishreeya Student and Ajay Ambassador. 
3. Saishreeya Student can reserve a specific seat in the CSXL or Pair Programming Labs for both themselves and up to a certain number of group-mates through the interactive seating widget by seeing which seats are available or reserved. Students must be signed in to their authenticated UNC account beforehand.
## User Stories: 
* As Saishreeya Student, I want to see which seats in the CSXL and Pair Programming Labs are available so that I know which seats I am able to reserve for myself or, if needed, groupmates.
* As Saishreeya Student, I want to see a list of the current seats I have reserved and the time at which the reservation for these seats ends so that I’m aware of when I should leave those seats.
* As Rumplestiltskin Root, I want to see an interactive seating chart of the CSXL and Pair Programming Labs, as well as have the ability to create, edit, and delete seats in order to manage and update the seats, if needed.
* As Ajay Ambassador, I want to see the countdown of time an individual has left in their reserved seat so I can notify them if they have extended their stay beyond their time slot. 
* As Ajay Ambassador, I want to see the name of each person at every seat to make sure everyone is accounted for and verify that reserved seats are occupied by the correct person. 
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
* Reservation Model: Model stores the necessary reservation information, including the seat reserved, the PID of the user, the first and last name of the user, the start time, and the total time the reservation is reserved for 
* Seat Model: A model that stores all the information about a given seat in the system. There will be identifiable unique IDs per seating, the location group associated (like what table), and the specific reservation instance that is connected with the given seat if the seat has been reserved
* Full Seating Model: This will store all the information required for all the tables and specific seating spots we have in general, reserved or not reserved, encapsulating the seat model we also have. 
* Available seating Model: This will be a submodel of the full seating model that only has the non-reserved seat models available.
* Room Model 
### API and Routes:
* Get Seats (/seating): Returns all the current seats we have available at the CSXL to eventually display them in the interactive seating chart. Used by every persona.
* Get Occupied Sear (/seating): Returns all the sets that have been reserved in the inventory so we know what seats are closed off from bookings and the seats that are still open for booking. Used by all personas.
* Get A User’s Seat Reservation  (/seating/reservations/{user_pid}): Returns the time left of a person’s reservation, the start and stop times, and their first and last name. Used by all the personas.
* Post Seat Reservation (/seating/reservation): This will receive all information pertaining to a new seat reservation in order to update which seat is taken or not. Used by Ajay Ambassador and Rumpelstiltskin Root. 
* Delete Seat Reservation (/seating/reservation): Deletes a seat reservation to update the database with the most current and correct seat reservation status. Utilized by Ajay Ambassador and Rumpelstiltskin Root. 
* Get reservations(/seating/reservations): Returns all of the current reservations so the Ambassador has a list of names of reservation users, time left, and seat location. Used by Ajay Ambassador and Rumpelstiltskin Root. 
* Post New Seat(/seating/post): Allows the root user to add a new seat in the CSXL, including its table type and location and all other necessary information for the new seat. Used by Rumpelstiltskin Root. 
* Delete a Seat  (/seating/delete): Allows the root user to delete an existing seat in the CSXL that has been removed. The purpose is to update the seats people can reserve in the CSXL to reflect what is actually existing. Used by Rumpelstiltskin Root.
### Security and Privacy of Data:
* Only XL Ambassadors and Root can edit/create check-ins and check-outs.
* Root is the only persona that can add/delete seat entries
* Saishreeya Student should not be able to cancel Sam Student's reservation
