#MovieGuidePart2 Made by Alon Rehin for CIS 261


def movies():

    List = [] #["Indiana Jones and the Dial of Destiny", "Star Wars: The Rise of Skywalker (Episode IX)", "The Lord of the Rings: The War of the Rohirrim"]

    with open("Movies.txt") as source:
        for movie in source:
            movie = movie.replace("\n","")
            List.append(movie)
    return List

def intro():

    #Guide = print("Movie Guide \n\n\nCOMMANDS: \nlist - List all movies\nadd - Add a movie\ndel - Delete a movie\nexit - Exit the program")
    print("Movie Guide \n\n\n")
    print("COMMANDS: \n")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit the program")


def display(List):
    Number = 0

    for movie in List:
        Number += 1
        print(str(Number) + ".",movie)

    return Number
  

def delete(List,Number):

    DelInput = input("\nWhich movie number you want to delete? ")

    if DelInput.isdigit() == False:
        print("\nPlease type in a number")

    elif int(DelInput) < 1 or int(DelInput) > Number:
        print("\nNot found in list")

    else:
            DelInput = int(DelInput) - 1
            List.pop(DelInput)
            print("\nDeleted\n")
            display(List)
    return List


        
def add(List):

    AddInput = input("\nWhich movie you want to add? ")

    List.append(AddInput)
    print("\nMovie added!")
    display(List)

    return List


intro()

List=movies()

Command = input("\nWhat do you want to do? ")

while Command.lower() != "exit":


    if Command.lower() == "list":
        print("\nYour list:\n")
        display(List)
        Command = input("\nWhat do you want to do? ")

    elif Command.lower() == "del":
        Number=display(List)
        delete(List,Number)
        Command = input("\nWhat do you want to do? ")

    elif Command.lower() == "add":
        add(List)
        Command = input("\nWhat do you want to do? ")

    else:
        print("Invalid input\n")
        intro()
        Command = input("\nWhat do you want to do? ")

print("\nGoodbye!\n")


