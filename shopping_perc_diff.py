def solution(prices, notes, x):
    '''
    prices = online prices
    notes = higher/lower than instore price
    x = price overpay limit 

    ex: prices = [110, 95, 70]
        notes = ["10.0% higher than in-store", 
         "5.0% lower than in-store", 
         "Same as in-store"]
        x = 5

    determines whether a given customer will be willing to pay for the given items 
    in their cart based on their stated price sensitivity x.
    '''

    percdiff = []
    total = [] # in store price
    final = [] # online - instore
    for i in notes:
        if i == 'Same as in-store':
            percdiff.append(0)
        elif i != 'Same as in-store':
            # append note2 with percentage difference
            if 'higher' in i:    
                percent_diff = float((i.split('%')[0]))
                percdiff.append(percent_diff)
            elif 'lower' in i:
                percent_diff = -abs(float((i.split('%')[0])))
                percdiff.append(percent_diff)
            
    # number of dollars more or less
    for price, perc in zip(prices, percdiff):
        if perc == 0:
            total.append(price)
        elif perc > 0:
            total.append(price / (abs(perc)/100 + 1))
        elif perc < 0:
            total.append(price / (1 - abs(perc)/100))
            
    for online, instore in zip(prices, total):
        final.append(round(online - instore, 4))

    if sum(final) > x:
        return False
    elif sum(final) <= x:
        return True
    