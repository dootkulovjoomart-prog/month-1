

while True:
    slovo=input("Enter your slovo (Чтобы остановить:Стоп): ").lower().strip()
    print(f"Слово:{slovo}")
    if slovo=='стоп':
       print("Programa ostanovleno")
       break

    kolichestvo_bukv= len(slovo)
    print(f"Количество букв : {kolichestvo_bukv}")
    glasnye = "aeiouауоыиэяюёе"
    soglasnye = "bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщъь"
    glasnye_schetcik = 0
    soglasnye_schetcik = 0

    for letter in slovo:
        if letter in glasnye:
            glasnye_schetcik+=1
        elif letter in soglasnye:
            soglasnye_schetcik+=1
    print("Количество гласных :",glasnye_schetcik)
    print("Количество согласных :",soglasnye_schetcik)
    if kolichestvo_bukv>0:

       prosent_glasnyh=round((glasnye_schetcik/kolichestvo_bukv)*100,2)
       prosent_soglasnyh=round((soglasnye_schetcik/kolichestvo_bukv)*100,2)

       print(f"Процент гласных/Процент согласных :{prosent_glasnyh}% /{prosent_soglasnyh}%")


