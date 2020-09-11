from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue
import random 

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#a way to translate the reverse path
def reverse_direction(direction):
    if direction == 's':
        return 'n'
    elif direction == 'n':
        return 's'
    elif direction == 'e':
        return 'w'
    elif direction == 'w':
        return 'e'

def traverse_all_rooms(starting_room):
    #keep track of path
    moves = Stack()
    
    visited_rooms = set()
    #make a starting point
    starting_room = player.current_room

    #continue until all rooms are visited
    while len(visited_rooms) < len(room_graph):
        #tracks the available travel directions for the current room
        available_directions = []

        #add current room to visited rooms
        visited_rooms.add(player.current_room)

        #get the exits for the current room
        exits = player.current_room.get_exits()

        for exit in exits:
            #if there is an exit
            if exit is not None:
                if player.current_room.get_room_in_direction(exit) not in visited_rooms:
                    #add exit to available directions
                    available_directions.append(exit)
                    # print('options', available_directions)


        #if there is an available direction in list
        if len(available_directions) > 0:
            #choose a random direction
            random_index = random.randint(0, len(available_directions) - 1)
            #add move to traversal_path
            traversal_path.append(available_directions[random_index])
            #add direction to stack
            moves.push(available_directions[random_index])
            #move the player
            player.travel(available_directions[random_index])
        
        #there are no more available directions
        else:
            last_move = moves.pop()
            traversal_path.append(reverse_direction(last_move))
            player.travel(reverse_direction(last_move))
traverse_all_rooms(0)

### Not using for revised solution ###
# def add_to_maze(room):
#     #make each room a key and each value a dictionary that holds the directions
#     maze[room.id] = {}

#     #use the get_exits from the room class
#     exits = room.get_exits()

#     #take each direction that is returned from get_exits
#     for direction in exits:
#         #make each exit a key and set the value to '?'
#             #the '?' will get replaced by another direction as paths get explored
#         maze[room.id][direction] = '?'
#     return maze

# print(add_to_maze(player.current_room))


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
