# Interactive Seating Chart / Map Widget

Team A7 Members: [Upasana Lamsal](https://github.com/upasanal), [Jake Rogers](https://github.com/Jakerogers1), [Ellie Kim](https://github.com/ellieekimm), [Saishreeya Kantamsetty](https://github.com/skanta04)

## Overview:

The current seat reservation within the CSXL allows students to choose between three general sections: standing desks, sitting desks, or communal area seats. With the creation of an interactive seating chart and map widget, this feature enables students to reserve certain seats within the XL Coworking Space and Pair Programming Labs. By enabling students to reserve specific seats, the mapping of students to seats enforces that students only sit in spaces reserved specifically for them. Furthermore, CSXL ambassadors and administrators can better track space usage, ensuring students stay within their reserved times and make improvements upon the space if needed.

## Key Personas:

1. Ajay Ambassador has the ability to organize and keep track of students coming into the CSXL based on their designated seats reserved through the interactive seating widget, ensuring students do not overstay their reservations, along with all the abilities of Saishreeya Student.
2. Rumplestiltskin Root can manage the seats available across the CSXL and Pair Programming labs available to students and faculty by editing seats as needed on the interactive seating widget, along with all the abilities of both Saishreeya Student and Ajay Ambassador.
3. Saishreeya Student can reserve a specific seat in the CSXL or Pair Programming Labs for both themselves and up to a certain number of group-mates through the interactive seating widget by seeing which seats are available or reserved. Students must be signed in to their authenticated UNC account beforehand.

## User Stories:

- As Saishreeya Student, I want to see which seats in the CSXL and Pair Programming Labs are available so that I know which seats I am able to reserve for myself or, if needed, groupmates.
- As Saishreeya Student, I want to see a list of the current seats I have reserved and the time at which the reservation for these seats ends so that I’m aware of when I should leave those seats.
- As Rumplestiltskin Root, I want to see an interactive seating chart of the CSXL and Pair Programming Labs, as well as have the ability to edit seats in order to manage and update the seat's category and coordinates, if needed.
- As Ajay Ambassador, I want to see the countdown of time an individual has left in their reserved seat so I can notify them if they have extended their stay beyond their time slot.
- As Ajay Ambassador, I want to see the name of each person for every seat reservation to make sure everyone is accounted for and verify that reserved seats are occupied by the correct person.

## Wireframes / Mockups:

The entirety of the wireframes and user flow for the Interactive Seating Widget can be found on [Figma](https://www.figma.com/file/I6sLTbZJpwgl86TjOvJYts/seating-chart!!!?type=design&node-id=0%3A1&mode=design&t=umt55L5tI9GD6C3L-1).

### **Student**

The Coworking page, which is currently available on the CSXL website, will still contain information regarding room reservations and the number of seats in each category within the CSXL. With the updated reservation system, **Saishreeya Student** can reserve seats in the CSXL, by being redirected to another page.

<img src = "https://github.com/comp423-24s/csxl-final-team-a7/blob/stage/docs/images/student-wireframe1.png" width = 200>

**Saishreeya Student** is able to see an interactive seating chart of the CSXL, with numbered seats and a legend to inform the user of which type of seat each seat is, such as a standing, sitting, or communal area seat.

<img src = "https://github.com/comp423-24s/csxl-final-team-a7/blob/stage/docs/images/student-wireframe2.png" width = 200>

**Saishreeya Student** can select multiple seats, which are then colored green, and able to reserve seats with the button at the bottom of the page.

<img src = "https://github.com/comp423-24s/csxl-final-team-a7/blob/stage/docs/images/student-wireframe3.png" width= 200>

Once **Saishreeya Student** reserves seat(s),they are taken to a confirmation page with the time of their reservation, the seat numbers, and the time their reservation ends. It also provides **Saishreeya Student** the option to cancel their reservation.

<img src = "https://github.com/comp423-24s/csxl-final-team-a7/blob/stage/docs/images/student-wireframe4.png" width = 200>

Afterward, **Saishreeya Student** is able to access their reservation through the Coworking page, where the ability to make reservations is replaced with a short summary of their current reservation.

<img src = "https://github.com/comp423-24s/csxl-final-team-a7/blob/stage/docs/images/student-wireframe5.png" width = 200>

### <b>Ambassador</b>

<p>As <b>Ajay Ambassador</b>, the Coworking tab on the sidebar will be the same view as Saishreeya Students', however, the existing XL Ambassador tab will now include a list of all students' reservations in all rooms and will have an option to manage each reservation.</p>
<img src="https://github.com/comp423-24s/csxl-final-team-a7/assets/111532242/de64f371-3a08-49a9-b944-e3d6aab19963" width="350">
<p>When managing each reservation, the ambassador can view the person that has occupied that seat/reservation and the time left in that reservation. <b>Ajay Ambassador</b> is also able to cancel reservation if situation is permitting.</p>
<img src="https://github.com/comp423-24s/csxl-final-team-a7/assets/111532242/a2ab653b-81b4-433d-a32b-0dfd6cb86a23" width="350">

### <b>Root</b>

**Rumplestilkstin Root** has the XL Ambassador and Coworking tabs that have the same view as Ajay Ambassador's and Saishreeya Student's, respectfully.

On **Rumplestilkstin Root** Admin Page, there is a tab for Seats. This tab offers **Rumplestilkstin Root** the ability to view seats for each room, which is selected at the top, and manage each seat.

<img src = "https://github.com/comp423-24s/csxl-final-team-a7/blob/stage/docs/images/root-wireframe2.png" width = "350">

The manage seat button allows **Rumplestilkstin Root** to change a seat's X, Y coordinates, and their category. The Seat ID is autopopulated.

<img src = "https://github.com/comp423-24s/csxl-final-team-a7/blob/stage/docs/images/root-wireframe1.png" width = "350">

## Technical Implementation Opportunities and Planning:

### Existing Codebase:

##### Dependencies

- Users: When a reservation is made, we will need to track who made the reservation by connecting it to a user object
- Roles: Functionality will differ between roles. For example, a student should only see their reservations, ambassadors should have access to a page to control check-ins/check-outs, root should be able to oversee everything and override reservations, and change hours, and limits if needed.

##### Extensions

- Entirely new database tables and data schemes will be required to store seats that have an ID and vector coordinates, but they will need to exist in a way to interact with and live on top of the existing database.
- These reservation check-ins and check-outs will point a user to a specific seating area in the CSXL (one-to-many)
- The front end will need to be augmented to implement a seating chart with clickable features that allow users to select a reservation area.

### Page Components and Widgets:

- Seating Chart Widget: A visual representation of all the seats in a room.
- Seating Chart Legend Widget: A visual represnentation that distinguishes seats based on their category.
- Seat Widget: A visual representation of a singular seat in a room that has the ability to be selectable.
- Seating Chart Component: Shows the seating chart widget based on the current room and the ability for students to reserve specific seats.
- User Admin Mangaging Seats Component: Shows all seats available and the ability to manage existing seating.
- XL Ambassador Reservation Component: Shows all current reservations and the ability to manage those (cancel).
- XL Ambassador Seating Reservation Widget: Table row widget for current individual reservation entries, with the corresponding ID and user.
- User Admin Seating Deletion Widget: Table row widget for individual entries in the seating library, with the corresponding ID, name, and change of location functionality.
- User Admin Seat View/Edit Widget: Form for viewing/editing seats.

### Models:

- Reservation Model: Model stores the necessary reservation information such as name, seat id's reserved, and total time left in the reservation.
- Seat Model: A model that stores all the information about a given seat in the system. There will be identifiable unique IDs per seating, the seat category (standing/sitting), the room it is in (unique room ID), the X and Y coordinates of the seat, if a seat is reserved/occupied, and the specific reservation instance that is connected with the given seat if the seat has been reserved (an optional reservation ID).
- Room Model: This will store a room ID, room name, the floorplan SVG, and the seats associated with the room. Creating the model will make it so in the future, new room floorplans can be added more easily.
- User Model: This will have the user's PID (unique identifier), their first name, and their last name.

### API and Routes:

- Get Seats (/seating): Returns all the current seats we have available at the CSXL to eventually display them in the interactive seating chart. Used by every persona.
- Get All Rooms (/seating/room): Get all the rooms that are in the overall CSXL environment. Used by every persona.
- Get Specific Room Details/Floorplan (/seating/room/{room_id}): Return the specific Room's floorplan, name, and associated seats. Used by every persona.
- Get all seats given a room (seating/room/{room_id}/seats): Returns all of the unique seats in a certain room. Used by every persona.
- Get specific seat details (/seating/seat/{seat_id}): Allows the user to see the information of a current existing seat given its preassigned seat ID, including the seat category, the room it is in, the X and Y coordinates of the seat, and if a seat is reserved/occupied. Used by all personas.
- Put Seat (/seating/seat/{seat_id}): Allows the root user to edit a pre-existing seat in the CSXL, including its seat category, X Coordinate, and Y coordinate. Used by Rumpelstiltskin Root.
- Get all reservations (/seating/reservation): Returns all current reservations that have been made by any user. Used by Rumpelstiltskin Root and Ajay Ambassador.
- Get A User’s Seat Reservations (/seating/reservations/{user_pid}): Returns the time left of a person’s reservation(s), the start and stop times, and their first and last name. Used by all the personas.
- Post Seat Reservation (/seating/reservations): This will receive all information pertaining to a new seat reservation in order to update which seat is taken or not. Used by all personas.
- Delete Seat Reservation (/seating/reservation/{reservation_id}): Deletes a seat reservation to update the database with the most current and correct seat reservation status. Used by all personas.
- Put Seat Reservation (/seating/reservation/{reservation_id}): Updates a current seat reservation to update the database with the most current and correct seat reservation status. Used by all personas.
- Get reservations (/seating/reservations): Returns all of the current reservations so the Ambassador has a list of names of reservation users, time left, and seat location. Used by Ajay Ambassador and Rumpelstiltskin Root.

### Security and Privacy of Data:

- Only XL Ambassadors and Root can edit/create check-ins and check-outs.
- Root is the only persona that can update seat entries
- Saishreeya Student should not be able to cancel Sam Student's reservation
