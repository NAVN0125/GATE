class upper:
    def __init__(self, string):
        self.string = string

    def upperCase(self):
        print(self.string.upper())

p = upper(input("Enter a string: "))
p.upperCase()