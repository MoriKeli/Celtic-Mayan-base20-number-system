"""
    © 2022 MORI KELI | ALL RIGHTS RESERVED.
    Program created 30/06/2022 0925 hrs EAT
"""
# A program to convert a number from base 10 to base 20.

# Our number system is called base 10 because we have ten digits: 0, 1, . . . , 9. Some cultures,
# including the Mayans and Celts, used a base 20 system. In one version of this system, the 20
# digits are represented by the letters "A" through "T". Here is a table showing a few conversions:
"""
        10| 20    10 | 20      10 | 20       10 | 20
        --+----------+-----------+------------+--------
         0| A       8|I        16|Q         39|BT
         1| B       9|J        17|R         40|CA
         2| C      10|K        18|S         41|CB
         3| D      11|L        19|T         60|DA
         4| E      12|M        20|BA       399|TT
         5| F      13|N        21|BB       400|BAA
         6| G      14|O        22|BC       401|BAB
         7| H      15|P        23|BD       402|BAC

"""

txt_file = open('test-results.txt', 'a')
base20_dict = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',
    11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
}


def base20(n):
    """
        This function converts a number from base 10 to its base 20 equivalent. Each digit in the result is converted to its letter equivalent.
        The 20 digits are represented by the letters "A" through "T" as shown in the table below:

        10| 20    10 | 20      10 | 20
        --+----------+-----------+-------
         0| A       8|I        16|Q
         1| B       9|J        17|R
         2| C      10|K        18|S
         3| D      11|L        19|T
         4| E      12|M        20|BA
         5| F      13|N
         6| G      14|O
         7| H      15|P

    """
    div = n//20     # get the dividend
    rem = n % 20    # get the remainder

    if n in base20_dict:
        print(f'Number base 10: {n}\nNumber base 20: {base20_dict[n]}\n{"---"*30}', file=txt_file)
        return f'Number base 10: {n}\nNumber base 20: {base20_dict[n]}'

    else:
        if div % 20 == 0:
            floor_div = div // 20
            floor_rem = div % 20
            print(f'Number base 10: {n}\nNumber base 20: {base20_dict[floor_div]}{base20_dict[floor_rem]}{base20_dict[rem]}\n{"---" * 30}', file=txt_file)
            return f'Number base 10: {n}\nNumber base 20: {base20_dict[floor_div]}{base20_dict[floor_rem]}{base20_dict[rem]}'

        elif div % 20 != 0 and div not in base20_dict:
            floor_div = div // 20
            floor_rem = div % 20

            print(f'Number base 10: {n}\nNumber base 20: {base20_dict[floor_div]}{base20_dict[floor_rem]}{base20_dict[rem]}\n{"---" * 30}', file=txt_file)
            return f'Number base 10: {n}\nNumber base 20: {base20_dict[floor_div]}{base20_dict[floor_rem]}{base20_dict[rem]}'

        else:

            print(f'Number base 10: {n}\nNumber base 20: {base20_dict[div]}{base20_dict[rem]}\n{"---" * 30}', file=txt_file)
            return f'Number base 10: {n}\nNumber base 20: {base20_dict[div]}{base20_dict[rem]}'


print(base20(n=int(input('Enter a number (base 10): '))))   # display output
