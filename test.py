
def nameoffunction():
    print("Hi there")
    print("Welcome to functions practice!")
    # Add two line brakes
    #  add two line breaks

    nameoffunction()

# How to pass something to a function
# - We add paramaters to these functions
# - We fill these paramaters later with arguments example below

def names_and_last_names(first_name, last_name):  # Basically def is defininf the name of the function and assinging it (two variables)
    print(f'Hey {first_name} {last_name}!')
    print('What is up?')


names_and_last_names('James', 'Deane')
names_and_last_names('Jane', 'Doe')

# Two types of functions:
# 1- perform a task : The first function above
# 2- return a value : Example below

def get_greeting(name): # This one simply returns a value
    return f'Hi {name}'

message  = get_greeting('Jane')
file = open('content.txt', 'w')  # Write it to a file
file.write(message)

# message = get_greeting(input('What is your name?: '))
# print(message)

# FUNCTIONS THAT RETURN SOMETHING









