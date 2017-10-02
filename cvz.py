import sys
import math

# Save humans, destroy zombies!
debug = True
x_target = ""
y_target = ""
mindist = 50000

def calcul_distance(x,y, x2,y2):
    return (abs((x+x2)/2+(y+y2)/2))
# game loop
while True:
    x, y = [int(i) for i in input().split()]
    human_count = int(input())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        x_target = str(human_x)
        y_target = str(human_y)
        tmpdistance = calcul_distance(x,y,human_x,human_y) 
        if mindist < tmpdistance:
            mindist = tmpdistance
            x_target = str(human_x)
            y_target = str(human_y)
        if debug:
            print("human "+str(human_id)+" : "+str(human_x)+ " - "+str(human_y), file=sys.stderr)
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        if debug:
            print("Zombi", file=sys.stderr)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # Your destination coordinates
    print(x_target+" "+y_target)
