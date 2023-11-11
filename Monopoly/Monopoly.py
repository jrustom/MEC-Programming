import json

properties = ""

'''
Property data taken from here
https://www.falstad.com/monopoly.html
'''
with open("monopoly/Properties.json", 'r') as file:
    properties = json.load(file)

def read_file_in_batches(file_path, batch_size=32):
    with open(file_path, 'r') as file:
        batch = []
        for line in file:
            batch.append(line.strip())
            if len(batch) == batch_size:
                yield batch
                batch = []

        if batch:
            yield batch

file_path = "monopoly/in.txt"

res = []

railroad = ["5", "15", "25", "35"]


for batch_number, batch_lines in enumerate(read_file_in_batches(file_path, batch_size=32), start=0):
    railroadOwnership = {"A" : 0, "B": 0, "C" : 0, "D" : 0}

    bankAccounts = {"A" : -300, "B": -300, "C" : -300, "D" : -300} # minus 300 to take into account passing go at least once, and collecting some rent

    propertyOwnerships = {} # used to track who owns what

    for i in range(28):
        property = batch_lines[i].split()
        curPrice = 0

        if len(property) > 4:
            owner = property[-1]
            propertyNumber = property[0]
            houses = int(property[2])
            mortgaged = property[3]


            curPrice += properties[propertyNumber]["Price per house"] * houses

            curPrice += properties[propertyNumber]["Price"]

            if mortgaged == 1:
                curPrice -= properties[propertyNumber]["Mortgage"]
            else:
                propertyOwnerships[propertyNumber] = {"owner" : owner, "houses" : houses}

                if propertyNumber in railroad:
                    railroadOwnership[owner] += 1

            bankAccounts[owner] += curPrice



    # calculate based on positions
    for i in range(28, 32):
        line = batch_lines[i].split()

        player = line[0]
        remaining = line[1]
        block = line[2]

        bankAccounts[player] += int(remaining)

        if block in propertyOwnerships:

            # utility
            if block == "12" or block == "28":
                rent =  24 # average utility price assumption

            elif block in railroad:
                rent =  properties[block]["Rent"][railroadOwnership[propertyOwnerships[block]["owner"]]]

            else:
                rent =  properties[block]["Rent"][propertyOwnerships[block]["houses"]]

            # remove rent from owner
            bankAccounts[propertyOwnerships[block]["owner"]] -= rent

            # send rent to payer
            bankAccounts[player] += rent

    res.append(max(500,sum(bankAccounts.values())//4)) # return average of sums


with open('monopoly/out.txt', 'w') as file:
    for node in res:
        file.write(f"{node}\n")
