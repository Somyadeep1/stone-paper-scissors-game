rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("0 for rock, 1 for paper, 2 for scissors")
user_input=int(input("Enter your choice: \n"))
coum_input=random.randint(0,2)
x=[rock,paper,scissors]
if user_input==coum_input:
  print(f"You chose {x[user_input]}")
  print(f"Computer chose {x[coum_input]}")
  print("Draw-----Try again")
elif user_input==0 and coum_input==1:
  print(f"You chose {x[user_input]}")
  print(f"Computer chose {x[coum_input]}")
  print("You lose")
elif user_input==0 and coum_input==2:
  print(f"You chose {x[user_input]}")
  print(f"Computer chose {x[coum_input]}")
  print("You Win")
elif user_input==1 and coum_input==0:
  print(f"You chose {x[user_input]}")
  print(f"Computer chose {x[coum_input]}")
  print("You Win")
elif user_input==1 and coum_input==2:
  print(f"You chose {x[user_input]}")
  print(f"Computer chose {x[coum_input]}")
  print("You lose")
elif user_input==2 and coum_input==0:
  print(f"You chose {x[user_input]}")
  print(f"Computer chose {x[coum_input]}")
  print("You lose")
elif user_input==2 and coum_input==1:
  print(f"You chose {x[user_input]}")
  print(f"Computer chose {x[coum_input]}")
  print("You Win")
