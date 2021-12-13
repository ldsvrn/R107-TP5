names = []
for i in range(2):
    names.append((input(f"Nom {i + 1}: ").upper(),
                  input(f"Prénom {i + 1}: ").capitalize()))

for name in names:
    print(f"{name[1]} {name[0]}")
