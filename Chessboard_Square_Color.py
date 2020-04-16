#determine the position
position=input("Enter the position:")
column=str(position[0])    
row=int(position[1])

#determine the colour
if column== ("a" or "c" or "e" or "g") and (row%2!=0) :
    print("black")
else:
    print("white")
