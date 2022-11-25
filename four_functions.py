input = int(input("Enter the number: "))

def functionHadArgumentHadReturn(parameter):
    return parameter + 1

def functionNoArgumentHadReturn():
    return input + 1

def functionHadArgumentNoReturn(parameter):
    print(parameter + 1)

def functionNoArgumentNoReturn():
    print(input + 1)

print(functionHadArgumentHadReturn(input))
functionHadArgumentNoReturn(input)
print(functionNoArgumentHadReturn())
functionNoArgumentNoReturn()