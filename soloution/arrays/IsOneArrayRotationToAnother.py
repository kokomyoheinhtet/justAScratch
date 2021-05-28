# Implement your function below.
def is_rotation(list1, list2):
    if len(list1) != len(list2):
        return False

    key = list1[0]
    key_location = -1

    for i in range(len(list2)):
        if key == list2[i]:
            key_location = i
            break

    if key_location < 0:
        return False

    for i in range(len(list1)):
        if list1[i] != list2[(i + key_location) % len(list2)]:
            return False

    return True


# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
# is_rotation(list1, list2a) should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
# is_rotation(list1, list2b) should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
# is_rotation(list1, list2c) should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
# is_rotation(list1, list2d) should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
# is_rotation(list1, list2e) should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
# is_rotation(list1, list2f) should return True.
list2g = [7, 1, 2, 3, 4, 5, 6]
# is_rotation(list1, list2g) should return True.

print(is_rotation(list1, list2a))
print(is_rotation(list1, list2b))
print(is_rotation(list1, list2c))
print(is_rotation(list1, list2d))
print(is_rotation(list1, list2e))
print(is_rotation(list1, list2f))
print(is_rotation(list1, list2g))
