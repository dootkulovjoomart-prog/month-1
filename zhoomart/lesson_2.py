#time = input("enter time:").lower()
# #if time == "morning" or time== "utro":
# #    print("good morning")
# #elif time == "afternoon" or time== "den":
# # print("good afternoon")
# #elif time == "evening" or time== "vecher":
#  #   print("good evening")
# #else:
#   #  print("heloo")
temperatura=int(input("enter temperatura:"))
if -40 <= temperatura <=0:
    print("holodno")
elif 1 <= temperatura <=16:
    print("prohladno")
elif 17 <= temperatura <=40:
    print("zharko")
else:
    print("opasno")