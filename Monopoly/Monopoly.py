# 4 players have completed 5 turns each\
# Players called A,B,C,D
# All players start with the same amount of money, some value between 500 and 2500
# Make dictionary for each box with name along with the value of each of those names ()
# Approximate Equation for finding the original amount for one character: final amount + price of each box they occupy + price of each house they own on each box

dictionary = {
    "Mediterraneal_Avenue": 60,
    "Baltic_Avenue": 60,
    "Reading_railroad": 200,
    "Oriental_Avenue": 100,
    "Vermont_Avenue": 100,
    "Connecticut_Avenue": 120,
    "St.Charle's_Place": 140,
    "Electric_Company": 150,
    "States_Avenue": 140,
    "Virginia_Avenue": 160,
    "Pennsylvania_Railroad": 200,
    "St.James_Place": 180,
    "Tennessee_Avenue": 180,
    "New_York_Avenue": 200,
    "Kentucky_Avenue": 220,
    "Indiana_Avenue": 220,
    "Illinois_Avenue": 240,
    "BnO_Railroad": 200,
    "Atlantic_Avenue": 260,
    "Ventinor_Avenue": 260,
    "Waterworks": 150,
    "Martin_Gardens": 280,
    "Pacific_Avenue": 300,
    "North_Carolina_Avenue": 300,
    "Pennsylvania_Avenue": 320,
    "Short_Line": 200,
    "Park_Place": 350,
    "Boardwalk": 400,
}

community_chest_cards = {
    1: 200,
    2: 200,
    3: 50,
    4: 50,
    5: "Get out of jail free.",
    6: "Go directly to jail. Do not collect $200.",
    7: 200,
    8: 100,
    9: 20,
    10: 10,
    11: 100,
    12: -100,
    13: -150,
    14: 25,
    15: -(40 * houses + 115 * hotels),
    16: 10,
    17: 100,
}
