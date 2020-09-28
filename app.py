# ******************************************************
# ****** SECTION 1 - ABOUT CONDITIONAL STATEMENTS ******
# ******************************************************

# Conditional Statements
#   - Logical statements that tell your code to only do something IF a condition is true
#   - Usually takes the form: IF [condition] THEN [action]
#   - Conditions can be anything that is TRUE or FALSE (Boolean or a comparison using an operator)

# ********************************************
# ****** SECTION 2 - BASIC IF STATEMENT ******
# ********************************************

# Just some boolean variables to use as a demonstration
is_sky_blue = True
is_water_dry = False

# Basic if-statements using a boolean variable as the condition
if is_sky_blue:
    print("Correct, the sky is blue.")
if is_water_dry:
    print("Water is dry?")

# # Now using a comparison for the condition
# if 1 < 2:
#     print("1 is less than 2")
# if 1 > 2:
#     print("1 is greater than 2?")
# if "test" == "test":
#     print("These strings match")

# *****************************************
# ****** SECTION 3 - ELSE CONDITIONS ******
# *****************************************

# # The "else" statement occurs if the condition is false
# grade = 95
# if grade >= 70:
#     print("you passed")
# else:
#     print("you failed")
#
# # The elif (else if) condition is only checked if the first condition is false
# speed = 55
# if speed < 40:
#     print("Too slow")
# elif speed > 70:
#     print("Too fast")
# else:
#     print("Acceptable speed")

# *****************************
# ****** SECTION 4 - NOT ******
# *****************************

# # The exclamation point (!) or not can be used check that something is NOT true.
# a = 7
# b = 10
# if a != b:
#     print("These numbers are not equal.")
# else:
#     print("These numbers are equal")
#
# # Remember that is_water_dry was set to FALSE. So this condition is "not False" which is equal to "True".
# if not is_water_dry:
#     print("The 'not' forces a logical opposite. Water is NOT dry, therefore the condition is considered True.")

# **************************************
# ****** SECTION 5 - COMBINATIONS ******
# **************************************

# # The "and" requires that BOTH conditions be true in order for the action to occur
# am_hungry = True
# is_tuesday = False
# if am_hungry and is_tuesday:
#     print("Eat tacos.")
# else:
#     print("No tacos.")
#
# # The "or" will be true if EITHER condition is true
# is_tired = True
# is_nighttime = False
# if is_tired or is_nighttime:
#     print("I fell asleep.")
# else:
#     print("I am awake.")

# **********************************************
# ****** SECTION 6 - NESTED IF STATEMENTS ******
# **********************************************

# # Statements are "Nested" if they are inside of each other.
# # The inner statement will only be tested if the outer statement is true.
#
# # Notice the indentation matters!
# day_of_the_week = "Friday"
# if am_hungry:
#     if day_of_the_week == "Monday":
#         print("Eat a salad.")
#     elif day_of_the_week == "Tuesday":
#         print("Eat tacos.")
#     elif day_of_the_week == "Wednesday":
#         print("Eat chicken")
#     else:
#         print("Eat soup")
# else:
#     print("Eat nothing")

# ***********************************************
# ****** SECTION 6 - TERNARY IF STATEMENTS ******
# ***********************************************

# # Ternary if statements are a shorthand way to write conditions when the action is short.
# # [action] if [condition] else [alternate action]
#
# is_light_red = False
# print("Stop") if is_light_red else print("Go")
