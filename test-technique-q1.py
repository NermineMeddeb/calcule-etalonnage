# Lire le fichier
with open('./document.txt', 'r') as file:
    LignesDeDocuments = file.readlines()

# Initialiser la somme
somme_totale = 0

# Calculer la valeur d'étalonnage pour chaque ligne
for ChaqueLigne in LignesDeDocuments:
    chiffres = [caractere for caractere in ChaqueLigne if caractere.isdigit()]  # Extraire les chiffres de chaque ligne pour faire la somme d'apres 
    if len(chiffres) >= 2:
        valeur = int(chiffres[0] + chiffres[-1])  # Combiner le premier et dernier chiffre comme il est indiquer dans le enonce
        somme_totale =somme_totale + valeur  # Ajouter à la somme

# Afficher la somme totale
print("La somme totale des valeurs d'étalonnage  :", somme_totale)
