import tempConverterKey as tc

doc = "temps.txt"
file = open(doc)
line = file.readline()

tempMap = {}
while (line):
    f, c = line.split(",")
    tempMap[int(f)] = float(c)
    line = file.readline()
file.close()
correct = 0
for i, (f, c) in enumerate(tempMap.items()):
    out= tc.farConversion(f)
    if out == c:
        correct += 1
        print("Fahrenheit Test" + str(i) + " is correct!")
    elif (out> c):
        print("Fahrenheit Conversion" + str(i) + " celsius temperature is too high.")
    else:
        print("Fahrenheit Conversion" + str(i) + " celsius temperature too low.")

for i, (f, c) in enumerate(tempMap.items()):
    out= tc.celsiusConversion(c)
    if out == f:
        correct += 1
        print("Celsius Test" + str(i) + " is correct!")
    elif (out> c):
        print("Celsius Conversion" + str(i) + " fahrenheit temperature is too high.")
    else:
        print("Celsius Conversion" + str(i) + " fahrenheit temperature too low.")

print("Final grade is: " + str(correct/(len(tempMap)*2) * 100) + "%")




