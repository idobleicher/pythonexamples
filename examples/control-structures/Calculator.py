while True:
   print("Options:")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'quit' to end the program")
   user_input = input(": ")

   if user_input == "quit":
      break
   elif user_input == "add":
       #As it is, this code crashes if the user enters a non-numeric input when prompted to  enter a number.
       #  We will look at fixing problems like this in a later module
       num1 = float(input("Enter a number: "))
       num2 = float(input("Enter another number: "))
       result = str(num1 + num2)
       print("The answer is " + result)
   elif user_input == "subtract":
       print("subtract")
   elif user_input == "multiply":
       print("multiply")
   elif user_input == "divide":
       print("divide")
   else:
      print("Unknown input")