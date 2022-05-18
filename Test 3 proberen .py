# 1 Op sommige plaatsen staat een regel met de tekst dummy (op onregelmatige plaatsen, niet gekoppeld aan de plaats van een zeker veld. Zorg in uw programmacode voor het
#      verwijderen van de tekst dummy en bewaar het gewijzigde bestand als Lijst3.txt.
# 2 Bereken de gemiddelde bijdrage (2 decimalen) van alle mensen met een Poedel of Huiskat
# 3 Bepaal het procentueel aandeel Cavia's bij de huisdieren

def main():
#Vraag1
    #Ik snap niet hoe ik die dummy moet verwijderen?
    
#Vraag2
    lees_in=open('Lijst3.txt','r')
    
    personen=[]
    lineNumber=0
    naam=None
    geslacht=None
    lengte=None
    haarkleur=None
    huisdier=None
    bijdrage=None

    for line in lees_in.readlines():
        line=line.replace('∖n','')
        if lineNumber%5==0:
            naam=line
        elif lineNumber%6==0:
            geslacht=line
        elif lineNumber%6==1:
            lengte=int(line)
        elif lineNumber%6==2:
            haarkleur=line
        elif lineNumber%6==3:
            huisdier=line
        elif lineNumber%6==4:
            bijdrage=int(line)

            personen.append(naam,geslacht,lengte,haarkleur,huisdier,bijdrage)
        lineNumber += 1

    mensen_huiskat_of_poedel=0
    bijdragen_mensen_huiskat_of_poedel=0
    for persoon in personen:
        if persoon[3]=='poedel' or persoon[3]=='huiskat':
            mensen_huiskat_of_poedel += 1
    gemiddelde=sum(bijdragen_mensen_huiskat_of_poedel)/len( mensen_huiskat_of_poedel)
    #Ben niet zeker hoe ik deze vraag moet oplossen
    print(f'gemiddelde is {gemiddelde:,.1f}')

#Vraag3
    cavia=0
    andere_huisdieren=0
    for persoon in personen:
        if persoon[3]=='cavia':
            cavia +=1
        if persoon[3]!='cavia':
            andere_huisdieren +=1
    percentage=len(cavia)/len(andere_huisdieren)
    print(f'het percentage is {percentage:,.1f}')
    
    lees_in.close()

main()

    
    
            
    

    
        
            
    
    
    

