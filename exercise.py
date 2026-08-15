row1=['☠️','☠️','☠️']
row2=['☠️','☠️','☠️']
row3=['☠️','☠️','☠️']
print(f"{row1}\n{row2}\n{row3}")
matrix=[row1,row2,row3]
position=input("enter the position where you want to hide the money")
row_number=int(position[0])
coloum_number=int(position[1])
row_selected=matrix[row_number-1]
row_selected[coloum_number-1]='x'
print(f"{row1}\n{row2}\n{row3}")