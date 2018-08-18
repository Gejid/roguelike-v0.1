import sys
import os
import msvcrt
playercords = [0, 0]
def Update():
    for a in range(20):
        for b in range(20):
            if(playercords == [a, b]):
                sys.stdout.write("A")
            else:
                sys.stdout.write("#")
        print("")
msg = "ROGUELIKE v0.1"
while True:
    Update()
    print("MESSAGE: " + msg)
    wtd = msvcrt.getch().decode("utf-8").lower()
    if(wtd == "w"):
        if(playercords[0] == 0):
            msg = "REACHED BORDER"
        else:
            playercords[0] -= 1
            msg = "MOVED UP"
    if(wtd == "s"):
        if(playercords[0] == 19):
            msg = "REACHED BORDER"
        else:
            playercords[0] += 1
            msg = "MOVED DOWN"
    if(wtd == "a"):
        if(playercords[1] == 0):
            msg = "REACHED BORDER"
        else:
            playercords[1] -= 1
            msg = "MOVED LEFT"
    if(wtd == "d"):
        if(playercords[1] == 19):
            msg = "REACHED BORDER"
        else:
            playercords[1] += 1
            msg = "MOVED RIGHT"
    os.system("cls")