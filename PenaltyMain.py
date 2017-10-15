from PenaltyShoot import Penalty
import time

def main():
    dict={}
    dict['Name']=input("Enter Your Name     : ")
    dict['Difficulty']=input("Difficulty (Easy/Medium/Hard)    : ")
    print(dict)
    time.sleep(1.5)
    while True:
        try:
            test = int("hello")
        except ValueError:
            print("=========================================\n")
            time.sleep(0.25)
            print("     WELCOME TO PENALTY SHOOT OUT!!\n")
            time.sleep(0.25)
            print("=========================================\n")
        time.sleep(1)
        print(
    "][][][][][][][][][][][][\n"
    "][                    ][\n"
    "][          0         ][\n"
    "][         -|-        ][\n"
    "][         / \        ][\n\n\n"
    "            @")
        x=Penalty(str(input("Left, Middle, or Right?    : ")))
        x.shootout()
        act=str(input("Shoot another Penalty?(Yes/No)   : \n"))
        if act=="No":
            print("GOODBYE")
            break
        elif act=="Yes":
            pass
        else:
            print("ERROR, I assume you would want another shootout")
            time.sleep(1)
            print("Restarting Program")
            for i in range(0, 3):
                time.sleep(0.75)
                print(".")

main()