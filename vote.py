try:
  age = int(int("enter your age:"))
  if age >= 18:
    print("you eligible")
  else:
    print("you not eligible")
except ValueError:
  print ("please enter a valid integer for age.")
