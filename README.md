# Movie Theater Challenge
#### Luke Gude

### **Description**:
Develop an algorithm that assigns seats based on priority. The algorithm is supposed to maximize customer satisfaction and customer safety. It should also place the reservations in the best seats in order of priority.

  * #### **Input**:
    * The input file should be formatted in a way that the reservation with the highest priority is at the top of the list, and the reservation with the lowest priority is at the bottom of the list.
    * Reservation identifier must have format of: ```R###``` followed by an integer
    * The input file will take in inputs if the file is formmated like:
      >```
      >R001 2 
      >R002 4 
      >R003 4 
      >R004 3
      >...
      >```
    * The algorithm will find the safest seat for the reservation while maintaining the best view.

  * #### **Output**:
    * The output will output a file called ```OutputFile.txt``` which contains the completed problem.
    * > ```
      >R001 F8, F9
      >R002 D8, D9, D10, D11
      >R003 H8, H9, H10, H11
      >R004 B8, B9, B10
      >...
      > ```
      
### **Instructions**:
  1. Open the directory that is housing the file ```MovieTheater.py```
  2. Create your input file using the style shown above or use an existing file that meets the requirements.
  3. Run the program by typing ```python MovieTheater.py [FileName]``` where ```FileName``` is the name of your input file.
  4. The program will run and create the output file, it will print out the location of the output file.


### **Assumptions**:
  * *Customer Satisfaction*
    * When a customer buys a ticket for a movie, the average choice is the middle of theater. This is because it is rare to find people who want to sit as close to the screen as possible. They prefer the middle/back.
    * People want to be a comfortable distance away from other people, but not on polar opposite sides of the theater.
    * If a reservation has more than 13 to a party, the requirement that they want to sit in the middle of the row goes down in order to compensate for space.
  * *Other*
  
    * The file will always meet the style guide.
    * Reservations with more than 20 will get denied and will not be able to fit in a row.
