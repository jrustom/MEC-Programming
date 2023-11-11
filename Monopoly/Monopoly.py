# 4 players have completed 5 turns each\
# Players called A,B,C,D
# All players start with the same amount of money, some value between 500 and 2500
# Make dictionary for each box with name along with the value of each of those names ()
# Approximate Equation for finding the original amount for one character: final amount + price of each box they occupy + price of each house they own on each box

import json

properties = ""

with open("Monopoly/Properties.json", 'r') as file:
    properties = json.load(file)

def read_file_in_batches(file_path, batch_size=32):
    with open(file_path, 'r') as file:
        batch = []
        for line in file:
            batch.append(line.strip())
            if len(batch) == batch_size:
                yield batch
                batch = []

        # Yield the last batch (if any) that might be smaller than the specified batch size
        if batch:
            yield batch

# Example usage:
file_path = "Monopoly/in.txt"

for batch_number, batch_lines in enumerate(read_file_in_batches(file_path, batch_size=32), start=1):

    bankAccounts = {"A" : 0, "B": 0, "C" : 0, "D" : 0}

    propertyOwnerShips = {}

    for i in range(28):
        property = batch_lines[i].split()

        if len(property) > 4:
            owner = property[-1]
            propertyName = property[0]
            houses = int(property[2])
            mortgaged = property[3]

            curPrice = 0

            curPrice += properties[propertyName]["Price per house"] * houses

            curPrice += properties[propertyName]["Price"]

            if mortgaged == 1:
                curPrice -= properties[propertyName]["Mortgage"]
            else:
                propertyOwnerShips[propertyName] = {"owner" : owner, "houses" : houses}

            bankAccounts[owner] += curPrice

        else:
            continue


    # calculate based on positions

    for i in range(29, 32):
        line = batch_lines[i].split()

        player = line[0]
        remaining = line[1]
        block = line[2]

        bankAccounts[player] += int(remaining)

        if block in propertyOwnerShips:
            # remove rent from owner
            rent =  properties[block]["Rent"][propertyOwnerShips[block]["houses"]]

            bankAccounts[propertyOwnerShips[block]["owner"]] -= rent

            # send rent to payer
            bankAccounts[player] += rent

    print(max(bankAccounts.values()))
