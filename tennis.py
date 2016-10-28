#!/bin/usr/python
import sys
import csv
gamecount=0
gameserver=1
iteration=0
curr=1
#increment curr after every rally
def printing(string):
    global iteration
    global curr
    print "Iteration", ":", iteration
    if curr%2==1:
        print "Player1", ":", string
    else:
        print "Player2", ":", string
    print "P1", "Score" ,":", P1._player__Score
    print "P2", "Score" ,":", P2._player__Score
    print "P1", "Game Win Count", ":", P1._player__Game
    print "P2", "Game Win Count", ":", P2._player__Game
    print "P1", "Set Win Count", ":", P1._player__Set
    print "P2", "Set Win Count", ":", P2._player__Set

def scores(string):
        global iteration
        global curr
        global gameserver
        if string=="Serve":
         #if curr is even then current ball must be hit by player 2 and prev was hit by player 1
            iteration+=1
            printing(string)
            curr+=1
        elif string=="Ace":
            #decerement curr by one as he has to start new Point
            iteration+=1
            curr-=1
            if curr%2==0:
                P2.update(P2,P1)
            else :
                P1.update(P1,P2)
            printing(string)
            curr=gameserver
        elif string=="Fault":
            #if Fault decrement curr by one as he has to reserve
            iteration+=1
            curr-=1
            if curr%2==0:
                P1.update(P1,P2)
            else:
                P2.update(P2,P1)
            printing(string)
            curr=gameserver
        elif string=="Backhand" or string=="Forehand":
            iteration+=1
            printing(string)
            curr+=1
        elif string=="PointLost-SameSide" or string=="PointLost-Out" or string=="Nets":
            iteration+=1
            curr-=1
            if curr%2==0:
                P1.update(P1,P2)
            else :
                P2.update(P2,P1)
            printing(string)
            curr=gameserver
        elif string=="PointLost-CouldNotReach":
            iteration+=1
            if curr%2==1:
                P2.update(P2,P1)
            else:
                P1.update(P1,P2)
            printing(string)
            curr=gameserver

class player:
   def __init__(self):
        self.__Score=0
        self.__Game=0
        self.__Set=0
   def update(self,a,b):
         global gamecount
         global curr
         global gameserver
         if a.__Score==0:
             a.__Score=15
         elif a.__Score==15:
             a.__Score=30
         elif a.__Score==30 and b.__Score!=40:
             a.__Score=40
         elif a.__Score==30 and b.__Score==40:
             a.__Score="Deuce"
             b.__Score="Deuce"
         elif a.__Score==40 and b.__Score!=40:
             a.__Score=0
             a.__Game+=1
             b.__Score=0
             gamecount+=1
             gameserver+=1
             curr=gameserver
             if a.__Game>=6 and (abs(a.__Game-b.__Game)>=2):
                 a.__Set+=1
         elif a.__Score=="Deuce" and b.__Score=="Deuce":
             a.__Score='AD'
             b.__Score='-'
         elif a.__Score=='-':
             a.__Score="Deuce"
             b.__Score="Deuce"
         elif a.__Score=='AD':
             a.__Score=0
             b.__Score=0
             a.__Game+=1
             gamecount+=1
             gameserver+=1
             curr=gameserver
             if a.__Game>=6 and (abs(a.__Game-b.__Game)>=2):
                 a.__Set+=1
P1=player()
P2=player()
with open(sys.argv[-1],"rb") as fo:
    reader=csv.reader(fo,delimiter=' ')
    for i in reader:
        scores(i[1])
fo.close()
