def findProfession(level, pos):
    if level == 1:
        return "Engineer"
    else:
        parent = findProfession(level-1, (pos+1) // 2)
        
        if parent == "Engineer" and (pos-1) % 2 == 0:
            return "Engineer"
        elif parent == "Engineer" and (pos-1) % 2 == 1:
            return "Doctor"
        elif parent == "Doctor" and (pos-1) % 2 == 0:
            return "Doctor"
        elif parent == "Doctor" and (pos-1) % 2 == 1:
            return "Engineer"