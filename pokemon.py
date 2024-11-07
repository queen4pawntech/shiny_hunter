import random
import math

class Pokemon:
    shiny=False
    name=''
    moves=[]
    def __init__(self, level):
        self.level = level
        self.health=20+3*level

class Geodude(Pokemon):
    def __init__(self, level):
        super().__init__(level)
        self.attack=math.floor(5+0.5*(level))
        self.defense=5+2*(level)
        self.speed=math.floor(3+0.5*(level))
    name='Geodude'
    moves=['Rock Throw', 'Rollout', 'Explosion', 'Tackle']

class Magikarp(Pokemon):
    def __init__(self, level):
        super().__init__(level)
        self.attack=math.floor(2+0.5*(level))
        self.defense=math.floor(2+0.5*(level))
        self.speed=math.floor(2+0.5*(level))
    name='Magikarp'
    moves=['Tackle', 'Splash', 'Hyper Beam', 'Bounce']

class Pikachu(Pokemon):
    def __init__(self, level):
        super().__init__(level)
        self.attack=math.floor(5+0.75*(level))
        self.defense=math.floor(5+0.5*(level))
        self.speed=math.floor(5+1.5*(level))
    name='Pikachu'
    moves=['Tackle', 'Thunderbolt', 'Quick Attack', 'Growl']

class Pidgey(Pokemon):
    def __init__(self, level):
        super().__init__(level)
        self.attack=math.floor(2+0.75*(level))
        self.defense=math.floor(2+0.5*(level))
        self.speed=math.floor(2+1.5*(level))
    name='Pidgey'
    moves=['Tackle', 'Growl', 'Wing Attack', 'Scary Face']

class Mewtwo(Pokemon):
    def __init__(self, level):
        super().__init__(level)
        self.attack=math.floor(10 + 2.5*(level))
        self.defense=math.floor(10 + 1.5*(level))
        self.speed=math.floor(10 + 2.5*(level))
    name='Mewtwo'
    moves=['Hyper Beam', 'Psystrike', 'Fire Blast', 'Ice Beam']

class Bulbasaur(Pokemon):
    def __init__(self, level):
        super().__init__(level)
        self.attack=math.floor(20+1.1*(level))
        self.defense=math.floor(20+1.25*(level))
        self.speed=20+1*(level)
    name='Bulbasaur'
    shiny=False
    moves=['Vine Whip', 'Tackle', 'Razor Leaf', 'Solar Beam']

class Charmander(Pokemon):
    def __init__(self, level):
        super().__init__(level)
        self.attack=math.floor(20+1.25*(level))
        self.defense=20+1*(level)
        self.speed=math.floor(20+1.25*(level))
    name='Charmander'
    moves=['Scratch', 'Growl', 'Flamethrower', 'Shadow Claw']

class Squirtle(Pokemon):
    def __init__(self, level):
        super().__init__(level)
        self.attack=20+1*(level)
        self.defense=math.floor(20+1.25*(level))
        self.speed=20+1*(level)
    name='Squirtle'
    moves=['Tackle', 'Tail Whip', 'Bite', 'Hydro Pump']
################################ TEST CODE ##################################################
"""def test_Geodude():
    testGeodude = Geodude(5)
    if testGeodude.name == 'Geodude':
        return True
    else:
        return False

"""
################################ DICTIONARIES AND LISTS ##################################################
attbank={'Tackle':0.4, 'Scratch':0.4, 'Rock Throw':0.5, 'Rollout':0.3, 'Explosion':2.5, 'Splash':0.0, 'Hyper Beam':1.5, 'Bounce':0.85, 'Thunderbolt':0.9, 'Quick Attack':0.4, 'Wing Attack':0.6, 'Psystrike':1.0, 'Fire Blast': 1.1, 'Ice Beam':0.9, 'Vine Whip':0.45, 'Razor Leaf':0.55, 'Solar Beam':1.2, 'Flamethrower':0.9, 'Shadow Claw':0.7, 'Bite':0.6, 'Hydro Pump':1.1}
atkstatbank={'Growl':0.75,'Attract':0.8}
defstatbank={'Screech':0.8,'Tail Whip':0.75}
spdstatbank={'Scary Face':0.75}
turn=0
wildPoke = {'Geodude':Geodude(turn+random.randint(1,5)), 'Magikarp':Magikarp(turn+random.randint(1,5)), 'Pidgey':Pidgey(turn+random.randint(1,5)), 'Pikachu':Pikachu(turn+random.randint(1,5)), 'Mewtwo':Mewtwo(turn+random.randint(7,10))}
starters={'Bulbasaur':Bulbasaur(5), 'Charmander':Charmander(5), 'Squirtle':Squirtle(5)}
posans=['Yes','yes','No', 'no']
posfans=['E','H','B']
bag={'Pokeball':0,'Potion':0}
caughtshiny=False
bank=0

def chustart():
    starter=0
    while starter not in starters:
        starter=input("""Do you want your starter to be Bulbasaur, Charmander, or Squirtle?:
""")
        if starter not in starters:
            print('Please pick between Bulbasaur, Charmander, or Squirtle.')
    return starters[starter]

def nickname(pok):
    nick=0
    while nick not in posans:
        nick=input("""Do you want to give your pokemon a name?(Yes/No):
""")
        if nick not in posans:
            print("""
Please respond "Yes" or "No".

""")
    if nick=='Yes' or nick=='yes':
        pok.name=input("""
What do you want to name your pokemon?
""")

def ranenc():
    rannum=random.randint(1,1001)
    if turn<40:
        ranshiny=random.randint(1,math.floor((8192-200*turn)))
    else:
        ranshiny=random.randint(1,100)
    if rannum>=1 and rannum<=250:
        enc=Geodude(turn+random.randint(1,5))
    elif rannum>=251 and rannum<=500:
        enc=Magikarp(turn+random.randint(1,5))
    elif rannum>=501 and rannum<=750:
        enc=Pikachu(turn+random.randint(1,5))
    elif rannum>=751 and rannum<=1000:
        enc=Pidgey(turn+random.randint(1,5))
    elif rannum==1001:
        enc=Mewtwo(turn+random.randint(7,10))
    if ranshiny==1:
        enc.shiny=True
    return enc

def damagestep(user,move,enemy):
    if move in atkstatbank:
        if math.floor(enemy.attack*atkstatbank[move])>1:
            enemy.attack=math.floor(enemy.attack*atkstatbank[move])
            return enemy
        else:
            enemy.attack=1
            return enemy
    elif move in defstatbank:
        if math.floor(enemy.defense*defstatbank[move])>1:
            enemy.defense=math.floor(enemy.defense*defstatbank[move])
            return enemy
        else:
            enemy.defense=1
            return enemy
    elif move in spdstatbank:
        if math.floor(enemy.speed*spdstatbank[move])>1:
            enemy.speed=math.floor(enemy.speed*spdstatbank[move])
            return enemy
        else:
            enemy.speed=1
            return enemy
    elif move in attbank:
        if math.floor(user.attack*attbank[move]-enemy.defense)>1:
            enemy.health=math.floor(enemy.health - (user.attack*attbank[move]-enemy.defense))
            return enemy
        else:
            enemy.health=(enemy.health-1)
            return enemy

def shinybattle(pk1,pk2,moneys):
    shinycaught==False
    if pk2.shiny==True:
        print('You encountered a lv. ' + str(pk2.level) + ' ' + pk2.name + ' that is shiny!  You can attempt to capture the ' + pk2.name + """
""")
    print("""
"""+
pk2.name+'      lvl. '+str(pk2.level)+' Health: '+ str(pk2.health) + '/'+ str((20+3*pk2.level))+"""
============================

"""+
pk1.name+'      lvl. '+str(pk1.level)+' Health: '+ str(pk1.health) + '/'+ str((20+3*pk1.level))+"""
============================
"""+
pk1.moves[0]+"""
"""+
pk1.moves[1]+"""
"""+
pk1.moves[2]+"""
"""+
pk1.moves[3])
    while pk1.health>0 or pk2.health>0 or shinycaught==False:
        umove=0
        npcmove=pk2.moves[random.randint(0,3)]
        move=0
        while move !='Attack' or move!='Catch':
            move=input("""Do you want to attack the shiny """,pk2.name,""" or do you want to try and catch it?(Attack or Catch)
""")
            if move!='Attack' or move!='Catch':
                print("""Please enter either 'Attack' or 'Catch'
""")
        if move=='Catch':
            shinycaught=capture(pk2)
        else:
            while umove not in pk1.moves:
                umove=input("""What move do you want ' + pk1.name + ' to use?
"""+
pk1.moves[0]+"""
"""+
pk1.moves[1]+"""
"""+
pk1.moves[2]+"""
"""+
pk1.moves[3])
                if umove not in pk1.moves:
                    print(pk1.name + " doesn't know that move!  Pick one that " + pk1.name +""" does know!
""")
            if pk1.speed > pk2.speed:
                pk2=damagestep(pk1,umove,pk2)
                print("""
""" + pk1.name + " used " + umove + " on " + pk2.name + """!
""")
                pk1=damagestep(pk2,npcmove,pk1)
                print("""
""" + pk2.name + " used " + npcmove + " on " + pk1.name + """!
""")
            else:
                pk1=damagestep(pk2,npcmove,pk1)
                print("""
""" + pk2.name + " used " + umove + " on " + pk1.name + """!
""")
                pk2=damagestep(pk1,umove,pk2)
                print("""
""" + pk1.name + " used " + umove + " on " + pk2.name + """!
""")
    if pk1.health <= 0:
        print('You died before you could catch a shiny pokemon!  Better luck next time!')
        quit()
    elif shinycaught==True:
        print('Congrats you caught a shiny pokemon!  You can finally escape!')
        quit()
    elif pk2.health<=0:
        print("You defeated ", pk2.name,"!.","""
    """, pk1.name," leveled up to " , str(pk1.level+1),"""
    You also earned""", str(100+turn*5),"pokedollars!")
        levelup(pk1)
        moneys+=(100+turn*5)




def battle(pk1,pk2,moneys):
    if pk2.shiny==False:
        print('You encountered a lv. ' + str(pk2.level) + ' ' + pk2.name + """ that is not shiny!
""")
    else:
        print('You encountered a lv. ' + str(pk2.level) + ' ' + pk2.name + ' that is shiny!  You can attempt to capture the ' + pk2.name + """
""")
    while pk1.health>0 or pk2.health>0:
        umove=0
        npcmove=pk2.moves[random.randint(0,3)]
        print("""
"""+
pk2.name+'      lvl. '+str(pk2.level)+' Health: '+ str(pk2.health) + '/'+ str((20+3*pk2.level))+"""
============================

"""+
pk1.name+'      lvl. '+str(pk1.level)+' Health: '+ str(pk1.health) + '/'+ str((20+3*pk1.level))+"""
============================
"""+
pk1.moves[0]+"""
"""+
pk1.moves[1]+"""
"""+
pk1.moves[2]+"""
"""+
pk1.moves[3])
        while umove not in pk1.moves:
            umove=input("What move do you want " + pk1.name + """ to use?
""")
            if umove not in pk1.moves:
                print(pk1.name + " doesn't know that move!  Pick one that " + pk1.name +""" does know!
"""+
pk1.moves[0]+"""
"""+
pk1.moves[1]+"""
"""+
pk1.moves[2]+"""
"""+
pk1.moves[3])
        if pk1.speed > pk2.speed:
            pk2=damagestep(pk1,umove,pk2)
            print("""
""" + pk1.name + " used " + umove + " on " + pk2.name + """!
  """)
            pk1=damagestep(pk2,npcmove,pk1)
            print("""
""" + pk2.name + " used " + npcmove + " on " + pk1.name + """!
  """)
        else:
            pk1=damagestep(pk2,npcmove,pk1)
            print("""
""" + pk2.name + " used " + npcmove + " on " + pk1.name + """!
  """)
            pk2=damagestep(pk1,umove,pk2)
            print("""
""" + pk1.name + " used " + umove + " on " + pk2.name + """!
  """)
    if pk1.health <= 0:
        print('You died before you could catch a shiny pokemon!  Better luck next time!')
        quit()
    if pk2.health<=0:
        print("You defeated ", pk2.name,"!.","""
""", pk1.name," leveled up to " , str(pk1.level+1),"""
You also earned""", str(100+turn*5),"pokedollars!")
        levelup(pk1)

def heal():
    if pkuser.health==20+3*pkuser.level:
        print(pkuser.name+' is already fully healed!')
    else:
        if pkuser.health+20>=20+3*pkuser.level:
            pkuser.health=20+3*pkuser.level
            print(pkuser.name+' has been fully healed!')
        else:
            pkuser.health+=20
            print(pkuser.name+' has been healed to '+ str(pkuser.health) +' health points!')

def capture(pkshiny):
    if (pkshiny.health/(20+pkshiny.level*3))>=0.2:
        catch=random.randint(1,2)
    if (pkshiny.health/(20+pkshiny.level*3))>=0.4:
        catch=random.randint(1,4)
    if (pkshiny.health/(20+pkshiny.level*3))>=0.6:
        catch=random.randint(1,8)
    if (pkshiny.health/(20+pkshiny.level*3))>=0.8:
        catch=random.randint(1,16)
    if (pkshiny.health/(20+pkshiny.level*3))>=1:
        catch=random.randint(1,24)
    if catch==1:
        print(pkshiny.name + ' was captured!')
        return True
    else:
        print(pkshiny.name + ' broke out of the ball!')
        return False

def shop(banki,bagi):
    want=0
    shopit=['Pokeball','Potion']
    while want not in shopit:
        want=input("What do you want to buy? You have "+ str(banki)+ """ pokedollars!
$200 Pokeball   $300 Potion

""")
        if want not in shopit:
            print("""Please input "Pokeball" or "Potion"
""")
    if want == "Pokeball":
        if banki<200:
            print("""You are broke you can't afford to buy a pokeball!
""")
        else:
            bagi[want]+=1
            banki-=200
            print("""A pokeball was added to your bag!
""")

    if want == "Potion":
        if banki<300:
            print("""You are broke you can't afford to buy a potion!
""")
        else:
            bagi[want]+=1
            banki-=300
            print("""A potion was added to your bag!
""")

def levelup(pk):
    if pk.level==100:
        return pk
    else:
        pk.level+=1
        if pk.species=='Bulbasaur':
            pk.health=20+3*(pk.level)
            pk.attack=10+1.1*(pk.level)
            pk.defense=10+1.25*(pk.level)
            pk.speed=10+1*(pk.level)
        if pk.species=='Charmander':
            pk.health=20+3*(pk.level)
            pk.attack=10+1.25*(pk.level)
            pk.defense=10+1*(pk.level)
            pk.speed=10+1.25*(pk.level)
        if pk.species=='Squirtle':
            pk.health=20+3*(pk.level)
            pk.attack=10+1*(pk.level)
            pk.defense=10+1.25*(pk.level)
            pk.speed=10+1*(pk.level)
        return pk

def shinyornah(pk1,pk2,bank):
    if pk2.shiny==False:
        battle(pk1,pk2,bank)
    else:
        shinybattle(pk1,pk2,bank)

#Game Execution
print("""Hello trainer!  You're stuck in a dimension until you catch a shiny pokemon!
If your starter pokemon faints before you catch a shiny pokemon, then you die too!
Each turn you'll be able to choose to encounter a pokemon, buy a potion or pokeball, or heal your pokemon.
After you defeat a pokemon, you'll get some money and your starter pokemon will raise a level.  Goodluck!
""")

pkuser=chustart()
nickname(pkuser)
ran=ranenc()

while caughtshiny==False or pkuser.health>0:
    ans=0
    ran=ranenc()
    while ans not in posfans:
        ans=input('Do you want to encounter a pokemon(E), heal your pokemon(H), or buy items(B)?: ')
        if ans not in posfans:
            print("""Please respond with "E", "H" or "B".
""")
    if ans=='E':
        if ran.shiny==True:
            shinybattle(pkuser,ran,bank)
        else:
            battle(pkuser,ran,bank)
    elif ans=='H':
        if bag['Potion']==0:
            print("""You don't have any potions, so you cant heal""", pkuser.name,"""
""")
        else:
            heal()
    else:
        shop(bank,bag)
