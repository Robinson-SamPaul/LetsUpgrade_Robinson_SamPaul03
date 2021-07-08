print("\tAltitudeProblems\n")

altitudeRequired = 1000
pilotsAltitude = int(input("Enter Your Current Altitude : "))

if altitudeRequired == pilotsAltitude:
    print("\nSafe to land.\nAltitude = ",(str(pilotsAltitude)+"ft"))

elif altitudeRequired < pilotsAltitude and pilotsAltitude < 5000:
    print("\nBring Down to 1000ft.\nAltitude = ",(str(pilotsAltitude)+"ft"))

elif pilotsAltitude < 1000:
    print("\nEverybody just hang on.\nAltitude = ",(str(pilotsAltitude)+"ft"))
    
else:
    print("\nTurn Around.\nAltitude = ",(str(pilotsAltitude)+"ft"))

