def artistas_x_genero(artists):
    # Variables
    genre_data = {}
    genre_list = []
    result = []

    # Count artists in each genre
    for artist in artists:
        genre = artist[1]
        if genre not in genre_data:
            genre_list.append(genre)
            genre_data[genre] = [genre, 0, []]
        genre_data[genre][1] += 1
        genre_data[genre][2].append(artist[0])

    # Format
    genre_list.sort()
    for genre in genre_list:
        genre_data[genre][2].sort()
        result.append(genre_data[genre])

    return(result)


def generos_con_mas_seguidores(artists):
    # Variables
    quota = 3
    genre_followers = []
    genres = []
    result = []
    genre_data = {}

    # Count followers per genre
    for artist in artists:
        if artist[1] not in genre_data:
            genre_data[artist[1]] = 0
        genre_data[artist[1]] += artist[2]

    # Unpack genres
    for genre in genre_data:
        genres.append(genre)
        genre_followers.append(genre_data[genre])

    # Select top 3
    while quota > 0:
        index = genre_followers.index(max(genre_followers))
        result.append(genres[index])
        del genre_followers[index]
        del genres[index]
        quota -= 1

    return result
