#Replacing X in the place of index of Matrix by user (11,12,13,21,22,23,31,32,33)

row1 = [1,2,3]
row2 = [4,5,6]
row3 = [7,8,9]
matrix=[row1,row2,row3]
print(f" {row1}\n {row2}\n {row3}")
place=input("Enter the number where you need to store your money: ")
row=int(place[0]) -1 
column=int(place[1]) -1
rows=matrix[row]
rows[column]='X'
print(f" {row1}\n {row2}\n {row3}")
