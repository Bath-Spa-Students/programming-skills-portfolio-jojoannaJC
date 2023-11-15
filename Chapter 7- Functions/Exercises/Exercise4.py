#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
#Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(message="'I love Python.'", size="Large "):
    """This is the size of the shirt made."""
    print("\nI am going to make a " + size + "shirt.")
    print("It will say, " + message)

make_shirt()
make_shirt(size="Medium")
make_shirt("Small", "Programming is cool.")