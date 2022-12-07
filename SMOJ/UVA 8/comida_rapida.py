def filtro(clients, branch, amount):
    # Filter clients by branch
    filtered_clients = []
    for client in clients:
        for location in clients[client]:
            if location[0] == branch:
                filtered_clients.append([clients[client][0], location[1]])

    # Filter clients by amount
    amount_list = []
    tmp = list(filtered_clients)
    for client in filtered_clients:
        if client[1] > amount:
            amount_list.append(client[1])
        else:
            tmp.remove(client)

    # Order clients from highest to lowest
    count = len(amount_list)
    filtered_clients = list(tmp)
    ordered_clients = []
    while count > 0:
        index = amount_list.index(max(amount_list))
        ordered_clients.append(filtered_clients[index])
        del filtered_clients[index]
        del amount_list[index]
        count -= 1

    return ordered_clients
