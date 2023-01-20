f = open("travels.txt", "r")
lines = f.read().split("\n")
for line in lines:
    print(line.split(" "))
    line = f.readline()
f.close()