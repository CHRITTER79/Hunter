import random

name = "John"
question = "Will I be cool"
answer = ""

random_number = random.randint(1, 9)

if random_number == 1:
  answer = "yes no oh wait yes uh hold on No"
elif random_number == 2:
  answer = "Shut up"
elif random_number == 3:
  answer = "Of course Sike loser LOL"
elif random_number == 4:
  answer = "Go Away"
elif random_number == 5:
  answer = "Ask again never"
elif random_number == 6:
  answer = "Yeah Yeah whatever you say hold on i'm checking my snapchats"
elif random_number == 7:
  answer = "Ugh sure bud"
elif random_number == 8:
  answer = "MHM"
elif random_number == 9:
  answer = "Pfft uh no in your dreams bozo"
else:
  answer = ""
  
print(name + " asks: " + question)
print("Hunter's  answer: " + answer)

