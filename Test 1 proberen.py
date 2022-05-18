# Dit tekstbestand Lijst 1.txt heeft een consistente structuur. Elke record bestaat uit 5 velden: Naam
# van een persoon, aanduiding van het geslacht,lengte van de persoon in cm (als geheel
# getal), haarkleur en huisdier. De gegevens zijn geheel fictief, alle overeenkomsten met
# bestaande personen zijn gebaseerd op toeval.
# Maak een programma in Python® waarmee u volgende vragen beantwoordt / uitvoert:

# 1 Schrijf de namen van alle blonde mensen met een Dwergkonijn weg naar een bestand
# bmdwk.txt
# 2 Bepaal de gemiddelde lengte van mensen met een Siamese kat (in cm, 1 decimaal)
# 3 Bepaal en toon het percentage (1 decimaal) van het aantal vrouwen met een Cavia t.o.v. het
# totaal aantal vrouwen.


def main():
    with open('Lijst1.txt', 'r') as lees_in:
        personen = []
        lineNumber = 0

        naam = None
        geslacht = None
        lengte = None
        haarkleur = None
        huisdier = None

        for line in lees_in.readlines():
            line = line.replace('\n', '')  # waarom moesten we dit ook al weer doen?

            if lineNumber % 5 == 0:
                naam = line
            elif lineNumber % 5 == 1:
                geslacht = line
            elif lineNumber % 5 == 2:
                lengte = int(line)
            elif lineNumber % 5 == 3:
                haarkleur = line
            elif lineNumber % 5 == 4:
                huisdier = line

                personen.append(
                    (naam, geslacht, lengte, haarkleur, huisdier))  # waarom moet ik dit zo laten inspringen?

            lineNumber += 1

        # 'a' betekent 'append' -> toevoegen aan het einde van de file
        with open('bmdwk.txt', 'w+') as output_file:
            # Vraag1
            persoonNr = 0
            for persoon in personen:
                if persoon[3] == 'blond' and persoon[4] == 'Dwergkonijn':
                    output_file.write(persoon[0] + '\n')
                persoonNr += 1

        # Vraag2
        lengtes_mensen_siamese_kat = []
        for persoon in personen:
            if persoon[4] == 'Siamese kat':
                lengtes_mensen_siamese_kat.append(persoon[2])
        gemiddelde = sum(lengtes_mensen_siamese_kat) / len(lengtes_mensen_siamese_kat)
        print(f'gemiddelde is {gemiddelde:,.1f}')
        # Vraag3
        aantal_vrouwen_met_cavia = 0
        aantal_vrouwen = 0
        for persoon in personen:
            if persoon[1] == 'V':
                aantal_vrouwen += 1
            if persoon[4] == 'Cavia':
                aantal_vrouwen_met_cavia += 1
        percentage = (aantal_vrouwen_met_cavia / aantal_vrouwen) * 100
        print(f'het percentage is {percentage:,.1f}')


main()
