while True:
   day=int(input("Enter the day:"))
   month=int(input("Enter the month:"))

   if(day>=21 and day<=31 and month==3) or (day>=1 and day<=20 and month==4):
      print("Oven")
   elif (day>=21 and day<30 and month==4) or (day>=1 and day<=21 and month==5):
      print("teles")
   elif (day>=22 and day<=31 and month==5) or (day>=1 and day<=21 and month==6):
      print("bliznesy")
   elif (day>=22 and day<=30 and month==6) or (day>=1 and day<=22 and month==7):
      print("rak")
   elif (day>=23 and day<=30 and month==7) or (day>=1 and day<=21 and month==8):
      print("lev")
   elif (day>=22 and day<=31 and  month==8) or (day>=1 and  day<=23 and month==9):
      print("deva")
   elif (day>=24 and day<=30  and month==9) or (day>=1 and  day<=23 and month==10):
      print("vesy")
   elif (day>=24 and day<=30 and month==10) or (day>=1 and day<=22 and month==11):
      print("skorpion")
   elif (day>=23 and day<=30 and month==11) or (day>=1 and  day<=22 and month==12):
      print("streles")
   elif (day>=23 and day<=31 and month==12) or (day>=1 and day<=20  and month==1):
      print("kozerok")
   elif (day>=21 and day<=31 and  month==10) or (day>=1 and day<=19 and month==2):
      print("vodoley")
   elif (day>=20 and day<=28 and month==2) or (day<=20 and day>=1 and month==3):
      print("fish")
   else:

      print("oshibka")
