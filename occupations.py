import random

OCUPATIONES = {}
occupashuns = open("occupations.csv", "rU")

occupashuns.readline()
for line in occupashuns:
    if line[0] == "\"":
        #i sincerely apologize for the next line
        OCUPATIONES[line[1:line.find("\"", 1, (len(line) + 1))].strip("\n")] = line[line.find(",", line.find("\"", 1, (len(line) + 1)), (len(line))) + 1:len(line)].strip("\n")
    else:
        x = line.split(",")
        OCUPATIONES[x[0].strip("\n")] = x[1].strip("\n")
del OCUPATIONES['Total']

    
def randomizer():
    percentz = OCUPATIONES.values()
    #THE CHEATY WAY
    #percentz = sorted(percentz, key=float)
    for i in range(0, len(percentz)):
        percentz[i] = float(percentz[i])
    percentz.sort()
    ranges = []
    total = 0
    for i in range(0, len(percentz)):
        total += percentz[i]
        ranges.append(total)
    for i in range(0, len(percentz)):
        percentz[i] = str(percentz[i])
    randnumba = random.random() * total
    randrange = 0
    for i in range(0, len(ranges)):
        if (randnumba < ranges[i]):
            randrange = i
            break
    return OCUPATIONES.keys()[i] + ", " + percentz[i] + "%"


print randomizer()
