import sys

# Constants
STARTING_ROW = 5
LEFT = 0
RIGHT = 19
BACK = 9
FRONT = 0
STARTING_SEAT = 7


# Checks to see if the selected section is in bounds
def inBounds(section, reservation=0):
    for index, seat in enumerate(section):
        if (index not in range(0, 20)):
            return False
    # if the reservation selection is above the max number of seats
    if reservation and reservation > len(section):
        return False
    return True

# Checks to see if the specific seat is in range


def seatInBounds(row, seat):
    return (row in range(0, 10)) and (seat in range(0, 20))


# Structure to store the seats in individual rows
class Row():
    def __init__(self, data):
        self.data = data  # Row Letter
        self.seats_open = 20
        self.seats = [0] * 20

    # Print Function for Row
    def __str__(self):
        return str(self.data)


# Class to handle the input files
class FileHandler():
    def __init__(self, file_name=sys.argv[1]):
        self.file_name = file_name
        self.file = open(file_name, "r")
        self.lines = self.file.readlines()
        self.contents = {}
        self.reservation_amount = self.parse_input()

    # Reads the input file and stores into contents
    def parse_input(self):
        for count, line in enumerate(self.lines):
            line = line.strip()
            line = line.split(" ")
            self.contents[line[0]] = line[1]
        return count+1

# Class to hold the information for the theater


class MovieTheater:
    def __init__(self):
        self.layout = self.fill_rows()  # Create a 10x20 matrix of seats with rows
        self.input_file = FileHandler()  # The class' file handler
        self.reservations = self.input_file.contents
        self.row_priority = {5: 20, 3: 20, 7: 20, 1: 20,
                             9: 20, 4: 20, 8: 20, 2: 20, 6: 20, 0: 20}  # Row priority with available spaces
        self.row_priority_list = [5, 3, 7, 1, 9, 4,
                                  8, 2, 6, 0]  # Row priority in a list

    # Takes in row number and seat number and returns a subset of potential seats
    def seatArray(self, row, seat, reservation):
        return self.layout[row].seats[seat:seat+reservation]

    # Driver function to find a seat
    def findSeat(self):
        index = 0  # Keep track of the Row priority
        for i in self.reservations:
            # If successfully finds a seat
            if (self.find_seat(self.reservations[i], i, index)):
                index += 1  # Move on to the next row

    def find_seat(self, reservation, reservationID, i):
        reservation = int(reservation)  # Convert any type to int
        temp_seat = STARTING_SEAT  # Start in the middle for most satisfaction
        # If the reservation has less than the amount of availible seats in a row
        if self.row_priority[self.row_priority_list[i]] >= reservation:
            temp_row = self.row_priority_list[i]
            seats = self.seatArray(temp_row, temp_seat, reservation)
            if not inBounds(seats, reservation):
                # If the reservation is over 13, move the party to the left most section
                seats = self.seatArray(temp_row, LEFT, reservation)
            if inBounds(seats, reservation):
                # Tries to find an open seat around the same seat and row
                while 1 in seats or (temp_seat+reservation > 20):
                    if temp_seat+reservation > RIGHT:
                        temp_seat = LEFT
                    if temp_row + 1 > 9:
                        temp_row = 0
                    else:
                        temp_row += 1
                    seats = self.seatArray(temp_row, temp_seat, reservation)
                takenSeats = []  # List of seats taken by the reservation
                for n in range(temp_seat, temp_seat+reservation):
                    # Sets the seat as taken
                    self.layout[temp_row].seats[n] = 1
                    # Adds the row letter and seat number
                    takenSeats.append(chr(temp_row+65)+str(n+1))
                # Adds the list to the dictionary
                self.reservations[reservationID] = takenSeats
                # Updates the amount of available seats
                self.row_priority[temp_row] -= reservation
                return True
            else:
                # Could not find an open seat fitting the constraints
                self.reservations[reservationID] = "No Seats Available"
                return False

    # Function to create the theater (10x20 matrix)
    def fill_rows(self):
        row_list = []
        for i in range(10):
            row_list.append(Row(chr(i+65)))
        return row_list

    # Function to write to the output file
    def output_to_file(self):
        outputFile = open("OutputFile.txt", "w+")
        for i in self.reservations:
            if type(self.reservations[i]) is not list:
                outputFile.write('{} {}\n'.format(i, 'No Seats Available'))
            else:
                outputFile.write('{} {}\n'.format(
                    i, ', '.join(self.reservations[i])))

    # Function to print the theater visually (Debugging)
    def printTheater(self):
        for row in self.layout:
            print(row, row.seats)


if __name__ == '__main__':
    movie = MovieTheater()
    movie.findSeat()
    movie.output_to_file()
