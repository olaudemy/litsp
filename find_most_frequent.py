import collections
from collections import Counter
import string

def find_most_frequent(text):
    text = "".join(w for w in text if w not in string.punctuation)
    text = text.lower().split()
    count = collections.Counter(text)
    value_list = count.values()
    max_num = max(value_list)
    fr = []
    for key, value in count.items():
        if value == max_num:
            fr.append(key)
        else:
            pass
    fr.sort()
    print(fr)
