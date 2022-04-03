README
this is the link of the YouTube video of our project 
https://youtu.be/zj8FlAr7sQU

0. Instructions
0.1
There are 3 terminals/GUI (User part, Operator part, Manager part). Only users need to log in with their username and password, while operators and manager just need to enter right password to confirm, because there won't be too many operators and mangers.
0.2
There are 500 bikes and 5 locations (location1, location2, location3, location4, location5) at first, and each location holds 100 bikes. You can increase bikes to any location, but you cannot increase location. Note that each location can hold at most 200 bikes, that means there will be at most 5*200=1000 bikes in this system.

1. User part
Note: The database has already been initialized and saved some accounts.
Here are login accounts:
Username: Lisa        password: q1234567
Username: pika        password: pika1234

1.1 Run Customer.py 

1.2 Login / Register page 
1.2.1 Registration Function
Stap1: Enter username and password with length of 8 digits and has at least one 		    number. 
Step2: Press register button.
       Note:
 It allows the user to create a new account the user can enter any username, 	but there are some restrictions on the password the password length must be 	8 digits or more and contains at least one number. 

1.2.2 Login Function
Stap1: Enter username and password, use one of these usernames and                			password. 
Step2: press login button
Note:
allows the user to enter a username and password. The username will be checked if it in the database or not, if not the system will ask the user to create a new account.

1.3 Report a damaged bike
Step1:  Select Report from main menu. 
Step2:  Enter the Bike ID of the damaged bike. 
step3:  Press Submit button to confirm send. 
step4:  When the display is submitted successfully, you can click the Return button to return to the main menu.

1.4 Rent a bike Function
Step1: select Rent from main menu. 
Step2: select the start location. 
step3: press rent button to conform the rent process.
Note:
Allows the user to select any location to rent a bike from it. If the selected location has no bike to rent, then the system will ask the user to select another location. 
If the selected location has bikes but they are defectives, then the system will ask the user to select another location. 

1.5 Return Function
Setep1: select the end location.
Note:
Allows the user to select any location to return a bike to it. If the selected location is full with bikes and have no available parking, then the system will ask the user to select another location.

1.6 Payment Function
Allow the user to pay for his/her journey, and also connecting with bank balance, when the user clicks the payment, it will pay through bank account.\
If money is not enough, it will tell you to charge money, but still can record this journey.

1.7 Check and Charge money through bank account
After user’s login, they can check how much money now saving in their account, if money is 0, it will remind you to charge money. 
Every user can charge money if they want, once ten pounds.
After charging money, it will show the number instantly.

2. Operator part

2.1 Run Operator.py
Confirming interface will display, operators enter the correct password to log in.
Step1:  Enter the password. (default password: 0)
Step2:  Click "confirm" or type return after entering password.
Note:
If entered password is wrong or nothing entered, the system will throw a warning, then clear the password box.

2.2 Track bikes
Step1:  Enter a bike ID in input box in fist line to track a specific bike, or select bike status and location in combo box to track all bikes matched to the condition. 
Step2:  Click Track button, then matched results will be displayed. If 0 bike matches to the filter condition, the system will throw an information, but your last track results are still there and can be operated.
Note:
The system will track by ID first. That means, if you want to track bikes by status and location, make sure the input box of ID is empty.
If you enter invalid number (like -10)/even not a number in input box, the system will throw a warning.

2.3 Repair bikes
Step1:  Click defective bike(s) in tracking results to select them. Of course, you can use "ctrl" or "shift" to select more bikes at once.
Step2:  Click repair button to repair all bikes you selected. 
Note: 
If there are working/normal bikes in your selections, the system will throw a warning, then repair other (defective) bikes in selections.

2.4 Move bikes
Step1:  Click defective bike(s) in tracking results to select them. Of course, you can use "ctrl" or "shift" to select more bikes at once.
Step2:  Select a target location in combo box above the move button.
Step3:  Click move button to move all selected bikes to selected location. 
Note: 
If the target location does not have enough space to hold all selected bikes (at most 200 bikes in each location), the system will throw a warning and cancel this move operation. 
If there are working bikes in your selections, or the target location you selected is same to the bikes’ original location, the system will throw a warning, then move other bikes to the target location.

2.5 Add bikes
Step1:  Enter the number of bikes you want to add in the input box above Add button.
Step2:  Select a target location in combo box above Add button.
Step3:  Click Add to add new bikes.
Note:
If the target location does not have enough space to hold bikes you want to add (at most 200 bikes in each location), the system will throw a warning and cancel this add operation. 
If you enter nothing/invalid number (like -10)/even not a number in input box, the system will throw a warning.

3. Manager part

This is a terminal for Managers. This terminal only need password to login and the default password is 1.
Manager can click the "Confirm" after entering "1" as password. And If input is wrong or nothing entered, the system will throw a warning.
Then there are only three buttons in Manager page. One is Report one is Chart and another is Clear.

3.1 Report
When Manager enter the time into start and end time box, and if they use the report button, it will generate reports showing all bike activities.
The report has 6 columns which are bike id, user id, start time, end time, start location, end location and activity type.
Bike id is a unique code to identify bike, and user id is same as bike id.
The start time and the end time is the bike use time period and included in the manager's input.
The start location and end location are the bike location change and if the bike just be repaired it would not change.
The activity type is what the bike was done in that time period.

3.2 Chart
This is a button that can generate a bar chart. Blue columns indicate the number of starting locations in areas represented by the X axis, and red is end locations.
This bar chart shows the use of each location during the time period chosen by the manager.

3.3 Clear
If they use the Clear button, the report generated in page will be cleared.






