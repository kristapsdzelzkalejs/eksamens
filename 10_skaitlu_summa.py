def uz_skaitli(text, default=0):
    try:
        return int(text)
    except ValueError:
        return default

skaitli = input("Ievadi 10 skaitlus atdalitus ar atstarpi: ")
print(sum(cipars for word in skaitli for cipars in map(uz_skaitli, word.split())))