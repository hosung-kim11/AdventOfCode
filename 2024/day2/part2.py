import os
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

res = 0
with open(file_path, "r") as file:
    for line in file:
        bad = 0
        line = [int(char) for char in line.strip().split()]
        increase = False
        prev = line[0]
        safe = True
        if line[1] > prev:
            increase = True
        for i in range(1, len(line)):
            if increase == True:
                if(line[i] - prev) > 3 or (line[i] - prev) <= 0:
                    bad += 1
                    if(bad > 1):
                        safe = False
                        break
                else:
                    prev = line[i]
            else:
                if (prev - line[i]) > 3 or (prev - line[i]) <= 0:
                    bad += 1
                    if(bad > 1):
                        safe = False
                        break
                else:
                    prev = line[i]
        if safe:
            res += 1

print(res)