# Test2-2-sem2
# 1 Schrijf de namen van alle roodharige mensen die een bijdrage van meer dan 150 betaalden weg naar een bestand rh150.txt
# 2 Bepaal het percentage mannen bij de bijdragen van minder dan 150 (1 decimaal)
# 3 Wijzig in het bestand Lijst2.txt de haarkleur blond naar laagblond als de lengte <160, ennaar hoogblond als de lengte > 190

def main():
    with open('Lijst2.txt', 'r') as input_file:

        personen = []
        naam = None
        geslacht = None
        lengte = None
        haarkleur = None
        bijdrage = None
        lineNumber = 0

        for line in input_file.readlines():
            line = line.replace('\n', '')

            if lineNumber % 5 == 0:
                naam = line
            elif lineNumber % 5 == 1:
                geslacht = line
            elif lineNumber % 5 == 2:
                lengte = int(line)
            elif lineNumber % 5 == 3:
                haarkleur = line
            elif lineNumber % 5 == 4:
                bijdrage = float(line)

                personen.append((naam, geslacht, lengte, haarkleur, bijdrage))

            lineNumber += 1

        with open('rh150.txt', 'w+') as output_file:
            # Vraag 1
            persoonNr = 0
            for persoon in personen:
                if persoon[3] == 'rood' and persoon[4] > 150:
                    output_file.write(persoon[0] + '\n')
                persoonNr += 1

        # Vraag2
        nr_mannen_minder_150 = 0
        nr_mannen = 0
        for persoon in personen:
            if persoon[1] == 'M':
                if persoon[4] < 150:
                    nr_mannen_minder_150 += 1
                nr_mannen += 1
        percentage = (nr_mannen_minder_150 / nr_mannen) * 100
        print(f'het percentage is {percentage:,.1f}')

    # Vraag3
    # Haal '-nieuw' weg voor de exacte oplossing van vraag 3
    with open('Lijst2-nieuw.txt', 'w') as output_file:
        for persoon in personen:

            haarkleur = persoon[3]

            if haarkleur == 'blond':
                if persoon[2] < 160:
                    haarkleur = 'laagblond'
                elif persoon[2] > 190:
                    haarkleur = 'hoogblond'

            naam = persoon[0] + '\n'
            geslacht = persoon[1] + '\n'
            lengte = str(persoon[2]) + '\n'
            bijdrage = str(persoon[4]) + '\n'
            haarkleur = haarkleur + '\n'

            output_file.write(naam)
            output_file.write(geslacht)
            output_file.write(lengte)
            output_file.write(bijdrage)
            output_file.write(haarkleur)


main()
