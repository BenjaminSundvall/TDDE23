def sifsum(wt_list):
    summa = 0
    for i in wt_list:
        summa += i%10 + i//10
    return(summa)


def check_pnr(pnr):
    weights = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    weighted_list = []

    for i in range(9):
        weighted_list.append(pnr[i] * weights[i])

    summa = sifsum(weighted_list)
    
    nearest_ten = (summa + 9) // 10 * 10
    
    ctrl = nearest_ten - summa

    return(ctrl == pnr[-1])

# blanda inte språk på variabelnamn
