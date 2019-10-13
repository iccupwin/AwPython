import itertools
for i in itertools.product(["T", "H"], repeat=3):
    print(i)

for i in itertools.product([0,1], repeat=3):
    print(i, '|', ''.join(str(j) for j in i))