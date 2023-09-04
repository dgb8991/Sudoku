""" Sudoku solution by Daniel Gonzalez Bernal """

import math  # Import the library we are going to use later on
from random import randint
import textwrap


def menu():  # Prints the control menu.
    print("")
    print("Welcome ! Please choose an option:")
    print("1. Create a Sudoku")
    print("2. Solve a Sudoku")
    print("3. Check a Sudoku")
    print("4. Exit")
    print("")

    while True:  # Program menu and options
        try:  # Try keyword allow us to check if the input char is a valid option
            option = int(input())
            if option == 1:
                print("Please enter the n value for the Sudoku (1-5):")
                n = int(input())
                maker(n)  # Calls the Sudoku maker function.
            elif option == 2:
                print("Please enter the sudoku file name")
                n = str(input())
                reader(n)  # Calls the reader function.
            elif option == 3:
                check_sudoku()  # Calls the check sudoku program.
            elif option == 4:
                exit(0)  # Closes the program.
            else:
                print("Please input a number between 1 and 4")
        except ValueError:  # If a wrong char is input, this except catch the error and handle it.
            print("Please input a number between 1 and 4")


def check_sudoku():  # This function reads the sudoku .txt and calls the fast and slow check functions.
    sudoku = []
    with open('solution.txt') as file:  # Reads the file were the sudoku is saved.
        data = file.read().splitlines()
    file.close()
    n = int(data[0])  # Reads and save the first row, it contains the N number of the sudoku.
    symbol_number = int(math.log10(n ** 2) + 1)  # Checks the number of digits we are going to use on the slice.
    del data[0]  # Delete the first row that contains the N number, this allows us to work easily with the data.
    for i in data:
        sudoku.append(textwrap.wrap(i, symbol_number))  # Slices each string into separate numbers.
    fast_check(sudoku, n)  # Calls the fast check function.
    print("Fast check result: PASS")
    slow_check(sudoku)  # Calls the slow check function.
    print("Slow check result: PASS")
    print("*** The given Sudoku is right ***")
    menu()  # Returns to the menu at the end.


def fast_check(sudoku, n):  # Checks the sudoku based on the sum of each row and column
    numbers_sum = sum(range(1, (n * n) + 1))  # Calculate the expected number for each row and column
    aux1 = 0  # Those aux variables helps to keep track of the sums results.
    aux2 = 0
    for i in range(0, len(sudoku)):  # Checks each row sum and compare it with the expected sum.
        for j in range(0, len(sudoku)):
            aux1 = int(sudoku[i][j]) + aux1
        if aux1 != numbers_sum:  # If the sums are not equal an error is show and returns to the menu.
            print("There is an error on row number: " + str(i + 1))
            menu()
        aux1 = 0
    for i in range(0, len(sudoku)):  # Checks each column sum and compare it with the expected sum.
        for j in range(0, len(sudoku)):
            aux2 = int(sudoku[j][i]) + aux2
        if aux2 != numbers_sum:  # If the sums are not equal an error is show and returns to the menu.
            print("There is an error on column number: " + str(i + 1))
            menu()
        aux2 = 0


def slow_check(sudoku):  # Checks the sudoku comparing the value with each cell
    for i in range(0, len(sudoku)):  # For each row it checks if each value has not duplicate.
        for j in range(0, len(sudoku)):
            for k in range(j + 1, len(sudoku)):
                if sudoku[i][j] == sudoku[i][k]:
                    print("There is an error on row number: " + str(i + 1))
                    print("Slow check result: FAIL...")
                    menu()  # If there's a duplicate an error is show and returns to the menu.
    for i in range(0, len(sudoku)):  # For each column it checks if each value has not duplicate.
        for j in range(0, len(sudoku)):
            for k in range(j + 1, len(sudoku)):
                if sudoku[j][i] == sudoku[k][i]:
                    print("There is an error on column number: " + str(i + 1))
                    print("Slow check result: FAIL...")
                    menu()  # If there's a duplicate an error is show and returns to the menu.


def reader(name):  # Read the txt with the blank sudoku
    sudoku = []  # Creates an empty list to save the sudoku information.
    with open(name + ".txt") as file:
        data = file.read().splitlines()
    file.close()
    n = int(data[0])  # Reads and save the first row, it contains the N number of the sudoku
    symbol_number = int(math.log10(n ** 2) + 1)
    del data[0]  # Delete the first row that contains the N number, this allows us to work easily with the data.
    for i in data:
        sudoku.append(textwrap.wrap(i, symbol_number))
    for i in range(n * n):  # Transforms the data from string into int.
        for j in range(n * n):
            if sudoku[i][j].isdigit():
                sudoku[i][j] = int(sudoku[i][j])
            else:
                sudoku[i][j] = 0  # Change the empty spaces into zeros.
    if sudoku_solver(sudoku, 0, 0, n):  # Calls the solver function.
        puzzle(sudoku, n)
    else:
        print("Solution does not exist")


def puzzle(sudoku, n):
    file1 = open("solution.txt", "w")
    file1.write(str(n) + "\n")
    # Create a file with the size of the sudoku at the top
    symbol_number = int(math.log10(n ** 2) + 1)
    # Calculate maximum number of digits used
    # Print each row with preceding 0s on small numbers
    for i in range(n * n):
        for j in range(n * n):
            sym = str(sudoku[i][j])
            while len(sym) < symbol_number:
                sym = '0' + sym
            file1.write(sym)
        file1.write("\n")
    file1.close()
    print("*** Solved! ***")
    print("File with solution created")
    menu()


def save_new(sudoku, n):
    file1 = open("sudoku.txt", "w")
    file1.write(str(n) + "\n")
    # Create a file with the size of the sudoku at the top
    symbol_number = int(math.log10(n ** 2) + 1)
    # Calculate maximum number of digits used
    # Print each row with preceding 0s on small numbers
    # When there is no value, print it as a several '-'
    for i in range(n * n):
        for j in range(n * n):
            if sudoku[i][j] != 0:
                sym = str(sudoku[i][j])
                while len(sym) < symbol_number:
                    sym = '0' + sym
            else:
                sym = ''
                while len(sym) < symbol_number:
                    sym += '-'
            file1.write(sym)
        file1.write("\n")
    file1.close()
    print("New sudoku file created")
    return


def solve(grid, row, col, num, n):
    # Check this row does not contain num
    for x in range(n * n):
        if grid[row][x] == num:
            return False
    # Check this column does not contain num
    for x in range(n * n):
        if grid[x][col] == num:
            return False
    # Check this box does not contain num
    start_row = row - row % n
    start_col = col - col % n
    for i in range(n):
        for j in range(n):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True


def sudoku_solver(grid, row, col, n):
    # When the end of the sudoku is reached return
    if row == (n * n) - 1 and col == (n * n):
        return True
    # If end of row is reached, go to next row
    if col == (n * n):
        row += 1
        col = 0
    # If cell is not empty, go to next one
    if grid[row][col] > 0:
        return sudoku_solver(grid, row, col + 1, n)
    # Try all possible values on this cell
    # If no values are possible, backtrack
    # If a valid value results in no solution, when we backtrack
    # a bad cell will be marked as 0 again
    for num in range(1, (n * n) + 1, 1):
        if solve(grid, row, col, num, n):
            grid[row][col] = num
            if sudoku_solver(grid, row, col + 1, n):
                return True
        grid[row][col] = 0
    return False


def maker(n):
    # Choose an optimal amount of clues for each number
    if n == 1:
        clues = 0
    elif n == 2:
        clues = 4
    elif n == 3:
        clues = 17
    elif n == 4:
        clues = 56
    elif n == 5:
        clues = 150
    else:
        clues = (n ** 2) * (n + 1)
    # Allocates memory for an empty sudoku
    sudoku = []
    for row in range(n * n):
        sudoku.append([0] * (n * n))
    # Introduces a number of clues, while validating them
    filled = 0
    while filled < clues:
        row, col, try_num = randint(0, n * n - 1), \
                            randint(0, n * n - 1), \
                            randint(1, n * n)
        if sudoku[row][col] == 0 and solve(sudoku, row, col, try_num, n):
            sudoku[row][col] = try_num
            filled += 1
    # Saves a possible sudoku and tries to validate it.
    # If it is not valid, start from nothing. Otherwise, save its solution.
    save_new(sudoku, n)
    print("Trying to solve...")
    if sudoku_solver(sudoku, 0, 0, n):
        puzzle(sudoku, n)
    else:
        print("Solution does not exist, creating a new sudoku")
        maker(n)


menu()  # Starts the program
