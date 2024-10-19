
import random
#
# for i in range(1, 50):
#     g = random.randint(0,51)
#     print((g))
#!/usr/bin/python
from random import randint

print("Bienvenue sur MegaGame V1.0 :-)")

# On demande un entier aléatoire entre 1 et 100 compris.
random_value = randint(1, 100)
print("Valeur aléatoire choisie :", random_value)

score = 0
# Tant que l'entier aléatoire n'a pas été trouvé.
while True:
    try:
        # On demande la saisie d'un entier à partir de la console.
        value = int(input("Veuillez saisir une valeur entière (1..100) : "))
    except ValueError:
        print("On a dit un entier ! On se concentre.")
        continue
    score += 1

    # On compare l'entier saisi avec la valeur aléatoire.
    if value == random_value:
        print(f"Félicitations, vous avez trouvé en {score} coup(s) !")
        break
    if value < random_value:
        print("La valeur à trouver est plus grande !")
    else:
        print("La valeur à trouver est plus petite !")

print("Bye bye")

