# Fabrice Bouchard
# 9 septembre 2022
# Ce programme compte les mots dans une phrase

# Mise en place de la fonction

def count_word():
    phrase = input(str("Écrivez une phrase:"))
    phrase = len(phrase.split(" "))   # Enlève les espaces et transforme les mots en caractères
    print(phrase)

count_word()