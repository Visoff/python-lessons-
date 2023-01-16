res = []
f = open("Perepis.txt", "r")
lines = f.read().split("\n")
for line in lines:
    if (int(line.split('  ')[3].split(".")[2]) < 1978):
        res.append(line)
f.close()
print("\n".join(res))