class Calculator:
    def __init__(self) -> None:
        self.result=0
    def add(self,x, y):
        """Add two numbers.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The result of the addition.
        """
        self.result=x+y
        return self.result

    def subtract(self,x, y):
        """Subtract y from x.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The result of the subtraction.
        """
        self.result=x-y
        return self.result

    def multiply(self,x, y):
        """Multiply two numbers.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The result of the multiplication.

        """
        self.result=x*y
        return x * y


    def divide(self,x, y):
        """Divide x by y.

        Args:
            x (float): The numerator.
            y (float): The denominator.

        Returns:
            float: The result of the division.

        Raises:
            ValueError: If y is zero.
        """
        if y == 0:       
            return("Cannot divide by zero")
        self.result=x/y
        return self.result



