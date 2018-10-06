def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


keyWord = ['abstract', 'args', 'assert', 'break', 'switch', 'case', 'try', 'catch', 'finally', 'class', 'continue', 'default', 'do', 'if', 'else', 'enum', 'extends', 'final', 'for', 'implements', 'imports', 'instanceOf', 'interface', 'main', 'native', 'new', 'package', 'private', 'protected', 'public', 'return', 'static', 'strictfp', 'super', 'syncronized', 'this', 'throw', 'throws', 'transient', 'void', 'volatile', 'while', 'goto', 'const', 'true', 'false']
variables = ["boolean", "byte", "char", "short", "int", "long", "float", "double", "String"]
mathOperator = ["+", "-", "/", "*", "=", "^", "%"]
logicalOperator = ["<", ">", "<=", ">=", "==", "!", "||", "&&"]
other = ["(", ")", "{", "}", ",", "?", "\"", "'", ";", ".", ":", "[", "]"]

identifierOutput = []
keyWordsOutput = []
mathOperatorOutput = []
logicalOperatorOutput = []
numericOutput = []
otherOutput = []


file = open("input.txt")
input = file.read()

isVariable = 1
isComma = 1



for word in input.split():

    if word[0] in other :
        if word[0] not in otherOutput :
            otherOutput.append(word[0])
        word = word.replace(word[0], '', 1)

    if len(word) == 0 :
        continue

    if word[len(word) - 1] in other:
        if word[len(word) - 1] == ",":
            isComma = 2
        else:
            isComma = 1
        if word[len(word) - 1] not in otherOutput:
            otherOutput.append(word[len(word) - 1])
        c = word[len(word) - 1]
        word = word.replace(word[len(word) - 1], '', 1)


    if isVariable == 2  and word not in identifierOutput :
        identifierOutput.append(word)

        if isComma == 1:
            isVariable = 1
		
        continue


    if word in variables :
        isVariable = 2
        if word not in keyWordsOutput :
            keyWordsOutput.append(word)

    elif word in keyWord :
        if word not in keyWordsOutput :
            keyWordsOutput.append(word)

    elif word in mathOperator :
        if word not in mathOperatorOutput :
            mathOperatorOutput.append(word)

    elif word in logicalOperator :
        if word not in logicalOperatorOutput :
            logicalOperatorOutput.append(word)

    elif word.isnumeric() or isFloat(word):
        if word not in numericOutput :
            numericOutput.append(word)

    elif word in identifierOutput :
        continue


print("Identifier: ")
print(identifierOutput)

print("Keywords: ")
print(keyWordsOutput)

print("Math Operators: ")
print(mathOperatorOutput)

print("Logical Operator: ")
print(logicalOperatorOutput)

print("Numeric values: ")
print(numericOutput)

print("Other: ")
print(otherOutput)


