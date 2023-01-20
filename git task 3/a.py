f = open("travels.txt", "r")
lines = f.read().split("\n")
x = {
}
b = 0
c = 0
d = {}
e = {}
count=0
prev_day = 1
mass_sum = 0
for line in lines:
    line_arr = line.split(" ")
    day = int(line_arr[0])
    mass = int(line_arr[6])
    From = line_arr[2]
    to = line_arr[3]
    path = int(line_arr[4])
    fuel = int(line_arr[5])

    if (day != prev_day):
        x[prev_day] = mass_sum
        count = 0
        prev_day = day
        mass_sum = 0
    count+=1
    mass_sum+=mass

    if (day == 1):
        c+=path

    if (line_arr[2] == "Липки"):
        b+=mass

    if (not From in d.keys()):
        d[From] = 0
    d[From]+=mass

    if (not to in e.keys()):
        e[to] = {"mass":0, "fuel":0, "count":0}
    e[to]["mass"]+=mass
    e[to]["count"]+=1
    e[to]["fuel"]+=fuel

x[prev_day] = mass_sum

f.close()
print(x)
print(b)
print(c)
print(len(d))
for a, b in d.items():
    print(a, b)

print(len(e))
max_fuel = 0
max_fuel_name = 0
for a, b in e.items():
    if (b["fuel"]/b["count"] > max_fuel):
        max_fuel = b["fuel"]/b["count"]
        max_fuel_name = a
    print(a, b["mass"])

print()
print(max_fuel_name, max_fuel)