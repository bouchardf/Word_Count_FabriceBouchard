# Fabrice Bouchard
# 28 septembre 2022
# Ce programme compte les mots dans une phrase

# Mise en place de la fonction

def count_word():
    phrase = input(str("Écrivez une phrase:"))
    phrase = len(phrase.split(" "))   # Enlève les espaces et transforme les mots en caractères
    return phrase

# Définire la variable

word = count_word()

# Afficher le nombre de mot dans la phrase
print(word)