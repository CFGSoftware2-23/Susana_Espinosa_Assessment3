def count_unique_consonants(input_str):
    consonants = "bcdfghjklmnpqrstvwxyz"
    unique_consonants = set()

    for char in input_str:
        if char.lower() in consonants:
            unique_consonants.add(char.lower())

    return len(unique_consonants)


# This is the result
input_str1 = "susana"
output1 = count_unique_consonants(input_str1)
print(output1)



# b)The time complexity of the solution is O(n), where "n" is the length of the input string. This is because the solution
# iterates through each character in the input string exactly once, performing constant-time operations for each character.
#
# The space complexity of the solution is O(k), where "k" is the number of unique consonants in the input string. In the worst
# case, if all characters in the input string are unique consonants, the set unique_consonants will store all of them. Thus,
# the space used by the set is proportional to the number of unique consonants.
#
# Assumptions:
#
# -The solution treats consonants as English consonants (excluding vowels and non-alphabetic characters).
# -The solution converts all characters to lowercase before checking for consonants, assuming case-insensitive matching.
# -The assumption is made that the set data structure used for storing unique consonants has a constant time complexity for insertion and lookup operations.
