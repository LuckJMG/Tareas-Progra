def repetidos(listA, listB):
    # Variables
    repeated = 0
    tmpA = []

    # Eliminated repeated elements in listA
    for element in listA:
        if element not in tmpA:
            tmpA.append(element)

    # Count equal elements between listA and listB
    for element in tmpA:
        if element in listB:
            repeated += 1

    return repeated
