deger = input(">>>")
yedek = deger
print(deger)
for i in deger:
    deger = deger[deger.__len__()-1]+deger[:deger.__len__()-1]
    if deger==yedek:
        break
    print(deger)