def puntaje(tournaments, points, year):
    # Variables
    year_tournaments = []
    points_list = []
    player_list = []
    player_points = {}
    result = []
    tmp_results = []

    # Filter tournaments by requested year
    for tournament in tournaments:
        if year in tournament:
            year_tournaments.append(tournament)

    # Sum points for each player
    for tournament in points:
        for competition in year_tournaments:
            if tournament == competition[1]:
                if competition[2] not in player_points:
                    player_points[competition[2]] = 0
                player_points[competition[2]] += points[tournament]

    # Unpack players and points
    for player in player_points:
        player_list.append(player)
        points_list.append(player_points[player])

    # Organize from A to Z
    count = len(player_list)
    while count > 0:
        index = player_list.index(max(player_list))
        tmp_results.append([points_list[index], player_list[index]])
        del points_list[index]
        del player_list[index]
        count -= 1

    # Unpack players and points
    for score in tmp_results:
        points_list.append(score[0])
        player_list.append(score[1])

    # Organize point and player list
    count = len(player_list)
    while count > 0:
        index = points_list.index(max(points_list))
        result.append([points_list[index], player_list[index]])
        del points_list[index]
        del player_list[index]
        count -= 1

    return result
