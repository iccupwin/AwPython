def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == i:
        print ("Move disk 1 from rod",from_rod, "to rod", to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print ("Move disk", n, "from_rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    
n = 4
TowerOfHanoi (5, \'A\', \'B\', \'C\')