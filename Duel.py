import
decision_joueur = input("Salut à toi jeune guerrier , tu viens d'entrer dans le repére du grand Pythonnium. Est tu pret a l'affronter durant un jeu de pierre feuille ciseaux ? oui ou non jeune guerrier ?: ")
if decision_joueur == "oui" :
  print("Trés bien prépare toi")
elif decision_joueur == "non" :
  print("mauviette je savais que tu n'en etais pas capable !")
  breakpoint
else :
  print("Je t'ai demandé oui ou non pas de me raconter ta vie")
  breakpoint
joueur = input("Que choisis tu entre la pierre , la feuille ou les ciseaux ? : ")
if joueur == "pierre" or joueur == "la pierre":
  ordinateur = "feuille"
  print(f"Le grand Pythonnium a joué , son choix est : {ordinateur}")
elif joueur == "feuille" or joueur == "la feuille" :
  ordinateur = "ciseaux"
  print(f"Le grand Pythonnium a joué , son choix est : {ordinateur}")
elif joueur ==  "ciseaux" or joueur == "les ciseaux" :
  ordinateur = "pierre"
  print(f"Le grand Pythonnium a joué , son choix est : {ordinateur}")
else:
  print("TU NE SAIS PAS JOUER, LE GRAND PYTHONNIUM TA ÉCRASÉ ET DÉGUSTÉ AU FORMAT BINAIRE !")
  breakpoint
print(f"tu avais donc choisis {joueur} et le grand Pythonnium {ordinateur}, tu as donc ...")
sleep(3)
nom = input("PERDU !!!! mais tu as le merite d'avoir essayé, quel est ton nom que je m'en souvienne ? ")
print(f"{nom} c'est ça ? tu resteras dans les mémoires !")
breakpoint
