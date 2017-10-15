from PenaltyStriker import Striker
import random

class Penalty(Striker):

    def __init__(self,shoot):
        Striker.__init__(self)
        self.shoot = shoot

    def shootout(self):
        keep = ['Left', 'Middle', 'Right']
        keeper = random.choice(keep)
        dir=Striker()
        if (self.shoot=='Left') and (keeper=='Left'):
            dir.shootleft()
            print(
                "][][][][][][][][][][][][\n"
                "][                    ][\n"
                "][  (@) 0             ][\n"
                "][    \-|-            ][\n"
                "][     / \            ][\n\n\n"
                "THE GOALIE CATCH THE BALL!! MAGNIFICENT!")
        elif (self.shoot=='Left') and (keeper=='Middle'):
            dir.shootleft()
            print(
                "][][][][][][][][][][][][\n"
                "][                    ][\n"
                "][  @       0         ][\n"
                "][         -|-        ][\n"
                "][         / \        ][\n\n\n"
                "IT'S A BRILLIANT GOALLL!!!! GOAL! GOAL! GOALLL!!!!")
        elif (self.shoot=='Left') and (keeper=='Right'):
            dir.shootleft()
            print(
                "][][][][][][][][][][][][\n"
                "][                    ][\n"
                "][  @           0     ][\n"
                "][             -|-    ][\n"
                "][             / \    ][\n\n\n"
                "IT'S A BRILLIANT GOALLL!!!! GOAL! GOAL! GOALLL!!!!")
        elif (self.shoot=='Middle') and (keeper=='Middle'):
            dir.shootmiddle()
            print(
                "][][][][][][][][][][][][\n"
                "][                    ][\n"
                "][          0         ][\n"
                "][        -(@)-       ][\n"
                "][         / \        ][\n\n\n"
                "THE GOALIE CATCH THE BALL!! MAGNIFICENT!")
        elif (self.shoot=='Middle') and (keeper=='Left'):
            dir.shootmiddle()
            print(
                "][][][][][][][][][][][][\n"
                "][                    ][\n"
                "][   0      @         ][\n"
                "][  -|-               ][\n"
                "][  / \               ][\n\n\n"
                "IT'S A BRILLIANT GOALLL!!!! GOAL! GOAL! GOALLL!!!!")
        elif (self.shoot=='Middle') and (keeper=='Right'):
            dir.shootmiddle()
            print(
                "][][][][][][][][][][][][\n"
                "][                    ][\n"
                "][          @     0   ][\n"
                "][               -|-  ][\n"
                "][               / \  ][\n\n\n"
                "IT'S A BRILLIANT GOALLL!!!! GOAL! GOAL! GOALLL!!!!")
        elif (self.shoot=='Right') and (keeper=='Right'):
            dir.shootright()
            print(
                "][][][][][][][][][][][][\n"
                "][                    ][\n"
                "][              0 (@) ][\n"
                "][             -|-/   ][\n"
                "][             / \    ][\n\n\n"
                "THE GOALIE CATCH THE BALL!! MAGNIFICENT!")
        elif (self.shoot=='Right') and (keeper=='Middle'):
            dir.shootright()
            print(
                "][][][][][][][][][][][][\n"
                "][                    ][\n"
                "][          0      @  ][\n"
                "][         -|-        ][\n"
                "][         / \        ][\n\n\n"
                "IT'S A BRILLIANT GOALLL!!!! GOAL! GOAL! GOALLL!!!!")
        elif (self.shoot=='Right') and (keeper=='Left'):
            dir.shootright()
            print(
                "][][][][][][][][][][][][\n"
                "][                    ][\n"
                "][   0             @  ][\n"
                "][  -|-               ][\n"
                "][  / \               ][\n\n\n"
                "IT'S A BRILLIANT GOALLL!!!! GOAL! GOAL! GOALLL!!!!")

        return str(self.shoot)