import sys
import requests 
import json
import apis

def square(n):
    """ Square numbers  

    >>> square(2)
    4
    >>> square(3)
    9
    >>> square(2.0)
    4.0
    >>> square(0)
    0
    >>> square(30)
    900
    """
    return n*n

def dispatcher(command, arg):
    """ Does things 
    >>> dispatcher("weather", "berkeley")
    Here's the weather forcast for berkeley

    >>> dispatcher("square", 2)
    The square of 2 is 4

    >>> dispatcher("go away", 3)
    It sounds like you no longer need my assistance
    Very well. Goodbye!

    """
    if command == "weather":
        print("Here's the weather forcast for "+arg)
        print(apis.fetch_weather(arg))
    if command == "square":
        print("The square of " + arg + " is " + str(square(int(arg))))
    elif command == "go away":
        print("It sounds like you no longer need my assistance")
        print("Very well. Goodbye!")
        return 
    elif command == "bye":
        print("Goodbye! Have a good day!")
        return
    # Reprompt the user. 
    prompter()


def prompter():
    """ asks for things """

    command = (input("How may I help you?: [weather, square, go away, bye]")).lower()
    if command == "weather":
        city = input("Sure thing! What city?")
        dispatcher(command, city)
    if command == "square":
        num = input("I love math! What number?")
        dispatcher(command, num)
    elif command == "stocks": # TODO
        print(apis.fetch_stocks(2))
    else:
        dispatcher(command, "")

def starter(cliargs):
    # TODO: Finish up command line interface
    print("DEBUG: Called with ", cliargs[1:])

    print("Summoning Jarvis")
    print("Good evening!")

    if (len(cliargs) > 1):
        command = cliargs[1]
        arg = cliargs[2]
        # TODO: Call dispatcher with args instead of prompting user. 
        dispatcher(command, arg)
    else:
        prompter()

#this is a comment
def dance():
    """Every personal assistant should know how to dance!"""
    print("left right chachacha left right chacha\n left left right right dip up chachacha")
    return

if __name__ == "__main__":
    starter(sys.argv)
