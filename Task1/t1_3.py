class Titandex:
    def __init__(self,name,height,strength):
        self.name=name
        self.height=height
        self.strength=strength
        self.streak=0
    
    def TitanvsScout(self,scoutname,scoutstrength):
        print("{} vs {}".format(self.name,scoutname))
        if(self.strength>scoutstrength):
            self.streak+=1
            print("{} with strength {} and height {}m has won. \n Winning Streak is {}".format(self.name,self.strength,self.height,self.streak))
        elif(self.strength==scoutstrength):
            print("It is a draw!")
            self.streak=0
        else:
            print("Scout {} with strength {} has won".format(scoutname,scoutstrength))
            self.streak=0

    def TitanvsTitan(self,titan):
        print("{} vs {}".format(self.name,titan.name))

        if(self.name==titan.name):
            print("You Cannot Make The Titan Fight Itself")
        else:
            if(self.strength>titan.strength):
                self.streak+=1
                titan.streak=0
                print("{} with strength {} and height {}m has won. \n Winning Streak of {} is {}".format(self.name,self.strength,self.height,self.name,self.streak))
            elif(self.strength==titan.strength):
                print("Its a Draw")
                self.streak=0
                titan.streak=0
            else:
                self.streak=0
                titan.streak+=1
                print("{} with strength {} and height {}m has won. \n Winning Streak of {} is {}".format(titan.name,titan.strength,titan.height,titan.name,titan.streak))

bT=Titandex("Beast Titan",17,250)
arT=Titandex("Armoured Titan",15,250)
fT=Titandex("Founding Titan",13,350)
cT=Titandex("Cart Titan",4,175)

bT.TitanvsScout("Levi",300)
bT.TitanvsScout("Armin",250)
bT.TitanvsScout("Sasha",200)

bT.TitanvsTitan(fT)
bT.TitanvsTitan(arT)
bT.TitanvsTitan(cT)
bT.TitanvsTitan(bT)