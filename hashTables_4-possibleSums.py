def possibleSums(coins, quantity):
    sums = {0}
    
    for c, q in zip(coins, quantity):
        new = {}
        for i in range(1, q+1):
            for sum in sums:
                tmp = sum + i * c
                if tmp not in sums:
                    new[tmp] = tmp
        sums.update(new)
    
    return len(sums) - 1