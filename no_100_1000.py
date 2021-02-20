skaitlis = int(input("Ievadi skaitli no 100 lidz 1000:"))
while skaitlis < 100 or skaitlis > 1000:
    print("Arpus diapazona!!")
    skaitlis = int(input("Ievadi skaitli no 100 lidz 1000:"))
else:
    print("Tavs ievadis skaitlis ir {0}".format(skaitlis))