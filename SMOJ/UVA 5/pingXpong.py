def ping_pong(player1, score1, player2, score2, point):
    # Check if a player already won
    if score1 == 5:
        return "TERMINADO - GANA PAR"
    elif score2 == 5:
        return "TERMINADO - GANA IMPAR"

    else:
        if point % 2 == 0:
            score1 += 1

            # Check if player1 won with extra point
            if score1 == 5:
                return "TERMINADO - GANA PAR"
            return player1
        else:
            score2 += 1

            # Check if player1 won with extra point
            if score2 == 5:
                return "TERMINADO - GANA IMPAR"
            return player2
