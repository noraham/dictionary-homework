"""Print out all the melons in our inventory."""


from melons import (melon_tracking)

def print_all_melons(melon_tracking):
    """prints all known melon details from melon_tracking dictionary in melons.py"""

    for melon, nested_melon_dict in melon_tracking.items():  # iterate through key:values in this dict
        print melon.upper()
        for key, value in nested_melon_dict.items():  # the value from the above iteration happened to be another dictionary, so iterate through the key:values in this dict
            print key + ":", value  # print each key:value on separate line
        print


print_all_melons(melon_tracking)
