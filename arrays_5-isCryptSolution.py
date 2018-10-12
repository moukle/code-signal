def isCryptSolution(crypt, solution):
    i = 0
    words = []
    for w in crypt:
        word = ""
        for c in w:
            index = [i for i, x in enumerate(solution) if x[0] == c][0]
            word += solution[index][1]
        words.append(word)
        i+=1
    
    for w in words:
        if w[0] == '0' and len(w) > 1:
            return False
        
    return int(words[0]) + int(words[1]) == int(words[2])