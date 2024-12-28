import os
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

res = 0
with open(file_path, "r") as file:
    for line in file:
        line = [int(char) for char in line.strip().split()]
        bad = 0
        safe = True
        increasing = True
        prev = line[0]
        if (prev > line[1]):
            increasing = False

        for i in range (1, len(line)):
            diff = line[i] - prev
            if(increasing):
                if(diff <= 0 or diff > 3):
                    bad += 1
                    if(i == 1 and i < len(line)):
                        if(line[i] > line[i+1]):
                            increasing = False
                    if (bad > 1):
                        safe  = False
                        break
            else:
                if(diff >= 0 or diff < -3):
                    bad += 1
                    if(i == 1 and i < len(line)):
                        if(line[i] > line[i+1]):
                            increasing = True
                    if (bad > 1):
                        safe = False
                        break
            prev = line[i]
        if(safe):
            res += 1
print(res)