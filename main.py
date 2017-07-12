#Import files from another files
import spy_details
from steganography.steganography import Steganography
from datetime import datetime

#Made a list of having of having the old status messages
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']



#definition of the function add_status which update the status of the spy
def add_status():

    updated_status_message = None
    #Here condition checked wheather the current_status_update is none or not
    if spy_details.spy.current_status_message != None:

        print 'Your current status message is %s \n' % (spy_details.spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'
    #Get the choice from the spy if they want to add status from older status , press y otherwise n
    default = raw_input("Do you want to select from the older status (y/n)? ")

    #If Condition check
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")

        #If condition check under the uper if block
        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message
    #If first conditon not satisfied then elif block executed
    elif default.upper() == 'Y':

        #Initialization of for loop
        item_position = 1

        for message in STATUS_MESSAGES:
            #Print the older status messages....
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        #Get the choice from  the spy for status update
        message_selection = int(raw_input("\nChoose from the above messages "))


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message

#Add a friend for chat
def add_friend():

    new_friend = spy_details.Spy('', '', 0, 0.0)
    #
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    #coverting the string type into the int type
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    #converting the string type into float type
    new_friend.rating = float(new_friend.rating)
    # If condition check and execute when satisfied
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy_details.spy.rating:
        spy_details.friends.append(new_friend)
        print 'Friend Added!'
    #If condition not satisfied execute else block
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(spy_details.friends)

#Select the friend for chat
def select_a_friend():
    item_number = 0

    for friend in spy_details.friends:
        #Prints the list of all the friends
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")
    #covert the type of friend_choice from string to int
    friend_choice_position = int(friend_choice) - 1

    #Return thefriends position
    return friend_choice_position

#Send the secret message
def send_message():

    friend_choice = select_a_friend()

    #Input the name of the image
    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"

    #Type the message which you want to send
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = spy_details.ChatMessage(text, True)

    spy_details.friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"

#Read the secret message
def read_message():

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)
    print secret_text

    new_chat = spy_details.ChatMessage(secret_text, False)

    spy_details.friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"

#Read the entire chat with the spy
def read_chat_history():

    read_for = select_a_friend()

    print '\n6'
   # loop for reading chats along with their time
    for chat in spy_details.friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), spy_details.friends[read_for].name, chat.message)

#Funtion gets the detail of the spy who wants to join the application
def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name


    if spy.age > 12 and spy.age < 50:


        print "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        if float(spy.rating)>4.5:
            print 'You are awesome.'
        elif float(spy.rating)>3.5:
            print 'You are among of good ones.'
        elif float(spy.rating)>2.5:
            print 'You are average.'
        else:
            print 'Not specified'


        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'

#Here we started from the code
print "Hello! Let\'s get started"

question = "Do you want to continue as " + spy_details.spy.salutation + " " + spy_details.spy.name + " (Y/N)? "
existing = raw_input(question)
if existing.upper() == "Y":
    start_chat(spy_details.spy)
else:

    spy = spy_details.Spy('', '', 0, 0.0)


    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print 'Please add a valid spy name'