import random


optinal_choises = ["rock", "paper", "scissors"]
def get_choises():
    player_input = input( "chose (rock, paper, scissors )\n")
    player_choise = player_input.strip().lower()
    

    computer_choise = random.choice(optinal_choises)
    choises = {"player": player_choise , "computer" :computer_choise}
   
    return choises
  
def validate(a):
  return True if a in(optinal_choises) else False

  
    
def check_win(pc , cc):
   
    
    if pc  == cc:
        return "its a tie"
    
    if pc == optinal_choises[0]:#check when rock
        if cc == optinal_choises[1]:
          return "Paper covers Rock, You lose"
        if cc == optinal_choises[2]:
            return "Rock smashes scissors, You win!"
        
    if pc == optinal_choises[1]: #paper
        if cc == optinal_choises[2]:
          return "Scissors cuts Paper, You lose"
        if cc == optinal_choises[0]:
            return "Paper covers Rock, You win!"   
        
    if pc == optinal_choises[2]:
        if cc == optinal_choises[0]:
          return "Rock smashes scissors, You lose"
        if cc == optinal_choises[1]:
            return "Scissors cuts Paper, You win!"  
        
        
        
        

    
    
    
    
 

while True:
    choise = get_choises()
    if not validate(choise["player"]):
      print("invalid choise")
      continue
    print(f"computer chose ,{choise["computer"]}")
    print (check_win(choise["player"],choise["computer"]))
    




