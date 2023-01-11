def range(secret_number):
  lower, higher = secret_number - 13, secret_number + 13
  
  if secret_number <=15: 
    print("The secret number is less than", higher)
  elif 15 < secret_number < 83:
    print(f"The number is in between: {lower} and {higher}")
  else: 
    print(f"The number is greater than {lower}")


