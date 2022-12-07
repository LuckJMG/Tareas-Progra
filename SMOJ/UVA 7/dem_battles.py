def ganadorBatalla(punchlines):
    # Determine challengers
    competitor1 = [punchlines[0][0], 0]
    competitor2 = [punchlines[1][0], 0]

    # Count punchlines of each competitor
    for punchline in punchlines:
        if punchline[0] == competitor1[0]:
            competitor1[1] += punchline[1]
        else:
            competitor2[1] += punchline[1]

    # Determine the winner
    difference = competitor1[1] - competitor2[1]

    if difference > 0:
        return [competitor1[0], difference]
    elif difference < 0:
        return [competitor2[0], abs(difference)]
    else:
        return ["Réplica", difference]
