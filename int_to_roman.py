def int_to_roman(myint):
    """ takes integer input, and transforms to roman numerals up to 3999 """

    # if adjusting number range, rules currently function
    # only with max numerosity of power of 10
    num2roman = {1000: 'M', 500: 'D',
                 100: 'C', 50: 'L',
                 10: 'X', 5: 'V',
                 1: 'I'}

    magnitudes = list(num2roman.keys())
    magnitudes.sort()   # sort keys / available magnitudes
    magnitudes.reverse()   # reverse order so descending

    # iterate over only powers of 10
    magnitudes = magnitudes[0:len(magnitudes):2]

    curchar = []
    # operate over each power of 10 -- largest to smallest
    try:
        for i in magnitudes:
            numinto = myint // i

            # if myint is 4 or 9x i, special case of one roman numeral
            # larger (5 or 10) prefaced by i
            if numinto == 4 or numinto == 9:
                curchar += num2roman[i] + num2roman[i * (numinto + 1)]

            # if myint is 5x i or larger, special case of 5 + ((myint-5) * i)
            elif numinto >= 5:
                curchar += num2roman[i * 5] + (numinto - 5) * num2roman[i]

            # otherwise can just repeat i numinto times
            else:
                curchar += numinto * num2roman[i]

            myint = myint - (numinto * i)

        return ''.join(curchar)

    except KeyError:
        return 'Input too large'
