name = "?"
familie = ["franzi", "feri", "pati", "katrin"]
while name != "bye":
    name = input("Wie ist Dein Name? ")
    print("Hallo " + name + " schön Dich zu sehen")
    if name in familie:
        print("Du bist dran mit Tisch abräumen!")
print("und tschüss")
