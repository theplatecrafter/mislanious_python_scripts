import random as r

def controledInput(type:str = "float",prompt:str = "",rePrompt:bool=True,invalidTXT:str="Invalid input"):
  """"this only supports float and int controled input. When rePrompt is set to true, it will keep on prompting for the correct answer. invalidTXT is the text that appears when rePrompt is true, and the user inputed a wrong value. numMin <= <userinput> <= numMax This will return "" when rePrompt is False and the user inputs an invalid input."""
  if rePrompt:
    while True:
      user_input = input(prompt)
      try:
        if type == "float":
          user_input = float(user_input)
          return user_input
        elif type == "int":
          user_input = int(user_input)
          return user_input
      except ValueError:
        print(invalidTXT)
  else:
    user_input = input(prompt)
    try:
      if type == "float":
        user_input = float(user_input)
        return user_input
      elif type == "int":
        user_input = int(user_input)
        return user_input
    except ValueError:
      return ""

def rand(gameState,choose,which):
  if choose:
    terraToe = [0,0,0,0,0,0,0,0,0]
    for i in range(9):
      if len(gameState[i]) != 9:
        terraToe[i] = gameState[i][9]
    
    quad = r.randint(1,9)
    while terraToe[quad-1] != 0:
      quad = r.randint(1,9)
    
    cell = r.randint(1,9)
    while gameState[quad-1][cell-1] != 0:
      cell = r.randint(1,9)
    
    return [quad,cell]
  else:
    output = r.randint(1,9)
    while gameState[which-1][output-1] != 0:
      output = r.randint(1,9)
    return output

def user(gameState,choose,which):
  if choose:
    terraToe = [0,0,0,0,0,0,0,0,0]
    for i in range(9):
      if len(gameState[i]) != 9:
        terraToe[i] = gameState[i][9]
    
    quad = int(controledInput("int","select quadrant (1~9): "))
    while not (quad >=1 and quad <= 9 and terraToe[quad-1] == 0):
      print("Invalid Input: select a diffrent quadrant")
      quad = int(controledInput("int","select quadrant (1~9): "))
    
    cell = int(controledInput("int","select cell (1~9): "))
    while not (cell >=1 and cell <= 9 and gameState[quad-1][cell-1] == 0):
      print("Invalid Input: select a diffrent cell")
      cell = int(controledInput("int","select cell (1~9): "))
    return [quad,cell]
  else:
    cell = int(controledInput("int",f"select cell (1~9) in quadrant {which}: "))
    while not (cell >=1 and cell <= 9 and gameState[which-1][cell-1] == 0):
      print("Invalid Input")
      cell = int(controledInput("int",f"select cell (1~9) in quadrant {which}: "))
    return cell