def groupingDishes(dishes):
    dict = {}
    
    for dish in dishes:
        dishName = dish.pop(0)
        for ingredient in dish:
            dict.setdefault(ingredient, [])
            dict[ingredient].append(dishName)
        
    arraaay = []
    for key, value in dict.items():
        if len(value) >= 2:
            tmp = []
            for dish in value:
                tmp.append(dish)
            tmp.sort()
            tmp.insert(0, key)
            arraaay.append(tmp)
    
    return sorted(arraaay, key=lambda arraaay_entry: arraaay_entry[0])