import json

loginNodesJson = json.dumps(


    #PASTE JSON FROM HERE
{
	"table": "NODES",
	"rows":
	[
		{
			"NAME": "EARTH",
			"l": 1,
			"r": 21
		},
    {
			"NAME": "EUROPE",
			"l": 2,
			"r": 5
		},
    {
			"NAME": "ASIA",
			"l": 6,
			"r": 10
		},
    {
			"NAME": "AFRICA",
			"l": 11,
			"r": 15
		},
    {
			"NAME": "AMERICA",
			"l": 16,
			"r": 20
		},
    {
			"NAME": "SPAIN",
			"l": 3,
			"r": 3
		},
    {
			"NAME": "FRANCE",
			"l": 4,
			"r": 4
		},
    {
			"NAME": "JAPAN",
			"l": 7,
			"r": 7
		},
    {
			"NAME": "CHINA",
			"l": 8,
			"r": 8
		},
    {
			"NAME": "MOROCCO",
			"l": 12,
			"r": 12
		},
    {
			"NAME": "EGYPT",
			"l": 13,
			"r": 13
		},
    {
			"NAME": "BRASIL",
			"l": 17,
			"r": 17
		},
    {
			"NAME": "USA",
			"l": 18,
			"r": 18
		}
	]
}
    #PASTE JSON TO HERE
)

loginNodes = json.loads(loginNodesJson)

#Get the lowest L and biggest R
minL = 0
maxR = 0
for node in loginNodes['rows']:
    if node['l'] < minL:
        minL = node['l']
    if node['r'] > maxR:
        maxR = node['r']

output = "\n"
openedNodes = []
numOpenedNodes = 0
numberOfOverlaps = 0
overlapLines = []

for line in range(minL, maxR - minL + 1):
    readNodes = []
    nodesInLine = 0
    hasOverlap = False

    #Draw 0's
    for digits in range(4 - len(str(line))):
        output = output + "0"
    output = output + str(line) + "--> "
    #Draw *'s
    for indent in range(numOpenedNodes):
        output = output + "*  "

    for node in loginNodes['rows']:
        if node['l'] == line:
            readNodes.append(node['NAME'])
            output = output + "*  " + node['NAME']
            openedNodes.append(node['NAME'])
            numOpenedNodes = numOpenedNodes + 1
            nodesInLine += 1
            if node['l'] == node['r']:
                output = output + "/ "
            else:
                output = output + " "

    for node in loginNodes['rows']:
        if node['r'] == line:
            numOpenedNodes = numOpenedNodes - 1

            #The node that closes should be the las one that was opened but not closed. If not, there is an overlapping
            if (openedNodes.index(node['NAME']) != len(openedNodes) - 1):
                hasOverlap = True
                numberOfOverlaps += 1
                overlapLines.append(line)

            openedNodes.remove(node['NAME'])

            if node['NAME'] not in readNodes:
                output = output + "/" + node['NAME'] + " "
                nodesInLine += 1

            readNodes.append(node['NAME'])

    if (nodesInLine == 0):
        output = output + "*  "

    if (hasOverlap == True):
        output = output + "\n  %%%%%%%%%%%%%%%%%%%%%%%%% ERROR: OVERLAPPING LINE " + str(
            line) + " %%%%%%%%%%%%%%%%%%%%%%%%%"

    output = output + "\n"

print(output)

print(numberOfOverlaps, "Overlapping lines.")
if (numberOfOverlaps > 1):
    print("Overlapping in lines: ")
    for overlap in overlapLines:
        print("-" + str(overlap))

if (numOpenedNodes > 0):
    print("\nThere are nodes that haven't been closed:")
    for i in openedNodes:
        print("-" + str(openedNodes[i]))
