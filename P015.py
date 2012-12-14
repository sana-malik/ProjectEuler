from math import factorial

def num_tracks(x, y):
    if x==1 or y==1:
        return x+y
    return num_tracks(x-1,y) + num_tracks(x, y-1)

def permutations(x,y):
    # do (x+y) choose x
    return factorial(x+y)/(factorial(x)*factorial(y))
     
print permutations(20,20)