__author__ = 'Windows'
nakup_listek = []

print ("Pozdravljeni v vasi nakupovalni kosarici")

odgovor = "da"
while odgovor == "da":
    odgovor = raw_input("Ali zelis dodati artikel? Da / Ne ? ")

    if odgovor == "ne":
        print("Nic ne dodaj. V vasi nakupovalni kosarici je: ")
        break
    elif odgovor == "da":
        print("Dodaj")


    dodatek = raw_input("Povej, kaj zelis dodati? ")

    nakup_listek.append(dodatek)
    print nakup_listek

print nakup_listek