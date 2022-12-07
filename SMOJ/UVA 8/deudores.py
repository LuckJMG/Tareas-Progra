def deudas(fines):
    # Variables
    debts = []
    names = []
    tmp_result = []
    result = []
    total_fines = {}

    # Calculate total fines
    for fine in fines:
        name = fine[0]
        debt = fine[1]
        if name not in total_fines:
            total_fines[name] = 0
        total_fines[name] += debt

    # Unpack total fines dictionary
    for name in total_fines:
        names.append(name)
        debts.append(total_fines[name])

    # Organize list from Z to A
    count = len(names)
    while count > 0:
        index = names.index(min(names))
        tmp_result.append([names[index], debts[index]])
        del names[index]
        del debts[index]
        count -= 1

    # Unpack total fines dictionary
    for fine in tmp_result:
        names.append(fine[0])
        debts.append(fine[1])

    # Organize list from largest to smallest
    count = len(debts)
    while count > 0:
        index = debts.index(max(debts))
        result.append([names[index], debts[index]])
        del names[index]
        del debts[index]
        count -= 1

    return result
