def sum_pairs (num_list , sum_val):
    fill_return = {}
    for num in num_list:
        temp = sum_val - num
        if temp in fill_return.values ():
            return list ((temp , num))
        else:
            fill_return[ temp ] = num

    return None
