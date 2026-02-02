# 0 = empty, 'X' = full/obstacle, 'R', 'E' = Exit
import time as tm

maze = [
    ["R","X","0","0","X"],
    ["X","0","0","0","X"],
    ["0","X","0","E"]
]

coordinates_of_R = {
    "X" : {
        "Current_posX":"None"
    },

    "Y" : {
        "Current_posY":"None"
    }
}

store_0 = []
def logic_slow_detailed():
    """
    Find position of R in maze
    """
    global maze
    for list_num in range(len(maze)):
        for element in range(len(maze[list_num])):
            if maze[list_num][element] == "R":
                print(f"INITIAL POSITION BEFORE/AFTER SORT: {maze[list_num]} contains {maze[list_num][element]} at index {element}")
            elif maze[list_num][element]=="X":
                print(f"Hit a wall at index{element} in list {maze[list_num]}")
            #sort for blank spaces
            elif maze[list_num][element] != "X" and maze[list_num][element] != "R" and maze[list_num][element] != "E":
                maze[list_num][element] = "R" #new code
                #maze[list_num].remove(maze[list_num][element]) OLD CODE
                #maze[list_num].insert(element,"R") OLD CODE
                coordinates_of_R['X']['Current_posX'] = element
                coordinates_of_R['Y']['Current_posY'] = list_num
                store_0.append(maze[list_num][element])
                print(coordinates_of_R['X'],coordinates_of_R['Y'])
                print(maze[list_num])
            
                
                """
                Note: Why did this work?
                Notice, if we remove "maze[list_num].insert(element,"R")" and just leave "maze[list_num].remove(maze[list_num][element])"
                it will throw an index out of range, this, i guess because when you remove the '0's' then the index of them (element)
                dissapears or turns into another one, which leads to the 'out of range' error because you're trying to work with
                [list_num][element] despite element not existing. Whereas if you use 'insert' you just replace it like nothing happened.
                Basically you were stealing the index and it crashed, now you replace it/put it back but different

                Just changed the code from feedback , using 'remove' and 'insert' is messy,especially when iterating -
                therefore - we use reassignment by just doing maze[list_num][element] = "R" if the if-statement is true
                so remember that for future stuff
                """
            elif maze[list_num][element] == "E":
                print("ESCAPED!")
                break
    if "E" not in maze[list_num]:
       print("THERE IS NO ESCAPE TO BEGIN WITH WE ARE DOOMED")
         

        
           
    #If we put outside loop it only prints it till the end, if inside the first 'for' loop it'll print it after every sort/wall, if 
    #we print it inside the last loop it'll print it once for every element so its going to be a lot

#logic_slow_detailed()

# 0 = empty, 'X' = full/obstacle, 'R', 'E' = Exit
def logic_fast_satisfactory():
    global maze
    for list_num in range(len(maze)):
        for element in range(len(maze[list_num])):
            #if maze[list_num][element] == "R":
                #print(f"INITIAL POSITION BEFORE/AFTER SORT: {maze[list_num]} contains {maze[list_num][element]} at index {element}")
            #elif maze[list_num][element]=="X":
                #print(f"Hit a wall at index{element} in list {maze[list_num]}")
            #sort for blank spaces
            if maze[list_num][element] != "X" and maze[list_num][element] != "R" and maze[list_num][element] != "E":
                print(maze[list_num])
                tm.sleep(0.40)
                maze[list_num][element] = "R" #new code
                print(maze[list_num])
                tm.sleep(0.40)
                maze[list_num][element] = "0"
                #maze[list_num].remove(maze[list_num][element]) OLD CODE
                #maze[list_num].insert(element,"R") OLD CODE
                coordinates_of_R['X']['Current_posX'] = element
                coordinates_of_R['Y']['Current_posY'] = list_num
                store_0.append(maze[list_num][element])
                #print(coordinates_of_R['X'],coordinates_of_R['Y'])
                #print(maze[list_num])
            
                
                """
                Note: Why did this work?
                Notice, if we remove "maze[list_num].insert(element,"R")" and just leave "maze[list_num].remove(maze[list_num][element])"
                it will throw an index out of range, this, i guess because when you remove the '0's' then the index of them (element)
                dissapears or turns into another one, which leads to the 'out of range' error because you're trying to work with
                [list_num][element] despite element not existing. Whereas if you use 'insert' you just replace it like nothing happened.
                Basically you were stealing the index and it crashed, now you replace it/put it back but different

                Just changed the code from feedback , using 'remove' and 'insert' is messy,especially when iterating -
                therefore - we use reassignment by just doing maze[list_num][element] = "R" if the if-statement is true
                so remember that for future stuff
                """
            elif maze[list_num][element] == "E":
                print("ESCAPED!")
                break
    if "E" not in maze[list_num]:
       print("THERE IS NO ESCAPE TO BEGIN WITH WE ARE DOOMED")
         

        
           
    #If we put outside loop it only prints it till the end, if inside the first 'for' loop it'll print it after every sort/wall, if 
    #we print it inside the last loop it'll print it once for every element so its going to be a lot

logic_fast_satisfactory()

