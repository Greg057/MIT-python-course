s = 'azcbobobegghakl'
num = 0

for i in range(len(s)): 
    if s[i] == "b" and i < len(s) - 2:
        if s[i + 1] == "o" and i < len(s) - 1:
            if s[i + 2] == "b":
                num += 1

print("Number of times bob occurs is:", num)