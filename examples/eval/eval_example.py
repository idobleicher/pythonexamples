#The eval() method parses the expression passed to this method and runs python expression (code) within the program.

#The syntax of eval() is:
#eval(expression, globals=None, locals=None)

# #expression - this string as parsed and evaluated as a Python expression
# globals (optional) - a dictionary
# locals (optional)- a mapping object. Dictionary is the standard and commonly used mapping type in Python.

x = 1
print(eval('x + 1'))
#2

def calculatePerimeter(l):
  return 4 * l

# Area of Square
def calculateArea(l):
  return l * 1


def calculate(fun_call) :
    for l in range(1, 3):
        if (fun_call == 'calculatePerimeter(l)'):
            print("If length is ", l , ", Perimeter = ", eval(fun_call))
        elif (fun_call == 'calculateArea(l)'):
            print("If length is ", l , ", Area = ", eval(fun_call))
        else:
          print('Wrong Function')
          break


calculate("calculatePerimeter(l)")
calculate("calculateArea(l)")

# If length is  1 , Perimeter =  4
# If length is  2 , Perimeter =  8
# If length is  1 , Area =  1
# If length is  2 , Area =  2
