# -*- coding: utf-8 -*-

#random is imported to give initial value of starting room.
import random

#maze stores the possible conections to a room

maze = {
        'A' : ['B', 'F'],
        'B' : ['A', 'E'],
        'C' : ['D', 'F'],
        'D' : ['C'],
        'E' : ['B', 'F'],
        'F' : ['A', 'C', 'E']
}

#description stores the descriptions for each room

description = {
        'A' : "Room A is bedroom 1",
        'B' : "Room B is restroom",
        'C' : "Room C is kitchen",
        'D' : "Room D is drawing room",
        'E' : "Room E is bedroom 2",
        'F' : "Room F is verandah"
}

#rRoomNumber returns the choice corresponding to the rooms
#useful when accessing them from a list, as we get the list
#indices

def RoomNumber(n):
    if n==1:
        return 'A'
    elif n==2:
        return 'B'
    elif n==3:
        return 'C'
    elif n==4:
        return 'D'
    elif n==5:
        return 'E'
    elif n==6:
        return 'F'

#Room Desc gives the description o the room you are in

def RoomDesc(n):
    print("\nWelcome to Room " + n)
    print(description[n])

#main function: this function helps us traverse through 
#the maze. it runs
#a while loop and the user continues to input choices.
#wrong input gives a promptshowing no path exists.
            
def main():
    print("Hello, Welcome to the house of creep")

    start = random.choice([1,2,3,4,5,6])

    print("We will start our journery from Room No : ",\
          RoomNumber(start),"\n")

    choice = 1
    s = RoomNumber(start)
    
    while(choice ==True):
        print("\nExisting Paths:", " ".join(maze[s]))
        my_list = maze[s]

        #copy stores a copy of the varible in case of wrong choices

        copy = s                               
        s = input("Where do you want to go next ")

        if s in my_list:
            RoomDesc(s)
        else:
            print("Wrong Choice")

            #we assign s to copy in case of wrong path so that
            #we know where we are in case of wrong choice.
            #if we do not do this s gets updated in next loop run
            #and we lose track of where we were previously.

            s=copy
       
        choice = int(input("Continue our Journey ?(0/1) "))
        if choice==0:
            break
       
        
if __name__ == main():
    main()
    

