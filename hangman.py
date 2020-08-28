# Write your code here
import random
menu = input("""H A N G M A N
Type "play" to play the game, "exit" to quit: """)

if menu == "play":
    choix = ["python", "java", "kotlin", "javascript"]
    solution = choix[random.randint(0, 3)]
    progres = "-" * len(solution)
    lettres_choisies = set()
    essais_restants = 8
    while essais_restants > 0:
        print()
        print(progres)
        lettre = input("Input a letter: ")
        ajouter_lettre = False
        if lettre in lettres_choisies:
            print("You already typed this letter")
        elif len(lettre) != 1:
            print("You should input a single letter")
        elif not lettre.islower():
            print("It is not an ASCII lowercase letter")
        elif lettre not in solution:
            ajouter_lettre = True
            print("No such letter in the word")
            essais_restants -= 1
        else:
            ajouter_lettre = True
            repeat = solution.count(lettre)
            dernier_index = 0
            for x in range(repeat):
                endroit = solution.find(lettre, dernier_index)
                progres = progres[:endroit] + lettre + progres[endroit + 1:]
                dernier_index = endroit
        if lettre not in lettres_choisies and ajouter_lettre:
            lettres_choisies.add(lettre)
        if progres == solution:
            print("""You guessed the word!
            You survived!""")
    if progres != solution:
        print("You are hanged!")
