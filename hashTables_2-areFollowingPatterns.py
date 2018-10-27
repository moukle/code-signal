def areFollowingPatterns(strings, patterns):
    dictA = {}
    dictB = {}

    for i in range(len(strings)):
        dictA[patterns[i]] = strings[i]
        dictB[strings[i]] = patterns[i]
        
    for i in range(len(strings)):
        if dictA[patterns[i]] != strings[i]:
            return False
        if dictB[strings[i]] != patterns[i]:
            return False
    return True