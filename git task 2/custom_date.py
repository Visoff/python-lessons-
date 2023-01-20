res = []
min = int(input("Минимальный порок: "))
max = int(input("Максимальный порок: "))
f = open("Perepis.txt", "r")
lines = f.read().split("\n")
for line in lines:
    year = int(line.split('  ')[3].split(".")[2])
    if (year < max and year > min):
        res.append(line)
f.close()
print("\n".join(res))