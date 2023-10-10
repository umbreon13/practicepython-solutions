# error checking

# already done in exercise 9

#try/catch structure
# try to execute the code, if there's nothing wrong, the program keeps going
  #  if there is something wrong (eg. intro a string instead of an int) the catch section is executed
try:
	guess = int(input("Guess a number between 1 and 9: "))
	print(f"You entered {guess}")
except ValueError:
	print("ValueError is thrown")
	

# another way:
guess = int(input("Guess a number between 1 and 9: "))
if guess < 1 or guess > 9:
	print("Guess again!")