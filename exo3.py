message = ""
for i in input("Entrez un mot ou une phrase: ").lower():
    if not i.isalpha():
        continue
    message += i

if message == message[::-1]:
    print("Le message est un Palindrome!")
else:
    print("Le message n'est pas un Palindrome...")
