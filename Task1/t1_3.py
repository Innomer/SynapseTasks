class Titandex:
    def __init__(self,name,height,strength):
        self.name=name
        self.height=height
        self.strength=strength
        self.streak=0
    
    def TitanvsScout(self,scoutname,scoutstrength):
        if(self.strength>scoutstrength):
            self.streak+=1
            print("Titan {} with strength {} and height {}m has won".format(self.name,self.strength,self.height))
        elif(self.strength==scoutstrength):
            print("It is a draw!")
            self.streak=0
        else:
            print("Scout {} with strength {} has won".format(scoutname,scoutstrength))
            self.streak=0

    def TitanvsTitan(self,titanname,titanheight,titanstrength):

        if(self.name==titanname):
            print("You Cannot Make The Titan Fight Itself")
        else:
            if(self.strength>titanstrength):
                print("Titan {} with strength {} and height {}m has won".format(self.name,self.strength,self.height))
                self.streak+=1
            elif(self.strength==titanstrength):
                print("Its a Draw")
                self.streak=0
            else:
                print("Titan {} with strength {} and height {}m has won".format(titanname,titanstrength,titanheight))
                self.streak=0

bT=Titandex("Beast Titan",17,250)
bT.TitanvsScout("Levi",300)
bT.TitanvsScout("Armin",250)
bT.TitanvsScout("Sasha",200)
bT.TitanvsTitan("Founding Titan",13,350)
bT.TitanvsTitan("Armored Titan",15,250)
bT.TitanvsTitan("Cart Titan",4,175)
bT.TitanvsTitan("Beast Titan",17,250)