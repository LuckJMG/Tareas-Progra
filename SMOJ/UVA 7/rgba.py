def change_palette_alpha(palettes, alpha):
    # Variables
    new_palettes = list(palettes)

    # Change alpha value
    for palette in new_palettes:
        palette[3] = alpha

    return new_palettes
