def unique(el):
    if len(set(el)) == len(el):
        return True
    else:
        return False
    
two_dimension = [list(map(int, input().split())) for _ in range(9)]
for el in two_dimension:
    print(unique(el))
