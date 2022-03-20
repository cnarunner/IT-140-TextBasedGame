# Bryce Jensen
# IT-140 Project 2

import time

# The very long dictionary I needed to drive all the code. Yes. I know I went overboard.
rooms = {
    'bedroom': {
        'name': 'The Bedroom',
        'direct': 'There are doors to the North and West.',
        'north': 'closet',
        'west': 'living',
        'contents': ['ipad'],
        'text': 'You always loved this floral wallpaper, although it \nis peeling a bit around the edges.',
    },
    'closet': {
        'name': 'Bedroom Closet',
        'direct': 'There is one door to the South.',
        'south': 'bedroom',
        'contents': ['medical gloves'],
        'text': 'Smells like old socks...and mothballs',
    },
    'living': {
        'name': 'The Living Room',
        "direct": "There are doors in all directions, but you shouldn't \ngo West till you're ready for the grandkids.",
        'north': 'kitchen',
        'south': 'basement',
        'east': 'bedroom',
        'west': 'frontdoor',
        'contents': ['masks'],
        'text': 'There is a couch and a coffee table in the corner, to the west is the Front Door. \n',
    },
    'basement': {
        'name': 'The Basement',
        'direct': 'There are doors to the North and East.',
        'north': 'living',
        'east': 'garage',
        'contents': ['tv remote'],
        'text': "Brr...you don't keep the heat on down here because \nno one ever comes down anymore.",
    },
    'garage': {
        'name': 'The Garage',
        'direct': 'There is only one door to the West.',
        'west': 'basement',
        'contents': ['toilet paper'],
        'text': 'At the beginning of the pandemic, your kids brought \nyou some of the hoard of toilet paper they bought. Now \nyou have your own personal hoard.',
    },
    'kitchen': {
        'name': 'The Kitchen',
        'direct': 'There are doors to the South and East.',
        'south': 'living',
        'east': 'bathroom',
        'contents': [],
        'text': 'This kitchen used to get used far more often, when \nfamily gatherings were a thing. Now all it makes are \nTV Dinners in the microwave.',
    },
    'bathroom': {
        'name': 'The Bathroom',
        'direct': 'There is only one door to the West.',
        'west': 'kitchen',
        'contents': ['hand sanitizer'],
        'text': 'Everything is pink...such a pretty color for a bathroom.'
    },
    'frontdoor': {
        'name': 'The Front Door',
        'direct': 'There is only one way to go, East.',
        'west': 'living',
        'contents': [],
        'text': 'The grandkids are on the other side of the door. Are you ready to let them in?',
    }}

# objects I needed made before being in the loop
avail_directions = ['north', 'south', 'east', 'west']
current_room = rooms['bedroom']
carrying_items = []

# I didn't like everything popping up all at once so I found a way to make it slow down
# the function is me being lazy so I didn't have to type a time.sleep() ~30 times
def wait(seconds):
    time.sleep(seconds)

# displays what items are in the room to collect
def display_item():
    print('\nIn the room: {}. \nEnter "collect" to collect the item'.format(current_room['contents'][0],))

# displays what you are carrying
def carry_items():
    print('You are carrying:', end='')
    for item in carrying_items:
        if item is carrying_items[-1]:
            print(item)
        else:
            print(item, end=', ')
    print('\nYou are carrying {}/6 items.'.format(len(carrying_items)))


# the information that could be useful before each user input
def quick_gen_commands():
    print('_____________________________________________')
    print('You are in:', current_room['name'], end='\n')
    wait(1)
    print(current_room['text'], end='\n')
    wait(2)

    # display items you are carrying
    print()
    carry_items()
    wait(2)

    # displaying room item
    if len(current_room['contents']) >= 1:
        display_item()
    elif len(current_room['contents']) == 0:
        print('\nThere is nothing in the room.')
    wait(2)

    print('\nEnter "north", "south", "east", or "west" \nor enter "?" to see where you can go.\n')

# end of game
def front_door():
    print()
    print('You are at:', current_room['name'], end='\n')
    print(current_room['text'], end='\n')
    wait(4)
    print('YES')
    wait(2)
    print('You open the door.')
    wait(2)
    print('"HI GRANDMA!!!!"')
    wait(2)
    print('"Hello!"')
    wait(1)
    print('"Remember to be safe you three," as you hand masks, hand sanitizer, \nand gloves to them, "we wouldn\'t want anyone getting sick!')
    wait(6)
    print('You smile as they run past you to explore the house they haven\'t seen in so long. \n')
    wait(5)
    print(input('\n\n"Enter" to end game.'))
    quit()

# STORYLINE
def storyline():
    print('*ring* *ring*')
    wait(2)
    print('*ring* *ring*')
    wait(2)
    print('*ring*')
    wait(0.5)
    print('You pick up your baby blue rotary phone off of your nightstand.')
    wait(3)
    print('\n"Hello?"')
    wait(2)
    print('\n"Hi Mom, I\'ll be there with the kids in about 5 minutes."')
    wait(3)
    print('\n"Okay! It will be good to see my grandkids. \nIt has been too long because of this darned pandemic."')
    wait(4)
    print('\nYou hang up the phone.')
    wait(2)
    print('\nIt is time to collect all your pandemic necessities \nso the grandkids don\'t get you sick!')
    wait(2)
    print('\n*sigh* Moving around causes your bones to creak and groan, \n but you\'re pushed forward by your excitement to see your grandkids again.\n' )
    print(input('"Enter" to continue'))



# ! GAME START
print('Enter "exit" at any time to leave the game.')
wait(2)

# calls the first functions to get the game started
storyline()
print()

# an Infinite loop unless the user tells it to quit or the end of the game is reached
while True:

    # keeping user away from front door till all items are collected
    if current_room == rooms['frontdoor']:
        if len(carrying_items) == 6:
            front_door()
        elif len(carrying_items) < 6:
            print("You don't have enough items to let them in yet!")
            wait(2)
            current_room = rooms['living']
        continue

    quick_gen_commands()
    user_input = input('\nEnter your command:\n').lower()
    # figuring out where to go
    if user_input == '?':
        print(current_room['direct'], end='\n')
        wait(3)

    # moving around rooms
    elif user_input in avail_directions:
        if user_input in current_room:
            current_room = rooms[current_room[user_input]]

        # if user goes somewhere unavailable
        else:
            print('There is a wall there!\n')

    # collecting items
    elif user_input == 'collect':
        item = current_room['contents'][0]

        if item in current_room['contents']:
            current_room['contents'].remove(item)
            carrying_items.append(item)
            print('\nYou collected an item!')

        elif len(current_room['contents']) == 0:
            print('There isn\'t anything to collect!')

    # leave the game
    elif user_input == 'exit':
        print('Goodbye!\n')
        print(input('\n"Enter" to end game.'))
        quit()

    # invalid input
    else:
        print('\n***That is not a valid command.***\n')
