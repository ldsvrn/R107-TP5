# len() rewrite...
def length(list):
    len = 0
    for _ in list:
        len += 1
    return len


def voyelle(string):
    voyelles = ('a', 'e', 'i', 'o', 'u', 'y')
    count = 0
    for i in string:
        if i in voyelles:
            count += 1
    return count


def search(string, pattern):
    for i in range(length(string)):
        if string[i:i + length(pattern)] == pattern:
            return i
    return -1


def count(string, pattern):
    count = 0
    for i in range(length(string)):
        if string[i:i + length(pattern)] == pattern:
            count += 1
    return count


T = input("Entrez T: ")
# wagon, wagon, il est beau le wagon
print(f"Longeur de T: {length(T)}")
print(f"Pourcentage de voyelles: {round(voyelle(T) / length(T) * 100, 2)}")
print(f"Première occurence de 'wagon': {search(T, 'wagon')}")
print(f"Occurences de 'wagon': {count(T, 'wagon')}")
