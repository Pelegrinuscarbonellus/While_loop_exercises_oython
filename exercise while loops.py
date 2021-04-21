# 7-4. Pizza toppings:

pizza_toppings = "the pizza toppings are: tomatoes, onions, pinneaple, anchovies, mozarella"
pizza_toppings += "I will let you know the toppings that ara available above"
pizza_toppings += "as a client you can enter 'quit' to end this program"

message = ""  # we create a variable called message which is empty: ""
while message != 'quit':  # we create a while loop here which says: that while message != is not quit
    message = input(pizza_toppings)

    if message != 'quit':
        print(message)


# 7-5. movie tickets:

age = "How old are you kid"
age += "Please press enter if you would like to 'quit' the program please"

while True:  # this means: if statement is True
    age = input(age) # we enter age = ti input
    if age == 12:
        break
    age = int(age)

    if age < 3:
        print("you got a free ticket!")


    elif age < 13:
        print(f"this ticket will cost you 10 dollars!")

    else:
        print("the ticket will cost you 15 dollars")

# 7-6. three exits

# 1. pizza toppings modified:

pizza_toppings = "the pizza toppings are: tomatoes, onions, pinneaple, anchovies, mozarella"
pizza_toppings += "I will let you know the toppings that ara available above"
pizza_toppings += "as a client you can enter 'quit' to end this program"

active = True

while active:
    message = input(pizza_toppings)
    if message == 'quit':
       active = False
    else:

        print(message)

print("")
pizza_toppings = "the pizza toppings are: tomatoes, onions, pinneaple, anchovies, mozarella"
pizza_toppings += "I will let you know the toppings that ara available above"
pizza_toppings += "as a client you can enter 'quit' to end this program"

active = True

while active:
    message = input(pizza_toppings)

    if message == 'quit':
        active = False

    else:
        print(message)




# This program below seems to work!

guitars_rock = "there are a few guitars available, one of them is broken"
guitars_rock += "one of these guitars will be repaired unless you state that you want"
guitars_rock += "to 'quit' this program and automatically will exit the program!"

active = True

while active:
    message = input(guitars_rock)
    if message == 'none':
        active = False
    else:
        print(message)


# 7-7. endless loop!

z = 500
while z == 500:
    print(z)
if z >= 400:
    print(f"loop becomes endless {z}")

    z += 5000





# repetition of exercise tickets number: structure

porn_tickets = "there are only a number of tickets that are available:"
porn_tickets = "you can enter 'quit' if you want to exit the program please"

while True:
    age = input(porn_tickets)

    if age == 13:
        break

    if age < 3:
        print("the porn ticket is free boy!")

    elif age < 13:
        print(f"the porn ticket will be 10 dollars boy!")

    else:
        (f"the porn ticket will be 15 dollars ")







# funfair tickets:

funfair_tickets_age = "These are the funfair tickets:"
funfair_tickets_age += "In order to qualify you must meet an age criteria"

while True:
    age = input(funfair_tickets_age)

    if age == 18:
        break

    if age < 3:
        print(f"the ticket will be free as your age is 3")

    elif age < 13:
        print(f"the ticket will be 1o dollars boy!")

    else:
        print(f"Your ticket will be 15 dollars boy!")


 # example of an infinite loop in python
z = 500
while z == 500:
    print(z)
if z >= 400:
    print(f"loop becomes endless {z}")

    z += 5000