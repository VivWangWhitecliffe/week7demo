class Calculator:
    @staticmethod
    def add(x, y):
        """Add two numbers.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The result of the addition.
        """
        return x + y

    @staticmethod
    def subtract(x, y):
        """Subtract y from x.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The result of the subtraction.
        """
        return x - y

    @staticmethod
    def multiply(x, y):
        """Multiply two numbers.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The result of the multiplication.
        """
        return x * y

    @staticmethod
    def divide(x, y):
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
            return x / y

        raise ValueError("Cannot divide by zero")



