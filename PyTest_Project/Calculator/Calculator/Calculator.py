
# Function to add two numbers
class Calculator:

    def add(self,num1, num2):
       return num1+num2

    # Function to subtract two numbers
    def subtract(self,num1,num2):
        return num1 - num2

    # Function to multiply two numbers
    def multiply(self, num1, num2):
        return num1 * num2

    # Function to divide two numbers
    def divide(self,num1, num2):
        try:
            return(round(num1/num2,2))
        except ZeroDivisionError as e:
            return "Infinity"
