# Create Function to get the choice 
def getChoices():
  player_choice = input('Enter a choice :')
  computer_choice = 'paper'
  choices = {"Player": player_choice, "Computer":     computer_choice}
  return choices
  
choices = getChoices()
print(choices)