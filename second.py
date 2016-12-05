# Create a function that takes a filename and a string as parameter,
# And writes the string got as second parameter into the file 10 times.
# If the writing succeeds, the function should return True.
# If any problem raises with the file output, the function should not break, but return False.
# Example: when called with the following two parameters: "tree.txt", "apple",
# the function should write "appleappleapple" to the file "tree.txt", and return True.

def string_writer(file_name, string):
    try:
        f = open(file_name, "w")
        f.write(string * 10)
        f.close()
        return True
    except:
        return False

print(string_writer("jam.txt", "strawberry"))

# def another_writer(file_name, string):
#     try:
#         f = open(file_name, "w")
#         for x in range(10):
#             f.write(string)
#         return True
#     except:
#         return False
#
# print(another_writer("jam.txt", "strawberry"))
