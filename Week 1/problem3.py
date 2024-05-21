s = 'azcbobobegghakl'

subString = ""
tempString = s[0]
lengthTemp = 0

for i in range(len(s) - 1):
    if s[i + 1] >= s[i]:
        tempString += s[i + 1]
    else:
        if len(tempString) > lengthTemp:
            subString = tempString
            lengthTemp = len(tempString)
        tempString = s[i + 1]

if len(subString) == 0:
    subString = tempString

print("Longest substring in alphabetical order is:", subString)