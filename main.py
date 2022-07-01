from replit import clear
from art import logo
print(logo)

def add(n1, n2):
  return n1 + n2

def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide,
}
def calculator():
  first_number = float(input("What's yout first number? "))
  
  for operator in operations:
    print(operator)
  
  should_continue = True
  
  while should_continue:
    ask_operator = input("Pick an operator: ")
    second_number = float(input("What's yout seconde number? "))
    
    calculation_function = operations[ask_operator]
    answer = calculation_function(first_number, second_number)
    
    print(f"{first_number} {ask_operator} {second_number} = {answer}")

    ask_to_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y'
  
    if ask_to_continue:
      first_number = answer
    else:
      print("--------------")
      print ("New calculation")
      should_continue = False
      clear()
      calculator()

calculator()
