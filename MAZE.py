import os
import readchar
import random
POS_X = 0
POS_Y = 1
NUM_OF_MAP_OBJECTS = 11
my_position = [6,3]
tai_length = 0
tail = []
map_objects = []
game_end = False
died = False
obstacle_definition = """\
#### ###################
####           ######## 
 #####                  
  ####     ###########   
#  ###        #####     
##  ###     #  ######  # 
###  ##                 
####            ########             
#####                   
##     #####   ######  # 
 #   #                   
    ####################
 #           #######      
   ##    ###  #####     
  ##                    \
"""
""""
#my solution
c=0
while c>=0 and c<10 :
    map_objects.append([random.randint(0, MAP_WIDTH-1),random.randint(0, MAP_HEIGHT-1)])
    c+=1
"""
#create obstacle map
obstacle_definition = [list(row)for row in obstacle_definition.split("\n")]
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)
#main loop
while game_end == False:
    os.system("cls")
    # generate random objects on the map
    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_position = [random.randint(0, MAP_WIDTH-1), random.randint(0, MAP_HEIGHT-1)]
        if new_position not in map_objects and new_position != my_position and \
                obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            map_objects.append(new_position)
    #Draw map
    print("+"+"-"*(MAP_WIDTH*2)+"+")
    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for cordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "
            object_in_cell = None
            tail_in_cell = None
            for map_object in map_objects:
                if map_object[POS_X] == cordinate_x and map_object[POS_Y] == cordinate_y:
                    char_to_draw = " *"
                    object_in_cell = map_object
            for tail_piece in tail:
                if tail_piece[POS_X] == cordinate_x and tail_piece[POS_Y] == cordinate_y:
                    char_to_draw = " @"
                    tail_in_cell = tail_piece
            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = " @"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tai_length += 1
                if tail_in_cell:
                    game_end = True
                    died = True
            if obstacle_definition[cordinate_y][cordinate_x] == "#":
                char_to_draw = "##"
            print("{}".format(char_to_draw),end="")
        print("|")
    print("+"+"-"*(MAP_WIDTH*2)+"+")
    # Ask user where he wants to move
    #direction = input("donde te quieres mover [WASD]: ")
    direction = readchar.readchar()
    if direction == "w":
        new_position = [my_position[POS_X],(my_position[POS_Y]-1)%MAP_WIDTH]
    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y]+1)%MAP_WIDTH]
    elif direction == "a":
        new_position = [(my_position[POS_X]-1)%MAP_WIDTH, my_position[POS_Y]]
    elif direction == "d":
        new_position = [(my_position[POS_X]+1)%MAP_WIDTH, my_position[POS_Y]]
    elif direction == "q":
        game_end = True
    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tai_length]
            my_position = new_position
if died == True :
    print("has muerto")