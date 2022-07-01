# Calculator
#Inputs: a, b, op
#Outputs: result

def calc(a, b, op):
    """
    Returns a string like this: a op b = c
    where c is the computed value according to the opeartor
    """

    if op not in '+-/*':
        return 'Please only type one of these characters: "+, -, *, /"!'

    if op == '+':
      
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b))
    if op == '-':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b))
    if op == '*':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b))
    if op == '/':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b))

# Main program
def main():
    # Get input A
    a = int(input('Please type the first number: '))
    # Get input B
    b = int(input('Please type the second number: '))
    # Get input operator
    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "+, -, *, /" : ')
    # Call calc function
    print(calc(a, b, op))
# Call main function
if __name__ == '__main__':
    main()