import players as p

def Game(Player1Looks:str = "x",Player2Looks:str = "o",EmptySpotLooks:str = "-",TieLooks:str = "t",showPrint:bool = True):
  game = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]] ## 0: nothing    1: circle    2: cross
  gameON = True
  round = 0
  currentPlayer = 1
  player1 = [0,0]
  player2 = 0

  def tick():
    if showPrint:
      print(f"round: {round}    player {currentPlayer}'s turn")
      if currentPlayer == 1:
        if round == 1 or len(game[player2-1]) != 9:
          print(f"player 1: changed cell {player1[1]} in quadrant(choosable) {player1[0]}")
        else:
          print(f"player 1: changed cell {player1} in quadrant {player2}")
      else:
        if len(game[player1-1]) != 9:
          print(f"player 1: changed cell {player2[1]} in quadrant(choosable) {player2[0]}")
        else:
          print(f"player 2: changed cell {player2} in quadrant {player1}")
    state = checkGame()
    if showPrint:
      terraToe = [0,0,0,0,0,0,0,0,0]
      for i in range(9):
        if len(game[i]) != 9:
          terraToe[i] = game[i][9]
      for j in range(3):
        for i in range(3):
          if terraToe[i+j*3] == 0:
            print(EmptySpotLooks,end=" ")
          elif terraToe[i+j*3] == 1:
            print(Player1Looks,end=" ")
          elif terraToe[i+j*3] == 2:
            print(Player2Looks,end=" ")
          elif terraToe[i+j*3] == -1:
            print(TieLooks,end=" ")
        print("")
      print("")
      for b in range(3):
        for a in range(3):
          for i in range(3):
            for j in range(3):
              if game[i+b*3][j+a*3] == 0:
                print(EmptySpotLooks,end=" ")
              elif game[i+b*3][j+a*3] == 1:
                print(Player1Looks,end=" ")
              elif game[i+b*3][j+a*3] == 2:
                print(Player2Looks,end=" ")
            print("  ",end="")
          print("")
        print("")
    if state == 1:
      if showPrint:
        print("Player 1 win")
      return 1
    elif state == 2:
      if showPrint:
        print("Player 2 win")
      return 2
    elif state == -1:
      if showPrint:
        print("tie")
      return 0

  def checkGame():
    for i in range(9):
      if len(game[i]) == 9:
        if [1,1,1] in [game[i][:3],game[i][3:6],game[i][6:]]:
          game[i].append(1)

        elif [2,2,2] in [game[i][:3],game[i][3:6],game[i][6:]]:
          game[i].append(2)

        elif (game[i][0] == 1 and game[i][3] == 1 and game[i][6] == 1) or (game[i][1] == 1 and game[i][4] == 1 and game[i][7] == 1) or (game[i][2] == 1 and game[i][5] == 1 and game[i][8] == 1):
          game[i].append(1)

        elif (game[i][0] == 2 and game[i][3] == 2 and game[i][6] == 2) or (game[i][1] == 2 and game[i][4] == 2 and game[i][7] == 2) or (game[i][2] == 2 and game[i][5] == 2 and game[i][8] == 2):
          game[i].append(2)

        elif (game[i][0] == 1 and game[i][4] == 1 and game[i][8] == 1) or (game[i][2] == 1 and game[i][4] == 1 and game[i][6] == 1):
          game[i].append(1)

        elif (game[i][0] == 2 and game[i][4] == 2 and game[i][8] == 2) or (game[i][2] == 2 and game[i][4] == 2 and game[i][6] == 2):
          game[i].append(2)

        elif not 0 in game[i]:
          game[i].append(-1)

    
    overall = [0,0,0,0,0,0,0,0,0]
    for i in range(9):
      if len(game[i]) != 9:
        overall[i] = game[i][9]
    
    if [1,1,1] in [overall[:3],overall[3:6],overall[6:]]:
      return 1
    elif [2,2,2] in [overall[:3],overall[3:6],overall[6:]]:
      return 2
    elif (overall[0] == 1 and overall[3] == 1 and overall[6] == 1) or (overall[1] == 1 and overall[3] == 1 and overall[7] == 1) or (overall[2] == 1 and overall[5] == 1 and overall[8] == 1):
      return 1
    elif (overall[0] == 2 and overall[3] == 2 and overall[6] == 2) or (overall[1] == 2 and overall[3] == 2 and overall[7] == 2) or (overall[2] == 2 and overall[5] == 2 and overall[8] == 2):
      return 2
    elif (overall[0] == 1 and overall[4] == 1 and overall[8] == 1) or (overall[2] == 1 and overall[4] == 1 and overall[6] == 1):
      return 1
    elif (overall[0] == 2 and overall[4] == 2 and overall[8] == 2) or (overall[2] == 2 and overall[4] == 2 and overall[6] == 2):
      return 2
    elif not 0 in overall:
      return -1
    return 0

  ################################### players
  def p1(a,choose,which):
    return p.user(a,choose,which)

  def p2(b,choose,which):
    return p.rand(b,choose,which)
  ###################################

  tick()
  while gameON:

    round += 1
    if round == 1:
      currentPlayer = 1
      player1 = p1(game,True,0)
      game[player1[0]-1][player1[1]-1] = 1
      tick()
      player1 = player1[1]
      currentPlayer = 2
      player2 = p2(game,False,player1)
      game[player1-1][player2-1] = 2
      state = tick()
    else:
      currentPlayer = 1
      if len(game[player2-1]) != 9:
        player1 = p1(game,True,0)
        game[player1[0]-1][player1[1]-1] = 1
        state = tick()
        player1 = player1[1]
      else:
        player1 = p1(game,False,player2)
        game[player2-1][player1-1] = 1
        state = tick()
      if state in [0,1,2]:
        return state
        break

      currentPlayer = 2
      if len(game[player1-1]) != 9:
        player2 = p2(game,True,0)
        game[player2[0]-1][player2[1]-1] = 2
        state = tick()
        player2 = player2[1]
      else:
        player2 = p2(game,False,player1)
        game[player1-1][player2-1] = 2
        state = tick()
      if state in [0,1,2]:
        return state
        break
  
def GraphWin(iterations:int,showPrint:bool = True):
  p1Win = 0
  p2Win = 0
  tie = 0
  for i in range(iterations):
    out = Game("0","1","2","t",False)
    if out == 1:
      p1Win+=1
    elif out == 2:
      p2Win+=1
    else:
      tie+=1
  if showPrint:
    print(f"Player 1 won {p1Win} times {int(p1Win/iterations*1000)/10}%")
    print(f"Player 2 won {p2Win} times {int(p2Win/iterations*1000)/10}%")
    print((f"The game tied {tie} times {int(tie/iterations*1000)/10}%"))
  return [p1Win,p2Win,tie]

Game()
