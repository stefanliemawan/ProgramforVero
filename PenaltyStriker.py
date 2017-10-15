import time

class Striker():

    def __init__(self):
        pass

    def shootleft(self):
        print("Shooting Left")
        for i in range (0,3):
            time.sleep(0.75)
            print(".")

    def shootright(self):
        print("Shooting Right")
        for i in range (0,3):
            time.sleep(0.75)
            print(".")

    def shootmiddle(self):
        print("Shooting Middle")
        for i in range (0,3):
            time.sleep(0.75)
            print(".")