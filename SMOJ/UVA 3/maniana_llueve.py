# Variables
will_rain = False

# Input
cluods_day = int(input())
cluods_night = int(input())
thief_ants = input()
dog_howls = input()
if dog_howls == "si":
    dog_eye = input()
tv_forecast = int(input())

# Determinate if tomorrow is going to rain
if cluods_night > cluods_day >= 3:
    will_rain = True
elif thief_ants == "si":
    will_rain = True
elif dog_howls == "si" and dog_eye == "izquierdo":
    will_rain = True

if tv_forecast >= 4:
    will_rain = False
elif cluods_night > cluods_day >= 3 and thief_ants == "si" and dog_howls == "si":
    will_rain = False

# Output
if will_rain:
    print("Maniana llueve")
else:
    print("Maniana se puede salir a jugar")
