notes = []
for i in range(5):
    notes.append(input(f"Veuillez entrer la note du module {i+1} et le coefficient correspondant: "))

for i, item in enumerate(notes):
    temp = item.split(" ")
    try:
        notes[i] = (float(temp[0]), int(temp[1]))
    except ValueError:
        print("Erreur, une des notes n'est pas un nombre!")
        quit()

haut, bas = 0.0, 0
for note, coef in notes:
    haut += note * coef
    bas += coef

print(f"La moyenne est de {round(haut/bas, 3)}")