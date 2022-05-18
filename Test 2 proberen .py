#Test2-2-sem2
# 1 Schrijf de namen van alle roodharige mensen die een bijdrage van meer dan 150 betaalden weg naar een bestand rh150.txt
# 2 Bepaal het percentage mannen bij de bijdragen van minder dan 150 (1 decimaal)
# 3 Wijzig in het bestand Lijst2.txt de haarkleur blond naar laagblond als de lengte <160, ennaar hoogblond als de lengte > 190

def main():
    lees_in=open('Lijst2.txt','r')
    
    persoon=[]
    naam=None
    lengte=None
    geslacht=None
    huisdier=None
    lineNumber=0

    for line in lees_in.readlines():
        line=line.replace('∖n','')
                 
        if lineNumber%5==0:
            naam=line
        elif lineNumber%5==1:
            geslacht=line
        elif lineNumber%5==2:
            lengte=int(line)
        elif lineNumber%5==3:
            haarkleur=line
        elif lineNumber%5==4:
            bijdrage=int(line)

            persoon.append(naam, geslacht,lengte,haarkleur,bijdrage)
            
        lineNumber+=1

    schrijf_weg=open('rh150.txt','w+')
#Vraag 1
    persoonNr=0
    for persoon in personen:
        if persoon[3]=='rood' and persoon[4]>150:
            schrijf_weg(persoon[0]+'∖n')
        persoonNr += 1
#Vraag2
    mannen_minder_150
    mannen_meer_150
    for persoon in personen:
        if persoon[0]=='man' and persoon[4]<150:
            mannen_minder_150 += 1
        if persoon[0]=='man' and persoon[4]>=150:
            mannen_meer_150 +=1
    percentage=(mannen_minder_150/mannen_meer_150)*100
    print(f'het percentage is {percentage:,.1f}')

    lees_in.close()
#Vraag3
    wijzig=open('Lijst2.txt','a')
    laagblond=0
    for persoon in personen:
        if persoon[3]=='blond' and persoon[2]<160:
            wijzig.replace('blond','laagblond') #niet zeker of dit klopt?? 
            laagblond += 1
        if persoon[3]=='blond' and persoon[2]>190:
            wijzig.replace('blond','hoogblond') #niet zeker of dit klopt?? 
            hoogblond += 1
    wijzig.close()

main()
            
            
            
    
    
                 

                 
