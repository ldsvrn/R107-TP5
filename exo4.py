while True:
    try:
        money = int(input("Combien de monnaie voulez vous?: "))
    except ValueError:
        continue
    break

available, given = [100, 50, 10, 2, 1], 0
toGive = [0] * len(available)
# good old bruteforce
while given != money:
    for i, item in enumerate(available):
        if (money - given) / item >= 1:
            given += item
            toGive[i] += 1
            break

for amount, bill in zip(toGive, available):
    print(f"\t- {amount}x {bill}€")
