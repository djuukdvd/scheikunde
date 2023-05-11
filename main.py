import random

homogenen = {
    "alkanen": {
        "methaan": "ch4",
        "ethaan": "c2h6",
        "propaan": "c3h8",
        "butaan": "c4h10",
        "pentaan": "c5h12",
        "hexaan": "c6h14",
        "heptaan": "c7h16",
        "octaan": "c8h18",
    },
    "alcoholen": {
        "methanol": "ch4o",
        "ethanol": "c2h6o",
        "propanol": "c3h8o",
        "butanol": "c4h10o",
        "pentanol": "c5h12o",
        "hexanol": "c6h14o",
        "heptanol": "c7h16o",
        "octanol": "c8h18o",
    },
    "aldehydes": {
        "methanal": "ch2o",
        "ethanal": "c2h4o",
        "propanal": "c3h6o",
        "butanal": "c4h8o",
        "pentanal": "c5h10o",
        "hexanal": "c6h12o",
        "heptanal": "c7h14o",
        "octanal": "c8h16o",
    },
    "ketonen": {
        "methanon": "ch2o",
        "ethanon": "c2h4o",
        "propanon": "c3h6o",
        "butanon": "c4h8o",
        "pentanon": "c5h10o",
        "hexanon": "c6h12o",
        "heptanon": "c7h14o",
        "octanon": "c8h16o",
    },
    "alkaanzuren": {
        "methaanzuur": "ch2o2",
        "ethaanzuur": "c2h4o2",
        "propaanzuur": "c3h6o2",
        "butaanzuur": "c4h8o2",
        "pentaanzuur": "c5h10o2",
        "hexaanzuur": "c6h12o2",
        "heptaanzuur": "c7h14o2",
        "octaanzuur": "c8h16o2",
    },
    "alkaanamines": {
        "methaanamine": "ch5n",
        "ethaanamine": "c2h7n",
        "propaanamine": "c3h9n",
        "butaanamine": "c4h11n",
        "pentaanamine": "c5h13n",
        "hexaanamine": "c6h15n",
        "heptaanamine": "c7h17n",
        "octaanamine": "c8h19n",
    },
}
while True:
    random_homogeen_key, random_homogeen_waarde = random.choice(list(homogenen.items()))

    naam, formule = random.choice(list(random_homogeen_waarde.items()))

    if random.randint(0, 1) == 1:
        print(naam)

        antwoord = input("typ hier de formule: ")

        if antwoord == formule:
            print("correct\n")
            homogenen[random_homogeen_key].pop(naam)
            homogenen = {key: value for key, value in homogenen.items() if value}
            if not homogenen:
                exit()
        else:
            print(formule)
            print("Bertje boos\n")
    else:
        print(formule)

        antwoord = input("typ hier de naam: ")

        if random_homogeen_key == "aldehydes" or random_homogeen_key == "ketonen":
            if antwoord == naam[:4] + "anal" or antwoord == naam[:4] + "anon":
                print("correct\n")
                homogenen[random_homogeen_key].pop(naam)
                homogenen = {key: value for key, value in homogenen.items() if value}
                if not homogenen:
                    exit()
            else:
                print(naam)
                print("Bertje boos\n")
        else:
            if antwoord == naam:
                print("correct\n")
                homogenen[random_homogeen_key].pop(naam)
                homogenen = {key: value for key, value in homogenen.items() if value}
                if not homogenen:
                    exit()
            else:
                print(naam)
                print("Bertje boos\n")
