import numbers
# CALCULATOR CHALLENGE
# The goal of this challenge is to make a basic console based calculator that can add, subtract, multiply, and divide.
# I have written in a few useful lines of code for you and added pseudo-code to guide you.
# Fill in the contents to make this calculator work
# Feel free to edit existing code or change the overall structure to make the user experience more friendly

# The "while loop" below will force the console to keep asking for commands until "is_running" becomes false


is_running = True
while is_running:

    # Ask the user which mathematical process they want to do. Or allow them to input a command to quit the program.
    # Make the prompts user friendly. Your users will not know what their options are unless you tell them.
    user_command = input("command?")

    # Ask the user for the numbers that will be added, subtracted, etc.
    # Again, try to make it user friendly
    # Notice that I am automatically converting their input into a "float". This can cause errors if
    # they do a non-number input. In the future we will learn how to handle errors.
    first_number = float(input("number?"))
    second_number = float(input("number?"))

    # Perform the appropriate mathematical operation that matches their command

    # Handle the case when the user inputs

    # Display the result to user

    # Make it so that the program closes when an appropriate command is given
    # Hint: When "is_running" becomes False the program will be allowed to end
