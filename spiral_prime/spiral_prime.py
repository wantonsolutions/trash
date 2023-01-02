import sympy
import sys

def gen_array(size=5):
    val=[None] * size
    for i in range(len(val)):
        val[i] = [None] * size
    return val

def find_center(arr):
    x=len(arr)
    if x > 0:
        y=len(arr[0])
    else:
        return(-1,-1)
    return (int(x/2), int(y/2))

next = {
    "right" : "up",
    "up": "left",
    "left" : "down",
    "down" : "right",
}

def next_position(position,direction):
    if direction == "right":
        position = (position[0]+1,position[1])
    elif direction == "up":
        position = (position[0],position[1]+1)
    elif direction == "left":
        position = (position[0]-1,position[1])
    elif direction == "down":
        position = (position[0],position[1]-1)
    else:
        position = (-1,-1)
    return position

def next_direction(position,arr,direction):
    x=position[0]
    y=position[1]
    go_next=False
    if direction == "right" and arr[x][y+1]==None:
        go_next=True
    elif direction == "up" and arr[x-1][y]==None:
        go_next=True
    elif direction == "left" and arr[x][y-1]==None:
        go_next=True
    elif direction == "down" and arr[x+1][y]==None:
        go_next=True
    
    if go_next:
        return next[direction]
    else:
        return direction

def invalid_position(position, arr):
    if position[0] < 0 or position[1] < 0:
        return True
    if position[0] >= len(arr) or position[1] >= len(arr):
        return True
    return False
            

def spiral(arr):
    position = find_center(arr)
    move = True
    direction = "down"
    value = 1
    while move:
        #mark
        arr[position[0]][position[1]] = value
        direction=next_direction(position,arr,direction)
        if value == 1:
            direction = "up"
        position = next_position(position,direction)
        if(invalid_position(position,arr)):
            break
        value = value+1
    return arr

def print_spiral(arr):
    #color = '\033[93m'
    color = '\033[91m'
    color2 = '\033[23m'
    endcolor = '\033[0m'
    symbol = '😀'
    # outside = '['
    # inside = ']'
    outside = ''
    inside = ''
    for val in arr:
        for index in val:
            if index == None:
                print(" ", end=" ")
            else:
                if sympy.isprime(index):
                    print(outside + color + symbol + endcolor + inside, end=" ")
                    #print(str(outside + color + "%2d" + endcolor + inside) % index, end=" ")
                else:
                    print(outside + " " + inside, end=" ")
                    #print(str(outside + color2 + "%2d" + endcolor + inside) % index, end=" ")
        print()

            





print("generating a prime spiral https://mathworld.wolfram.com/PrimeSpiral.html")
print("add an integer argument if you want a bigger spiral -- python spiral_prime.py 25")

size = 10

try:
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
except:
    print("using default size of ten, supply a proper integer")


val = gen_array(size)
print(find_center(val))
val = spiral(val)
print_spiral(val)


