def vocales(palabra):
    pass

def ganador(p1, p2, p3):
    # Determinate how many vocals has each word
    p1 = vocales(p1)
    p2 = vocales(p2)
    p3 = vocales(p3)

    # Check the winner
    if p1 > p2 and p1 > p3:
        return 1
    elif p2 > p1 and p2 > p3:
        return 2
    elif p3 > p1 and p3 > p2:
        return 3
    else:
        return "Empate"

print(ganador("MAsas", "BocAs", "AutO"), ganador("aAa", "iwi", "eEE"))
