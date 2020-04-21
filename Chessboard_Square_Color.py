#determine the position
position=input("Enter the position:")
column=str(position[0])    
row=int(position[1])

#determine the colour
if column== "a" or column=="c" or column=="e" or column=="g" :
    if row%2==0:
        print("white")
    else:
        print("black")
else:
    if row%2==0:
        print("black")
    else:
        print("white")
