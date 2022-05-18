# 1 Op sommige plaatsen staat een regel met de tekst dummy (op onregelmatige plaatsen, niet gekoppeld aan de plaats van een zeker veld. Zorg in uw programmacode voor het
#      verwijderen van de tekst dummy en bewaar het gewijzigde bestand als Lijst3.txt.
# 2 Bereken de gemiddelde bijdrage (2 decimalen) van alle mensen met een Poedel of Huiskat
# 3 Bepaal het procentueel aandeel Cavia's bij de huisdieren

werkelijkeOplossing = False


def get_suffix():
    global werkelijkeOplossing
    if werkelijkeOplossing:
        return ''
    else:
        return '-nieuw'


def main():
    # Vraag1
    # Ik snap niet hoe ik die dummy moet verwijderen?

    # Vraag2
    lees_in = open('Lijst3.txt', 'r')
    filtered_list_file = open(f'Lijst3{get_suffix()}.txt', 'w+')

    for line in lees_in.readlines():
        # Gebruik line.rstrip! \n moet weg!
        if line.rstrip('\n') != 'dummy':
            filtered_list_file.write(line)

    lees_in.close()
    filtered_list_file.close()

    personen = []
    line_number = 0
    naam = None
    geslacht = None
    lengte = None
    haarkleur = None
    huisdier = None
    bijdrage = None

    with open(f'Lijst3{get_suffix()}.txt', 'r') as input_file:
        for line in input_file.readlines():
            line = line.replace('\n', '')
            if line_number % 6 == 0:
                naam = line
            elif line_number % 6 == 1:
                geslacht = line
            elif line_number % 6 == 2:
                lengte = int(line)
            elif line_number % 6 == 3:
                haarkleur = line
            elif line_number % 6 == 4:
                huisdier = line
            elif line_number % 6 == 5:
                bijdrage = float(line)

                personen.append((naam, geslacht, lengte, haarkleur, huisdier, bijdrage))
            line_number += 1

    mensen_huiskat_of_poedel = 0
    bijdragen_mensen_huiskat_of_poedel = 0
    for persoon in personen:
        if persoon[4] == 'Poedel' or persoon[4] == 'Huiskat':
            mensen_huiskat_of_poedel += 1
            bijdragen_mensen_huiskat_of_poedel += persoon[5]

    # None als er geen mensen zijn?
    gemiddelde = bijdragen_mensen_huiskat_of_poedel / mensen_huiskat_of_poedel
    # Ben niet zeker hoe ik deze vraag moet oplossen
    print(f'gemiddelde is {gemiddelde:,.1f}')

    # Vraag3
    nr_cavias = 0
    nr_huisdieren = 0
    for persoon in personen:
        # Elke persoon heeft een huisdier (aanname)
        nr_huisdieren += 1

        if persoon[4] == 'Cavia':
            nr_cavias += 1

    percentage = nr_cavias / nr_huisdieren * 100
    print(f'het percentage is {percentage:,.1f}')


main()
