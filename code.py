#  C'est bien beau d'écrire ça mais j'ai pas lu le document donc il faudrait peut-être que je commence par là.

print("Python seems to f**ing work at last")

def fib_rec(n):
    if n <= 1 : 
        return 1
    else : 
        return fib_rec(n-1) + fib_rec(n-2)

def listeFib(n):
    return [fib_rec(k) for k in range(n)]

print(listeFib(int(input("Combien de termes ?"))))

# OK j'ai un environnement python qui marche ça fait très plaisir maintenant il n'y a plus qu'à :
# -Lire Orderly.pdf, comprendre leur code, lire la documentation de pynauty, et implémenter tout ça
# Ça a l'air prometteur en vrai, il faudra aussi que j'upload le code sur github pour pouvoir travailler
# dessus depuis Sète depuis mon ordi, en vrai ça devrait pouvoir le faire, j'y crois
# Tout ça sont des tests pour voir si GitHub marche effectivement bien, c'est là le moment om je commence à avoir un max de fun, en plus c'est confortable de bosser comme ça ici, je pense qu'il faudrait que je reste ici pour faire le boulot for now sinon je vais être distracted
