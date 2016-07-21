def int_to_roman(myint):
    """ takes integer input, and transforms to roman numerals up to 3999 """
    magnitudes = [1000, 100, 10, 1]
    num2roman = {'1000': 'M', '500': 'D', '100':'C', '50':'L', '10': 'X', '5':'V', '1':'I'}
    curchar = str()
    
    # operate over each magnitude -- largest to smallest
    for i in magnitudes:
        numinto  = myint // i
        # if myint is 4 or 9x i, special case of one roman numeral 
        # larger (5 or 10) prefaced by i 
        if numinto == 4 or numinto == 9:
            curchar += num2roman[str(i)] + num2roman[str(i * (numinto + 1))]  
            curval = numinto * i
            myint = myint - curval
        # if myint is 5x i or larger, special case of 5 + ((myint-5) * i)    
        elif numinto >= 5:
            curchar += num2roman[str(i * 5)] + (numinto - 5) * num2roman[str(i)]  
            curval = numinto * i
            myint = myint - curval
        # otherwise can just repeat i numinto times
        else:
            curchar += numinto * num2roman[str(i)] 
            curval = numinto * i
            myint = myint - curval

    return curchar