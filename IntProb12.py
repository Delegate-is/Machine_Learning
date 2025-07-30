# Find most frequent value in a list
list = [1, 2, 3, 4, 5, 1, 2, 1]
from collections import Counter
most_common = Counter(list).most_common(1)
print("Most frequent value:", most_common[0][0])
print("Frequency:", most_common[0][1])

from statistics import mode
list_1 = [1, 2, 3, 4, 5, 1, 2, 1]
print(list_1)
print(mode(list_1))
# Find less frequent value in a list
def find_least_frequent(lst):
    from collections import Counter
    frequency = Counter(lst)
    least_common = frequency.most_common()[-1]
    return least_common[0], least_common[1]
lst = [1, 2, 3, 4, 5, 1, 2, 1]
least_value, least_freq = find_least_frequent(lst)
print("Least frequent value:", least_value)
print("Frequency:", least_freq)