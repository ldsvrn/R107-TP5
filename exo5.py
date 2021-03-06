def salary(hrs, wage):
    pay = 0.0
    if hrs <= 160:
        pay += hrs * wage
    if 160 < hrs <= 200:
        pay += (hrs - 160) * (wage * 1.25)
    if hrs > 200:
        pay += (hrs - 200) * (wage * 1.5)
    return pay


while True:
    try:
        timeWorked = int(input("Combien d'heures avez vous travaillé?: "))
        hrWage = int(input("Combien êtes vous payé à l'heure?: "))
        break
    except ValueError:
        continue

print(f"Vous serez payé {salary(timeWorked, hrWage)}")
