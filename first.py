# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the original list.
# It should raise an error if the parameter is not a list.
# Example: with the input [1, 2, 3, 4, 5] it should return [2, 4].

orig_list = [23, 564, 24, 897, 413, 943, 123, 666]
nonlist = "lobab"

def every_second_element(input_list):
    if type(input_list) != list:
        raise TypeError("Not a list, fool!")
    else:
        newlist = []
        for x in range(len(input_list)):
            if x % 2 == 1:
                newlist.append(input_list[x])
        return newlist

print(every_second_element(orig_list))
# print(every_second_element(nonlist))
