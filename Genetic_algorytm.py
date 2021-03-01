import math
import random
import copy

print("Genetic Algorithm\n")
chromosomes = {}
phenotype = {}


def chromosomesInput(chromosomes, numberOfChromosomes):
    x = 1
    maximumLength = 0
    while x <= numberOfChromosomes:
        print("Input chromosome number ", x, ":")
        chromosomes[x] = str(input())

        for y in chromosomes[x]:
            if y == "1":
                continue
            if y == "0":
                continue
            else:
                x -= 1
                print("Chromosome must be binary")
                break
        x += 1
    for x in chromosomes:
        if len(chromosomes[x]) >= maximumLength:
            maximumLength = len(chromosomes[x])
    for x in chromosomes:
        if len(chromosomes[x]) != maximumLength:
            for y in range(maximumLength-len(chromosomes[x])):
                chromosomes[x] = "0" + chromosomes[x]


def calculatePhenotype(phenotype, chromosomes, numberOfChromosomes, a, b, c, d):
    x = 1
    while x <= numberOfChromosomes:
        variable = int(chromosomes[x], 2)
        phenotype[x] = float(a * math.pow(variable, 3) +
                             b * math.pow(variable, 2) + c * variable + d)
        x += 1


def drawOfChromosomes(phenotype, chromosomes):
    randomPoint = {}
    tempDict = {}
    point = float(0)

    randomPoint[0] = 0
    for x in phenotype:
        point = point + phenotype[x]
        randomPoint[x] = point
    for x in chromosomes:
        randomNumber = random.uniform(0, int(point))
        for y in chromosomes:
            if float(randomPoint[y-1]) <= float(randomNumber) and float(randomPoint[y]) >= float(randomNumber):
                tempDict[x] = copy.deepcopy(chromosomes[y])
    for x in tempDict:
        chromosomes[x] = copy.deepcopy(tempDict[x])


def chromosomesCrossingOver(chromosomes, pk, numberOfChromosomes):
    y = 1
    for x in range(int(numberOfChromosomes/2)):
        pkRandom = random.uniform(0, 1)
        lokus = random.randint(1, len(chromosomes[1]))
        if pkRandom <= pk:
            temp1 = ""
            temp2 = ""
            counter = 1
            for s in chromosomes[y]:
                if counter > lokus:
                    temp1 = temp1 + s
                counter += 1
            counter = 1
            for s in chromosomes[y+1]:
                if counter > lokus:
                    temp2 = temp2 + s
                counter += 1
            chromosomes[y] = chromosomes[y][:lokus]+temp2
            chromosomes[y+1] = chromosomes[y+1][:lokus]+temp1
        y += 2


def mutations(chromosomes, pm, numberOfChromosomes):
    for x in range(numberOfChromosomes):
        pmRandom = random.uniform(0, 1)
        lokus = random.randint(1, 5)
        if pmRandom <= pm:
            if list(chromosomes[x+1])[lokus-1] == '0':
                s = list(chromosomes[x+1])
                s[lokus-1] = '1'
                chromosomes[x+1] = "".join(s)

            elif list(chromosomes[x+1])[lokus-1] == '1':
                s = list(chromosomes[x+1])
                s[lokus-1] = '0'
                chromosomes[x+1] = "".join(s)


numberOfChromosomes = int(input("How many chromosomes?: "))
print("")
print("Function ax^3+bx^2+cx+d parameters")
a = float(input("Parameter a: "))
b = float(input("Parameter b: "))
c = float(input("Parameter c: "))
d = float(input("Parameter d: "))
print("")
pk = float(input("Crossing over parameters Pk: "))
pm = float(input("Mutation parameter Pm: "))
print("")

chromosomesInput(chromosomes, numberOfChromosomes)
calculatePhenotype(phenotype, chromosomes, numberOfChromosomes, a, b, c, d)

print("\nChromosomy: ", chromosomes)
print("Value of phenotypes of first chromosomes: ", phenotype)
print("Sum of phenotypes values: ",
      sum(phenotype.values()), "\n")

maxCh = float(0)
maxCh1 = ""
localMax = 0
counter = int(0)
x = 1

while True:
    calculatePhenotype(phenotype, chromosomes, numberOfChromosomes, a, b, c, d)
    if max(phenotype.values()) > maxCh:
        maxCh = max(phenotype.values())
        for x in phenotype:
            if phenotype[x] == maxCh:
                maxCh1 = int(chromosomes[x], 2)
    drawOfChromosomes(phenotype, chromosomes)
    chromosomesCrossingOver(chromosomes, pk, numberOfChromosomes)
    mutations(chromosomes, pm, numberOfChromosomes)
    if localMax >= sum(phenotype.values()):
        counter += 1
    elif localMax < sum(phenotype.values()):
        localMax = sum(phenotype.values())
        counter = 0
    if counter >= 1000:
        print("Number of iterations: ", x+1)
        break
    x += 1

print("\nSum of value of phenotypes of final chromosomes: ",
      sum(phenotype.values()))

print("Best found chromosome: ", bin(maxCh1)[2:])
print("Max value of function: ", maxCh, "\n")


input("Click Enter to finish...")
