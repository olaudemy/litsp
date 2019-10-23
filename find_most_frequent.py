import collections
from collections import Counter
import string

#with imported counter
def find_most_frequent(text):
    text = "".join(w for w in text if w not in string.punctuation)
    text = text.lower().split()
    count = collections.Counter(text)
    value_list = count.values()
    max_num = max(value_list)
    fr = []
    fr = fr.append(key for key, value in count if value == max_num)
    print(fr)
    fr.sort()
    return fr
    
    
#most_frequent2, with own counter
def find_most_frequent2(text):
    text = "".join(w for w in text if w not in string.punctuation)
    text = text.lower().split()
    counter = {}
    for word in text:
        counter[word] = counter.get(word, 0) + 1
    print(counter)
    max_value = max(counter.values())
    most_fr = [key for key, value in counter.items() if value == max_value]
    most_fr.sort()
    print(most_fr)
