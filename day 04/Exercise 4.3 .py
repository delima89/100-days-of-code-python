
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Onde voce que esconde o tesouro? ")
local1=position[0]
local2=position[1]
map[int(local2)-1][int(local1)-1]="X"
print(f"{row1}\n{row2}\n{row3}")

