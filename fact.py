
#This program calculates the factorial of a given number

def factorial(num):
    '''This function calculates the factorial of a number'''
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def factorial_without_recursion(number):
    fact = 1
    while(number > 0):
        fact = fact * number
        number = number - 1
    print('Factorial of', number,'is: ')
    print(fact)

if __name__ == '__main__':
    userInput = int(input('Enter the number to find its factorial: '))
    print('Factorial of', userInput, 'is:', factorial(userInput))
    factorial_without_recursion(userInput)