#i am using colaboratory
#Andrii Radyhin Hexapawn AI
import random
import os
movevalue=[0.33,0.66,1,0.33,0.66,1,0.25,0.50,0.75,1,1,0.25,0.50,0.75,1,0.33,
           0.66,1,1,0.5,1,1,1,1,0.33,0.66,1,1,0.5,1,0.33,0.66,1,1,0.5,1,0.5,1,
           0.5,1,0.5,1,0.5,1,1,0.5,1,0.5,1,0.33,0.66,1,1,1,0.5,1,1,0.5,1,1,0.5,
           1,1,1,0.5,1,1,1,0.5,1,1,0.5,1,0.5,1,1,0.33,0.66,1,0.5,1,1,0.33,0.66,
           1,0.5,1,0.5,1,0.5,1,0.33,0.66,1,1,1,0.25,0.5,0.75,1,1,1,1,1]
move=[]

def change():
  for x in move:
    if (x==7 or x==12 or x==97): #0.25
      movevalue[x-1]+=0.05
      movevalue[x]-=0.05
      movevalue[x+1]-=0.05
    elif (x==8 or x==13 or x==98): #0.50
      movevalue[x-1]+=0.05
      movevalue[x-2]-=0.05
      movevalue[x]-=0.05
    elif (x==9 or x==14 or x==99): #0.75
      movevalue[x-1]+=0.05
      movevalue[x-2]-=0.05
      movevalue[x-3]-=0.05
    elif (x==1 or x==4 or x==16 or x==25 or x==31 or x==50 or x==77 or x==83 or x==92): #0.33
      movevalue[x-1]+=0.05
      movevalue[x]-=0.05
    elif (x==2 or x==5 or x==17 or x==26 or x==32 or x==51 or x==78 or x==84 or x==93): #0.66
      movevalue[x-1]+=0.05
      movevalue[x-2]-=0.05
    elif (x==10 or x==15 or x==100): #1 after 0.75
      movevalue[x-4]-=0.05
      movevalue[x-3]-=0.05
      movevalue[x-2]-=0.05
    elif (x==3 or x==6 or x==18 or x==27 or x==33 or x==52 or x==79 or x==85 or x==94): #1 after 0.66

      movevalue[x-3]-=0.05
      movevalue[x-2]-=0.05
    
def app(x):
  move.append(x)
  def Reset(): 
  game=[[2,4,6],[0,0,0],[1,3,5]]
  return game
  
def Hprint(game):
    print("   c1 c2 c3")
    print("l1",game[0])
    print("l2",game[1])
    print("l3",game[2])

def Existpawn(pawn,game):
  count=0
  for i in range(len(game)):
    for j in range(len(game[i])):
      if game[i][j]==pawn:
        count+=1
        break
  if count == 1:
    return 1
  else:
    return 0

def Playermove(game,line,column,pawn):
  #position of pawn and what pawn
  for i in range(len(game)):
    for j in range(len(game[i])):
      if game[i][j]==pawn:
        a=i
        b=j
        break
  #back play
  if line>a:
    print("Error, You cannt play pawn back")
    return 0
  #diagonal play
  elif (line<a) and (column!=b):
    if (abs(column-b)==1) and (a-line==1):
      if ((game[line][column]==2) or (game[line][column]==4) 
      or (game[line][column]==6)):
        game[a][b]=0
        game[line][column]=pawn
        return game
      else:
        print("Error, You cannt play this position (diagonal)")
        return 0
    else:
        print("Error, You cannt play this position (diagonal)")
        return 0
  #front play
  elif (a-line==1)and(column==b):
    if game[line][column]==0:
      game[a][b]=0
      game[line][column]=pawn
      return game
    else:
      print("There is opponent's pawn already")
      return 0
  #right or left play
  elif (line==a)and((column<b)or(column>b)):
    print ("You can't play left or right")
    return 0
  print("Error!!!")
  return 0
  
 def Machineplay(game):
  a1 =-1; a2 =-1; a3 =-1; a4 =-1; a5 =-1; a6 =-1; b1 =-1; b2 =-1; b3 =-1; b4 =-1; b5 =-1; b6 =-1
  for a in range(1,7):
   for i in range(len(game)):
      for j in range(len(game[i])):
        if game[i][j]==a:
          if a==1:
            a1=i; b1=j
          elif a==2:
            a2=i; b2=j
          elif a==3:
            a3=i; b3=j
          elif a==4:
            a4=i; b4=j
          elif a==5:
            a5=i; b5=j
          elif a==6:
            a6=i; b6=j

    #2 4 6
    #1 0 0 
    #0 3 5
  if (((a1==1) and (b1==0)) and ((a2==0) and (b2==0)) and ((a3==2) and(b3==1)) and ((a4==0) and (b4==1)) and ((a5==2) and (b5==2)) and ((a6==0) and (b6==2))):
    u=random.uniform(0,1)
    if u<=movevalue[0]:
      game[0][1]=0 #1
      game[1][0]=4
      app(1) 
    elif u<=movevalue[1]:
      game[0][1]=0
      game[1][1]=4 #2
      app(2)
    else:
      game[0][2]=0 #3
      game[1][2]=6
      app(3)
    return game

    #2 4 6
    #0 0 5
    #1 3 0
  elif (((a1==2)and(b1==0))and((a2==0)and(b2==0))and((a3==2)and(b3==1))and((a4==0)and(b4==1))and((a5==1)and(b5==2))and((a6==0)and(b6==2))):
    u=random.uniform(0,1)
    if u<=movevalue[3]:
      game[0][0]=0 #4
      game[1][0]=2
      app(4)
    elif u<=movevalue[4]:
      game[0][1]=0
      game[1][1]=4 #5
      app(5)
    else:
      game[0][1]=0
      game[1][2]=4 #6
      app(6)
    return game
      
    #2 4 6
    #0 3 0
    #1 0 5
  elif(((a1==2)and(b1==0))and((a2==0)and(b2==0))and((a3==1)and(b3==1))and((a4==0)and(b4==1))and((a5==2)and(b5==2))and((a6==0)and(b6==2))):
    u=random.uniform(0,1)
    if u<=movevalue[6]:
      game[0][0]=0
      game[1][0]=2 #7
      app(7)
    elif u<=movevalue[7]:
      game[0][0]=0
      game[1][1]=2 #8
      app(8)
    elif u<=movevalue[8]:
      game[0][2]=0
      game[1][1]=6 #9
      app(9)
    else:
      game[0][2]=0
      game[1][2]=6 #10
      app(10)
    return game

    #2 0 6
    #3 0 0
    #0 0 5
  elif(a1==-1)and((a2==0)and(b2==0))and((a3==1)and(b3==0))and(a4==-1)and((a5==2)and(b5==2))and((a6==0)and(b6==2)):
    game[0][2]=0
    game[1][2]=6 #win #11
    app(11)
    return game
    
    #2 0 6
    #4 3 0
    #0 0 5
  elif(a1==-1)and((a2==0)and(b2==0))and((b3==1)and(a3==1))and((a4==1)and(b4==0))and((a5==2)and(b5==2))and((a6==0)and(b6==2)):
    u=random.uniform(0,1)
    if u<=movevalue[11]:
      game[0][0]=0
      game[1][1]=2 #12
      app(12)
    elif u<=movevalue[12]:
      game[1][0]=0
      game[2][1]=4 #win #13
      app(13)
    elif u<=movevalue[13]:
      game[0][2]=0
      game[1][1]=6 #14
      app(14)
    else:
      game[0][2]=0
      game[1][2]=6 #player wins #15
      app(15)
    return game

    #0 0 6
    #4 5 0
    #0 0 0
  elif(a1==-1)and(a2==-1)and(a3==-1)and((a4==1)and(b4==0))and((a5==1)and(b5==1))and((a6==0)and(b6==2)):
    u=random.uniform(0,1)
    if u<=movevalue[15]:
      game[1][0]=0
      game[2][0]=4 #win # 16
      app(16)
    elif u<=movevalue[16]:
      game[0][2]=0
      game[1][1]=6 #win # 17
      app(17)
    else:
      game[0][2]=0
      game[1][2]=6 #player wins #18
      app(18)
    return game

    #0 0 6
    #4 2 5
    #0 0 0
  elif(a1==-1)and((a2==1)and(b2==1))and(a3==-1)and((a4==1)and(b4==0))and((a5==1)and(b5==2))and((a6==0)and(b6==2)):
    game[1][0]=0
    game[2][0]=4 #win #19
    app(19)
    return game

    #2 0 0
    #4 3 5
    #0 0 0
  elif(a1==-1)and((a2==0)and(b2==0))and((a3==1)and(b3==1))and((a4==1)and(b4==0))and((a5==1)and(b5==2))and(a6==-1):
    u=random.uniform(0,1)
    if u<=movevalue[19]:
      game[1][0]=0
      game[2][0]=4 #win #20
      app(20)
    else:
      game[0][0]=0
      game[1][1]=2 #player wins #21
      app(21)
    return game
     
    #2 0 0
    #4 6 5
    #0 0 0
  elif(a1==-1)and((a2==0)and(b2==0))and(a3==-1)and((a4==1)and(b4==0))and((a5==1)and(b5==2))and((a6==1)and(b6==1)):
    game[1][0]=0
    game[2][0]=4 #win #22
    app(22)
    return game

    #2 0 6
    #4 0 5
    #0 3 0
  elif(a1==-1)and((a2==0)and(b2==0))and((a3==2)and(b3==1))and((a4==1)and(b4==0))and((a5==1)and(b5==2))and((a6==0)and(b6==2)):
    game[1][0]=0
    game[2][0]=4 #win #23
    app(23)
    return game

    #2 0 0
    #4 5 0
    #0 0 0
  elif(a1==-1)and((a2==0)and(b2==0))and(a3==-1)and((a4==1)and(b4==0))and((a5==1)and(b5==1))and(a6==-1):
    game[1][0]=0
    game[2][0]=4 #24
    app(24)
    return game

    #2 0 6
    #1 5 0
    #0 3 0
  elif((a1==1)and(b1==0))and((a2==0)and(b2==0))and((a3==2)and(b3==1))and(a4==-1)and((a5==1)and(b5==1))and(a6==-1):
    u=random.uniform(0,1)
    if u<=movevalue[24]:
      game[0][0]=0
      game[1][1]=2 #player wins #25
      app(25)
    elif u<=movevalue[25]:
      game[0][2]=0
      game[1][1]=6 #win #26
      app(26)
    else:
      game[0][2]=0
      game[1][2]=6 #27
      app(27)
    return game
    
    #2 0 0
    #1 5 3
    #0 0 0
  elif((a1==1)and(b1==0))and((a2==0)and(b2==0))and((a3==1)and(b3==2))and(a4==-1)and((a5==1)and(b5==1))and(a6==-1):
    game[0][0]=0
    game[1][1]=2 #p wins #28
    app(28)
    return game     
    
    #2 4 0
    #1 3 6
    #0 0 5
  elif((a1==1)and(b1==0))and((a2==0)and(b2==0))and((a3==1)and(b3==1))and((a4==0)and(b4==1))and((a5==2)and(b5==2))and((a6==1)and(b6==2)):
    u=random.uniform(0,1)
    if u<=movevalue[28]:
      game[0][0]=0
      game[1][1]=2 #29
      app(29)
    else:
      game[0][1]=0
      game[1][0]=4 #30
      app(30)
    return game
    
    #2 4 0
    #1 0 3
    #0 0 5
  elif((a1==1)and(b1==0))and((a2==0)and(b2==0))and((a3==1)and(b3==2))and((a4==0)and(b4==1))and((a5==2)and(b5==2))and(a6==-1):
    u=random.uniform(0,1)
    if u<=movevalue[30]:
      game[0][1]=0
      game[1][0]=4 #p wins #31
      app(31)
    elif u<=movevalue[31]:
      game[0][1]=0
      game[1][1]=4 #32
      app(32)
    else:
      game[0][1]=0
      game[1][2]=4 #win #33
      app(33)
    return game

    #2 0 0
    #1 5 3
    #0 0 0
  elif((a1==1)and(b1==0))and((a2==0)and(b2==0))and((a3==1)and(b3==2))and(a4==-1)and((a5==1)and(b5==1))and(a6==-1):
    game[0][0]=0
    game[1][1]=2 #p wins #34
    app(34)
    return game

    #0 4 6
    #2 3 5
    #1 0 0
  elif((a1==2)and(b1==0))and((a2==1)and(b2==0))and((a3==1)and(b3==1))and((a4==0)and(b4==1))and((a5==1)and(b5==2))and((a6==0)and(b6==2)):
    u=random.uniform(0,1)
    if u<=movevalue[34]:
      game[0][1]=0
      game[1][2]=4 #win #35
      app(35)
    else:
      game[0][2]=0
      game[1][1]=6 #36
      app(36)
    return game

    #0 4 0
    #2 1 5
    #0 0 0
  elif((a1==1)and(b1==1))and((a2==1)and(b2==0))and(a3==-1)and((a4==0)and(b4==1))and((a5==1)and(b5==2))and((a6==-1)):
    u=random.uniform(0,1)
    if u<=movevalue[36]:
      game[1][0]=0
      game[2][0]=2 #win #37
      app(37)
    else:
      game[0][1]=0
      game[1][2]=4 #player wins #38
      app(38)
    return game

    #2 4 0
    #1 3 6
    #0 0 5
  elif((a1==1)and(b1==0))and((a2==0)and(b2==0))and((a3==1)and(b3==1))and((a4==0)and(b4==1))and((a5==2)and(b5==2))and((a6==1)and(b6==2)):
    u=random.uniform(0,1)
    if u<=movevalue[38]:
      game[0][0]=0
      game[1][1]=2 #39
      app(39)
    else:
      game[0][1]=0
      game[1][0]=4 #p wins #40
      app(40)
    return game

    #0 4 0
    #1 5 6
    #0 0 0
  elif((a1==1)and(b1==0))and(a2==-1)and(a3==-1)and((a4==0)and(b4==1))and((a5==1)and(b5==1))and((a6==1)and(b6==2)):
    u=random.uniform(0,1)
    if u<=movevalue[40]:
      game[0][1]=0
      game[1][0]=4 #p wins #41
      app(41)
    else:
      game[1][2]=0
      game[2][2]=6 #win #42
      app(42)
    return game

    #2 4 0
    #1 0 3
    #0 0 5
  elif((a1==1)and(b1==0))and((a2==0)and(b2==0))and((a3==1)and(b3==2))and((a4==0)and(b4==1))and((a5==2)and(b5==2))and(a6==-1):
    u=random.unifrom(0,1)
    if u<=movevalue[42]:
      game[1][0]=0
      game[1][1]=4 #43
      app(43)
    else:
      game[1][0]=0
      game[1][2]=4 #win #44 
      app(44)
    return game

    #2 0 0
    #1 5 3
    #0 0 0
  elif((a1==1)and(b1==0))and((a2==0)and(b2==0))and((a3==1)and(b3==2))and(a4==-1)and((a5==1)and(b5==1))and(a6==-1):
    game[0][0]=2
    game[1][1]=2 #p wins 45
    app(45)
    return game

    #0 4 6
    #2 3 5
    #1 0 0
  elif((a1==2)and(b1==0))and((a2==1)and(b2==0))and((a3==1)and(b3==1))and((a4==0)and(b4==1))and((a5==1)and(b5==2))and((a6==0)and(b6==2)):
    u=random.uniform(0,1)
    if u<=movevalue[46]:
      game[0][1]=0
      game[1][2]=4 #p wins 46
      app(46)
    else:
      game[0][2]=0
      game[1][1]=6 #47
      app(47)
    return game
    
    #0 4 0
    #2 1 5
    #0 0 0
  elif((a1==1)and(b1==1))and((a2==1)and(b2==0))and(a3==-1)and((a4==0)and(b4==1))and((a5==1)and(b5==2))and(a6==-1):
    u=random.uniform(0,1)
    if u<=movevalue[47]:
      game[1][0]=0
      game[2][0]=2 #win 48
      app(48)
    else:
      game[0][1]=0
      game[1][2]=4 #p wins 49
      app(49)
    return game
         
    #0 4 6
    #1 2 0
    #0 0 5
  elif((a1==1)and(b1==0))and((a2==1)and(b2==1))and(a3==-1)and((a4==0)and(b4==1))and((a5==2)and(b5==2))and((a6==0)and(b6==2)):
    u=random.uniform(0,1)
    if u<=movevalue[49]:
      game[0][1]=0
      game[1][0]=4 #50
      app(50)
    elif u<=movevalue[50]:
      game[1][1]=0
      game[2][1]=2 #win 51
      app(51)
    else:
      game[0][2]=0
      game[1][2]=6 #52
      app(52)
    return game
    
    #0 0 6
    #4 2 5
    #0 0 0
  elif(a1==-1)and((a2==1)and(b2==1))and(a3==-1)and((a4==1)and(b4==0))and((a5==1)and(b5==2))and((a6==0)and(b6==2)):
    game[1][0]=0
    game[2][0]=4 #win 53
    app(53)
    return game

    #0 4 0
    #1 5 6
    #0 0 0
  elif((a1==1)and(b1==0))and(a2==-1)and(a3==-1)and((a4==0)and(b4==1))and((a5==1)and(b5==1))and((a6==1)and(b6==2)):
    game[1][0]=0
    game[2][0]=1 #win 54
    app(54)
    return game

    #0 4 6
    #0 1 0
    #0 0 5
  elif((a1==1)and(b1==1))and(a2==-1)and(a3==-1)and((a4==0)and(b4==1))and((a5==2)and(b5==2))and((a6==0)and(b6==2)):
    u=random.uniform(0,1)
    if u<=movevalue[54]:
      game[0][2]=0
      game[1][1]=6 # 55
      app(55)
    else:
      game[0][2]=0
      game[1][2]=6 #win 56
      app(56)
    return game
    
    #0 4 0
    #0 6 5
    #0 0 0
  elif(a1==-1)and(a2==-1)and(a3==-1)and((a4==0)and(b4==1))and((a5==1)and(b5==2))and((a6==1)and(b6==1)):
    game[1][1]=0
    game[2][1]=6 #win 57
    app(57)
    return game

    #0 4 6
    #0 5 0
    #1 0 0
  elif((a1==2)and(b1==0))and(a2==-1)and(a3==-1)and((a4==0)and(b4==1))and((a5==1)and(b5==1))and((a6==0)and(b6==2)):
    u=random.uniform(0,1)
    if u<=movevalue[57]:
      game[0][2]=0
      game[1][1]=6 #58
      app(58)
    else:
      game[0][2]=0
      game[1][2]=6 #59
      app(59)
    return game
    
    #0 4 0
    #1 6 0
    #0 0 0
  elif((a1==1)and(b1==0))and(a2==-1)and(a3==-1)and((a4==0)and(b4==1))and(a5==-1)and((a6==1)and(b6==1)):
    game[1][1]=0
    game[2][1]=6 #win #60
    app(60)
    return game

    #0 4 6
    #0 2 5
    #1 0 0
  elif((a1==2)and(b1==0))and((a2==1)and(b2==1))and(a3==-1)and((a4==0)and(b4==1))and((a5==1)and(b5==2))and((a6==0)and(b6==2)):
    u=random.uniform(0,1)
    if u<=movevalue[60]:
      game[1][1]=0
      game[2][1]=2 #win 61
      app(61)
    else:
      game[0][1]=0
      game[1][2]=4 #62
      app(62)
    return game
    
    #0 0 6
    #0 1 4
    #0 0 0
  elif((a1==1)and(b1==1))and(a2==-1)and(a3==-1)and((a4==1)and(b4==2))and(a5==-1)and((a6==0)and(b6==2)):
    game[0][2]=0
    game[1][1]=6 #win 63
    app(63)
    return game

    #0 0 6
    #1 2 4
    #0 0 0
  elif((a1==1)and(b1==1))and((a2==1)and(b2==1))and(a3==-1)and((a4==1)and(b4==2))and(a5==-1)and((a6==0)and(b6==2)):
    game[1][1]=0
    game[2][0]=2 #win 64
    app(64)
    return game
   
    #2 4 0
    #1 6 0
    #0 0 5
  elif((a1==1)and(b1==1))and((a2==0)and(b2==0))and(a3==-1)and((a4==0)and(b4==1))and((a5==2)and(b5==2))and((a6==1)and(b6==1)):
    u=random.uniform(0,1)
    if u<=movevalue[64]:
      game[0][1]=0
      game[1][0]=4 #65
      app(65)
    else:
      game[1][1]=0
      game[2][1]=6 #win 66
      app(66)
    return game

    #2 0 0
    #4 5 0
    #0 0 0
  elif(a1==-1)and((a2==0)and(b2==0))and(a3==-1)and((a4==1)and(b4==0))and((a5==1)and(b5==1))and(a6==-1):
    game[1][0]=0
    game[2][0]=4 #win 67
    app(67)
    return game

    #2 0 0
    #4 6 5
    #0 0 0
  elif(a1==-1)and((a2==0)and(b2==0))and(a3==-1)and((a4==1)and(b4==0))and((a5==1)and(b5==2))and((a6==1)and(b6==1)):
    game[1][0]=0
    game[2][0]=4 #win 68
    app(68)
    return game

    #2 4 0
    #0 1 0
    #0 0 5
  elif((a1==1)and(b1==1))and((a2==0)and(b2==0))and(a3==-1)and((a4==0)and(b4==1))and((a5==2)and(b5==2))and(a6==-1):
    u=random.uniform(0,1)
    if u<=movevalue[68]:
      game[0][0]=0
      game[1][0]=2 #69
      app(69)
    else:
      game[0][0]=0
      game[1][1]=2 #70
      app(70)
    return game
    
    #0 4 0
    #0 2 5
    #0 0 0
  elif(a1==-1)and((a2==1)and(b2==1))and(a3==-1)and((a4==0)and(b4==1))and((a5==1)and(b5==2))and(a6==-1):
    game[0][1]=0
    game[1][2]=4 #win 71
    app(71)
    return game

    #0 4 0
    #2 1 5
    #0 0 0
  elif((a1==1)and(b1==1))and((a2==1)and(b2==0))and(a3==-1)and((a4==0)and(b4==1))and((a5==1)and(b5==2))and(a6==-1):
    u=random.uniform(0,1)
    if u<=movevalue[71]:
      game[1][0]=0
      game[2][0]=2 #win 72
      app(72)
    else:
      game[0][1]=0
      game[1][2]=4 #p wins 73
      app(73)
    return game
    
    #2 4 0
    #0 5 0
    #1 0 0
  elif((a1==2)and(b1==0))and((a2==0)and(b2==0))and(a3==-1)and((a4==0)and(b4==1))and((a5==1)and(b5==1))and(a6==-1):
    u=random.uniform(0,1)
    if u<=movevalue[73]:
      game[0][0]=0
      game[1][0]=2 #74
      app(74)
    else:
      game[0][0]=0
      game[1][1]=2 #75
      app(75)
    return game
    
    #0 4 0
    #1 2 0
    #0 0 0
  elif((a1==1)and(b1==0))and((a2==1)and(b2==1))and(a3==-1)and((a4==0)and(b4==1))and(a5==-1)and(a6==-1):
    game[1][1]=0
    game[2][1]=2 #win 76
    app(76)
    return game
          
    #2 4 0
    #0 6 5
    #1 0 0
  elif((a1==2)and(b1==0))and((a2==0)and(b2==0))and(a3==-1)and((a4==0)and(b4==1))and((a5==1)and(b5==2))and((a6==1)and(b6==1)):
    u=random.uniform(0,1)
    if u<=movevalue[76]:
      game[0][0]=0
      game[1][0]=2 #77
      app(77)
    elif u<=movevalue[77]:
      game[1][1]=0
      game[2][1]=6 #78
      app(78)
    else:
      game[0][1]=0
      game[1][2]=4 #79
      app(79)
    return game
    
    #0 4 0
    #2 1 5
    #0 0 0
  elif((a1==1)and(b1==1))and((a2==1)and(b2==0))and(a3==-1)and((a4==0)and(b4==1))and((a5==1)and(b5==2))and(a6==-1):
    u=random.uniform(0,1)
    if u<=movevalue[79]:
      game[1][0]=0
      game[2][0]=2 #80
      app(80)
    else:
      game[0][1]=0
      game[1][2]=4 #81
      app(81)
    return game
         
    #2 0 0 
    #1 6 4
    #0 0 0
  elif((a1==1)and(b1==0))and((a2==0)and(b2==0))and(a3==-1)and((a4==1)and(b4==2))and(a5==-1)and((a6==1)and(b6==1)):
    game[1][1]=0
    game[2][1]=6 #82
    app(82)
    return game
 
    #2 0 0
    #0 1 4
    #0 0 0
  elif((a1==1)and(b1==1))and((a2==0)and(b2==0))and(a3==-1)and((a4==1)and(b4==2))and(a5==-1)and(a6==-1):
    u=random.unifrom(0,1)
    if u<=movevalue[82]:
      game[0][0]=0
      game[1][0]=2 #83
      app(83)
    elif u<=movevalue[83]:
      game[0][0]=0
      game[1][1]=2 #84
      app(84)
    else:
      game[1][2]=0
      game[2][2]=4 #85
      app(85)
    return game
     
    #2 4 0
    #1 3 6
    #0 0 5
  elif((a1==1)and(b1==0))and((a2==0)and(b2==0))and((a3==1)and(b3==1))and((a4==0)and(b4==1))and((a5==2)and(b5==2))and((a6==1)and(b6==2)):
    u=random.uniform(0,1)
    if u<=movevalue[85]:
      game[0][0]=0
      game[1][1]=2 #86
      app(86)
    else:
      game[0][1]=0
      game[1][0]=4 #87
      app(87)
    return game
        
    #0 4 0
    #1 5 6
    #0 0 0
  elif((a1==1)and(b1==0))and(a2==-1)and(a3==-1)and((a4==0)and(b4==1))and((a5==1)and(b5==1))and((a6==1)and(b6==2)):
      u=random.uniform(0,1)
      if u<=movevalue[87]:
        game[0][1]=0
        game[1][0]=4 #88
        app(88)
      else:
        game[1][2]=0
        game[2][2]=6 #89
        app(89)
      return game
      
      #2 0 0
      #4 5 6
      #0 0 0
  elif(a1==-1)and((a2==0)and(b2==0))and(a3==-1)and((a4==1)and(b4==0))and((a5==1)and(b5==1))and((a6==1)and(b6==2)):
    u=random.uniform(0,1)
    if u<=movevalue[89]:
      game[0][0]=0
      game[1][1]=2 #90
      app(90)
    else:
      game[1][0]=0
      game[2][0]=4 #91
      app(91)
    return game
            
    #2 0 6
    #0 1 5
    #0 3 0
  elif((a1==1)and(b1==1))and((a2==0)and(b2==0))and((a3==2)and(b3==1))and(a4==-1)and((a5==1)and(b5==2))and((a6==0)and(b6==2)):
    u=random.uniform(0,1)
    if u<=movevalue[91]:
      game[0][0]=0
      game[1][0]=2 #92
      app(92)
    elif u<=movevalue[92]:
      game[0][0]=0
      game[1][1]=2 #93
      app(93)
    else:
      game[0][2]=0
      game[1][1]=6 #94
      app(94)
    return game
            
    #0 0 6
    #3 1 5
    #0 0 0
  elif((a1==1)and(b1==1))and(a2==-1)and((a3==1)and(b3==0))and(a4==-1)and((a5==1)and(b5==2))and((a6==0)and((b6==2))):
    game[0][2]=0
    game[1][1]=6 #95
    app(95)
    return game
            
    #2 0 6
    #1 0 4
    #0 3 0
  elif((a1==1)and(b1==0))and((a2==0)and(b2==0))and((a3==2)and(b3==1))and((a4==1)and(b4==2))and(a5==-1)and((a6==0)and(b6==2)):
      game[1][2]=0
      game[2][2]=4 #96
      app(96)
      return game

    #2 0 6
    #0 3 4
    #1 0 0
  elif((a1==2)and(b1==0))and((a2==0)and(b2==0))and((a3==1)and(b3==1))and((a4==1)and(b4==2))and(a5==-1)and((a6==0)and(b6==2)):
    u=random.uniform(0,1)
    if u<=movevalue[96]:
      game[1][2]=0
      game[2][2]=5 #97
      app(97)
    elif u<=movevalue[97]:
      game[0][0]=0
      game[1][0]=2 #98
      app(98)
    elif u<=movevalue[98]:
      game[0][0]=0
      game[1][1]=2 #99
      app(99)
    else:
      game[1][2]=0
      game[2][2]=4 #100
      app(100)
    return game
            
    #2 0 0
    #0 1 4
    #0 0 0
  elif((a1==1)and(b1==1))and((a2==0)and(b2==0))and(a3==-1)and((a4==1)and(b4==2))and(a5==-1)and(a6==-1):
    game[1][2]=0
    game[2][2]=4 #101
    app(101)
    return game
            
    #0 0 6
    #1 2 4
    #0 0 0
  elif((a1==1)and(b1==0))and(a2==-1)and(a3==-1):
    game[1][1]=0
    game[2][1]=2 #102
    app(102)
    return game
            
    #0 0 6
    #0 1 4
    #0 0 0
  elif((a1==1)and(b1==1))and(a2==-1)and(a3==-1)and((a4==1)and(b4==2))and(a5==-1)and((a6==0)and(b6==2)):
    game[0][2]=0
    game[1][1]=6 #103
    app(103)
    return game
            
    #2 0 6
    #0 0 3
    #1 0 0
  elif((a1==2)and(b1==0))and((a2==0)and(b2==0))and((a3==1)and(b3==2))and(a4==-1)and(a5==-1)and((a6==0)and(b6==2)):
    game[0][0]=0
    game[1][0]=2 #104
    app(104)
  return game
  
def Check(game,line,column,pawn):#0-нельзя так ходить 1-можно
  #position of pawn and what pawn
  for i in range(len(game)):
    for j in range(len(game[i])):
      if game[i][j]==pawn:
        a=i
        b=j
        break
#out play
  if (line==-1 or line==3)or(column==-1 or column==3):
    print("c1")
    return 0
#diagonal play for player
  if (line<a) and (column!=b):
    print("c2")
    if (b-column==1 or column-b==1) and (a-line==1):
      if (game[line][column]==2) or (game[line][column]==4) or (game[line][column]==6):
        return 1
      else:
        return 0
    else:
        return 0
#diagonal play for machine
  if (line>a) and ((column<b) or (column>b)):
    print("c3")
    if (b-column==1 or column-b==1) and (line-a==1):
      if (game[line][column]==1) or (game[line][column]==3) or (game[line][column]==5):
        return 1
      else:
        return 0
    else:
        return 0
#front play for player
  if (a-line==1)and(column==b):
    print("c4")
    if game[line][column]==0:
      return 1
    else:
      return 0
#front play for machine
  if (line-a==1)and(column==b):
    print("c5")
    if game[line][column]==0:
      return 1
    else:
      return 0
      
  return 1
  
def Win(game,whose_move): #2 p wins 1 m wins 0 nobody                  whose_move=1 player's turn whose_move=2 machine's turn
  a1 =-1; a2 =-1; a3 =-1; a4 =-1; a5 =-1; a6 =-1; count=0
  for v in range(1,7):
    for i in range(len(game)):
      for j in range(len(game[i])):
        if game[i][j]==v:
          if v==1:
            a1=i; b1=j
          elif v==2:
            a2=i; b2=j
          elif v==3:
            a3=i; b3=j
          elif v==4:
            a4=i; b4=j
          elif v==5:
            a5=i; b5=j
          elif v==6:
            a6=i; b6=j

  if a1==0 or a3==0 or a5==0:
    return 2
  elif a2==2 or a4==2 or a6==2:
    return 1
    
  if (a1==-1)and(a3==-1)and(a5==-1):
    return 1
  elif(a2==-1)and(a4==-1)and(a6==-1):
    return 2

  if whose_move==1:
    if a1!=-1:
      for a in range(-1,2):
        x=Check(game,a1-1,b1+a,1)
        if x!=0:
          return 0
      count=1
    else:
      count=1

    if a3!=-1:
      for a in range(-1,2):
        x=Check(game,a3-1,b3+a,3)
        if x!=0:
          return 0
      count=2
    else:
      if count==1:
        count==2

    if a5!=-1:
      for a in range(-1,2):
        x=Check(game,a5-1,b5+a,5)
        if x!=0:
          return 0
      count=3
    else:
      if count==2:
        count=3

  if count==3:
    return 1
    
  if whose_move==2:
    if a2!=-1:
      for a in range(-1,2):
        x=Check(game,a2+1,b2+a,2)
        if x!=0:
          return 0
      count=-1
    else:
      count=-1

    if a4!=-1:
      for a in range(-1,2):
        x=Check(game,a4+1,b4+a,4)
        if x!=0:
          return 0
      if count==-1:
        count=-2
    else:
      if count==-1:
        count=-2

    if a6!=-1:
      print("21")
      for a in range(-1,2):
        x=Check(game,a6+1,b6+a,6)
        if x!=0:
          return 0
      if count==-2:
        count=-3
    else:
      if count==-2:
        count=-3

  if count==-3:
    return 2
  return 0
  
def Hexapawn():
  game=Reset()
  count=0
  game1=0
  while 1:
    while (game1==0)or(count==0):
      Hprint(game)
      print("Enter pawn(1,3,5) column (1-3) and line (1-3): ")
      x=int(input())
      a=int(input())-1
      b=int(input())-1
      count=Existpawn(x,game)
      game1=Playermove(game,b,a,x)
      Hprint(game1)

      if (game1==0)or(count==0):
        print("Try again\n")
      else:
        game=game1
        win=Win(game,2)
        if win == 1 or win == 2:
          game=Reset()
          if win==1:
            change()
            move=[]
            print("Machine Wins\n")
            print(movevalue)
          elif win==2:
            print("Player Wins\n")
          continue

    print("Machine's turn\n")
    game=Machineplay(game)
    Hprint(game)
    count=0
    game1=0
    win=Win(game,1)
    if win == 1 or win == 2:
      game=Reset()
      if win==1:
        change()
        move=[]
        print("Machine Wins\n")
        print(movevalue)
      else:
        print("Player Wins\n")
      
