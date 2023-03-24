# This is Jonathan Farkas' integration project.
# This program contains a Maze game as well as parts from the previous sprint present to
# fill the project's requirements.

# This function is used in the maze game to find if the desired movement direction is valid or not.
def move_valid(direction, f_maze, position):
    if direction == 'w':
        if f_maze[position[0] - 1][position[1]] != '|':
            return True
        else:
            return False
    if direction == 'a':
        if f_maze[position[0]][position[1] - 1] != '|':
            return True
        else:
            return False
    if direction == 's':
        if f_maze[position[0] + 1][position[1]] != '|':
            return True
        else:
            return False
    if direction == 'd':
        if f_maze[position[0]][position[1] + 1] != '|':
            return True
        else:
            return False


def maze_game():
    # Declaration of relevant variables including the maze itself as a two-dimensional array and the player's
    # starting position.
    maze = [['|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
            ['|', '+', 'O', 'O', 'O', 'O', 'O', '|', 'O', '|', 'O', 'O', 'O', 'O', 'O', 'O', '|'],
            ['|', 'O', '|', '|', 'O', '|', 'O', '|', 'O', 'O', 'O', '|', '|', '|', 'O', '|', '|'],
            ['|', 'O', '|', 'O', '|', 'O', 'O', '|', 'O', '|', 'O', '|', 'O', 'O', 'O', 'O', '|'],
            ['|', 'O', 'O', 'O', '|', '|', '|', 'O', '|', 'O', 'O', '|', 'O', '|', '|', 'O', '|'],
            ['|', 'O', '|', 'O', '|', 'O', 'O', 'O', '|', 'O', '|', 'O', '|', 'O', 'O', 'O', '|'],
            ['|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O', 'O', 'O', '|', 'O', '|', '|', '|'],
            ['|', 'O', 'O', 'O', 'O', 'O', '|', 'O', 'O', '|', '|', 'O', '|', 'O', 'O', 'O', '|'],
            ['|', '|', '|', '|', 'O', '|', 'O', '|', 'O', 'O', '|', 'O', '|', '|', '|', 'O', '|'],
            ['|', 'O', 'O', 'O', 'O', '|', 'O', '|', 'O', '|', 'O', 'O', 'O', 'O', '|', 'O', '|'],
            ['|', 'O', '|', '|', '|', 'O', 'O', '|', 'O', 'O', '|', '|', '|', 'O', '|', 'O', '|'],
            ['|', 'O', 'O', 'O', 'O', '|', 'O', '|', '|', 'O', '|', 'O', 'O', 'O', '|', 'O', '|'],
            ['|', '|', '|', '|', 'O', '|', 'O', 'O', 'O', 'O', '|', 'O', '|', '|', '|', 'O', '|'],
            ['|', 'O', 'O', 'O', 'O', 'O', '|', 'O', '|', 'O', 'O', 'O', '|', 'O', 'O', 'O', '|'],
            ['|', 'O', '|', '|', '|', '|', 'O', 'O', 'O', '|', '|', 'O', '|', 'O', '|', '|', '|'],
            ['|', 'O', 'O', '|', 'O', 'O', 'O', '|', 'O', '|', 'O', 'O', '|', 'O', 'O', '+', '|'],
            ['|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]
    current_pos = [1, 1]
    print("\nWelcome to the maze game!"
          "You will start in the top left corner of the maze, your position is indicated by a plus sign (+).\n"
          "Walls are marked with | and empty space is marked with an O.\n"
          "You will use w, a, s, and d inputs to move.\n\n"
          "Input 'Ready' to begin!\n")
    ready = False
    while not ready:
        is_user_ready = input()
        if is_user_ready == "Ready":
            ready = True
        else:
            print("I can wait all day..")

    # While loop which runs the maze game, with the condition for the loop to stop being the current position being
    # that of the player's goal.
    while current_pos != [15, 15]:
        for i in range(17):
            print("")
            for j in range(17):
                print(maze[i][j], end=' ')

        # While loop which accepts a correct input from the player and tests the validity of that input using
        # the move_valid function
        movement = input("\nInput movement:\n")
        move_is_valid = False
        while not move_is_valid:
            while (movement != 'w' and movement != 'a') and (movement != 's' and movement != 'd'):
                movement = input("\nInvalid input, try again:\n")
            move_is_valid = move_valid(movement, maze, current_pos)
            if not move_is_valid:
                print("You cannot move that direction, try again.")
                movement = input("\nInput movement:\n")

        # if-elif chain which changes the maze arrays variables based on the player's direction of movement.
        # Would be neater if it worked as a function, but I'm not entirely sure how that would be possible.
        if movement == 'w':
            maze[current_pos[0] - 1][current_pos[1]] = '+'
            maze[current_pos[0]][current_pos[1]] = 'O'
            current_pos[0] -= 1
        elif movement == 'a':
            maze[current_pos[0]][current_pos[1] - 1] = '+'
            maze[current_pos[0]][current_pos[1]] = 'O'
            current_pos[1] -= 1
        elif movement == 's':
            maze[current_pos[0] + 1][current_pos[1]] = '+'
            maze[current_pos[0]][current_pos[1]] = 'O'
            current_pos[0] += 1
        elif movement == 'd':
            maze[current_pos[0]][current_pos[1] + 1] = '+'
            maze[current_pos[0]][current_pos[1]] = 'O'
            current_pos[1] += 1

    print("Congratulations, you've been reunited with your long lost plus sign shaped brother!\n\n"
          "This maze was drawn by Kaylynn Harris! We hope you enjoyed :)\n\n"
          "You will now be returned to module selection")
    main()


def requirement_filler():
    print("Welcome to the requirement filler\n"
          "the requirement filler utilizes code from my Sprint 1 project to fill out the list of required functions.")

    # Uses a while loop to find the factorial of a number the user is prompted for.
    factorial_number = int(input("What number would you like the factorial of?\n"))
    factorial_stable = factorial_number
    factorial_multiply = factorial_number - 1
    # Inputted number is decremented by one so the first operation in
    # the while loop yields the first step in the factorial.
    while factorial_multiply > 0:
        factorial_number *= factorial_multiply
        factorial_multiply -= 1
    print("The factorial of", factorial_stable, "is", factorial_number)

    # Simple division with an option to display the remainder or not.
    # Used geeksforgeeks.org to remember the 'end=' parameter.
    # Utilizes floor division to display with no remainder and the modulus function to display the remainder on its own.
    division_numerator = float(input("What number would you like to be divided?\n"))
    division_divisor = float(input("What number would you like to be divided by?\n"))
    remainder_selection = int(input("Would you like the remainder?\n1. Yes\n2. No\n"))
    if remainder_selection == 1:
        remainder_result = (division_numerator / division_divisor)
        print("The quotient is", remainder_result, "and the remainder is", (division_numerator % division_divisor),
              sep='-', end='\n')
    else:
        remainder_result = division_numerator // division_divisor
        print("The quotient is", remainder_result)

    interest_principle = float(input("What is your starting balance?\n"))
    interest_rate = (float(input(
        "What is the interest rate? (For a rate of 5.2% type 5.2)\n"))) / 100
    # The rate inputted is divided by 100 to get the percentage
    interest_period = int(input("How many times per year is interest applied?\n"))
    interest_years = float(input("How many years will you keep the money in the account?\n"))

    interest_final = interest_principle * ((1 + (interest_rate / interest_period)) ** (
            interest_period * interest_years))
    # Inputs are plugged into compound interest formula which utilizes exponents

    print("You initial investment of ", interest_principle, "will become %.2f" % interest_final, "after",
          interest_years, "years.")

    # Utilizes string multiplication to reflect emotional intensity
    emotion = input("How are you feeling emotionally?\n")
    emotion_intensity = 0
    while emotion_intensity < 1 or emotion_intensity > 1000:
        try:
            emotion_intensity = int(input("And from 1-1000, how intense is that emotion?\n"))
            if emotion_intensity < 1 or emotion_intensity > 1000:
                print("Your emotional intensity is outside of the specified range.")
        except ValueError:
            print("Invalid input, please try again\n\n")

    print("I see, so you're feeling\n", emotion * emotion_intensity, sep='')

    print("\n\n You have reached the end of the Requirement filler," + "you will now be returned to module selection.")
    main()


def main():
    print("\nHello and welcome to Jonathan Farkas' integration project!\n"
          "This iteration includes a maze module, along with a module which fulfills the rest of the project's "
          "requirements\n\n")
    module_selection = 0
    while module_selection != 1 and module_selection != 2:
        try:
            module_selection = int(
                input("Input the number for your desired module:\n1. Maze Game\n2. Requirement fillers\n\n"))
        except ValueError:
            print("Invalid input, please try again\n\n")
    if module_selection == 1:
        maze_game()
    if module_selection == 2:
        requirement_filler()


main()
