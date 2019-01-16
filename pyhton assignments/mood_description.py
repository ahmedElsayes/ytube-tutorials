mood = int(input("How do you feel? (1-10) "))
if mood == 1:
    print("A suitable smiley would be :'(")
elif mood == 10:
    print("A suitable smiley would be :-D")
elif  (7 < mood < 10):
    print("A suitable smiley would be :-)")
elif (4 <= mood <= 7):
    print("A suitable smiley would be :-|")
elif (1 < mood < 4):
    print("A suitable smiley would be :-(")
else:
    print("Bad input!")
