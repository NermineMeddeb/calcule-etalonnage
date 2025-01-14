with open('./document.txt', 'r') as file:
    LignesDeDocuments = file.readlines()

somme_totale = 0

for ChaqueLigne in LignesDeDocuments:
    chiffres = [caractere for caractere in ChaqueLigne if caractere.isdigit()]   
    if len(chiffres) >= 2:
        valeur = int(chiffres[0] + chiffres[-1])  
        somme_totale =somme_totale + valeur  

print("La somme totale des valeurs d'étalonnage  :", somme_totale)
