def filtrar(original, delete):
    # Variables
    filtered_list = []

    # Delete repeated elements
    for element in original:
        if element not in filtered_list:
            filtered_list.append(element)

    # Filter list
    for element in delete:
        if element in filtered_list:
            filtered_list.remove(element)

    return filtered_list
