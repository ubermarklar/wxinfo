tempmax = -1000
tempmin = 1000
barmax = -1000
barmin = 1000

r = open("wxlogfile.txt", "r")

for line in r:
    l = line.split(",")
    at = l[0] #date and time
    i = int(l[1]) #incremented counter for the logfile
    t = float(l[2]) #temperature
    b = float(l[3]) #barometric pressure
    if t > tempmax:
        tempmax = t
    if t < tempmin:
        tempmin = t
    if b > barmax:
        barmax = b
    if b < barmin:
        barmin = b

print tempmax
print tempmin
print barmax
print barmin

r.close()
