class CustomizedInteger:
    def __init__(self, integer):
        self.integer = integer

    def __str__(self):
        return f"Customized Integer {self.integer}"


int1 = CustomizedInteger(4)

print(int1)
