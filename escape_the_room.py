from dataclasses import dataclass
from enum import auto

from enum import Enum
import sys


@dataclass
class room(Enum):
    """
    This has all the rooms for this game. Each room has 6 attributes, s, n, e, w, hint and picture.
    """
    foodcourt = {
        "s": "outcropping",
        "n": "wall",
        "e": "wall",
        "w": "flyingpotion",
        "hint": "You are in a wide food court. You glance at the clock. It reads quarter past nine. South of you, light shines through an open doorway. To the west, a wooden door is closed.\n Type (n/s/e/w) to move.",
        "picture": """
        ######################################################            
        #                                                    #      N
        #                       Food Court                   #    W + E
        #                                                    #      S
        ######                                               #
        #    #                 ######                        #
        #door#                 #door#                        #
        #    #                 #    #                        #
        ######################################################
        """,
    }
    outcropping = {
        "s": "wall",
        "n": "foodcourt",
        "e": "wall",
        "w": "wall",
        "hint": "There is an island far away to the south. The ship is not here. Go back, as there is literally nothing on the island.\n An open doorway leads to the north.",
        "picture": """
        ######################################################
        #                                                    #
        #                        Outcropping                #
        #                  #                                #
        #                 # ##                             #
         #               #   ##        ##                 #  
          #             #      #     # #    #       #      #                        ######
           #           #        #   #   #  ##     # #    #                          #     #
            ###########         #####    ### #####  #####                           #Island#
                        Ocean                                                       #########
            """,
    }
    flyingpotion = {
        "s": "goodwitch",
        "n": "wall",
        "w": "wall",
        "e": "foodcourt",
        "hint": "You come to a luxurious living room, where you see a beaker with yellowish liquid inside on the carpet. Type 'drink' to drink it. An archway leads to the south, and an open doorway is in the east.",
        "picture":"""
        ###################################################
        #                                                 #         N
        #             Living Room                         #       W + E
        #                                         #########         S
        #                                         # door  #
        #                  ######                 #########
        #                  #door#                         #
        #                  #    #                         #
        ###################################################
        """
    }
    goodwitch = {
        "s": "ship",
        "n": "flyingpotion",
        "e": "zombieroom",
        "w": "wall",
        "hint": "You are now in a room with a low ceiling. A figure hovers over you. You need to run away. Type 'e' or 's' to scram. Quick! It is coming...",
        "picture":"""
        
        
        
        
        
        
        
        
        
        """
    }


print(
    "You roll around on the floor, waiting for the fire to come to you, but... nothing comes. You open your eyes."
)

current_room = room.foodcourt
while True:
    print(
        "Welcome to Escaping Time 1.0. \n You can move in 4 directions, North(n), South(s), East(e) and West(w). \n Press d to start playing"
    )
    user_input = input(">")
    if user_input == "d":
        print(current_room.value["hint"])
        print(current_room.value["picture"])
        while True:
            user_input = input(">")
            if (
                user_input != "s"
                and user_input != "n"
                and user_input != "w"
                and user_input != "e"
            ):
                print("I don't know '" + str(user_input) + "'. Type (n/s/e/w) to move")
            else:
                next_room = current_room.value[user_input]
                print(next_room)
                if next_room == "wall":
                    print("There is a wall here. Type (n/s/e/w) to move")
                elif next_room == "zombieroom":
                    print(
                        "You got eaten by zombies. Try again in the next life (which is likely to be very soon). You lost."
                    )
                    sys.exit()
                elif next_room == "ship":
                    print(
                        "Congratulations! You found the ship and now you have escaped the mansion. You WON."
                    )
                    sys.exit()
                else:
                    current_room = room[next_room]
                    print("You come to  " + next_room + ". ")
                    print(current_room.value["hint"])
                    print(current_room.value["picture"])
    else:
        print("I don't know what you're saying. Read instructions carefully")
