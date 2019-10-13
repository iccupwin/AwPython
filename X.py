row = 1
col = 5
line = col
for i in range(1, line+1):
    for j in range(1, line+1):
        if row == i and col == j:
            print("<->", end="")
            row = row+1
            col = col-1
        elif i == j:
            print("<->", end = "")
        else:
            print(end = "   ")
    print() 
    