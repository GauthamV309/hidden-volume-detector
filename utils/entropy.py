import math
from collections import Counter

def calculate_entropy(data):
    if not data:
        return 0
    counter = Counter(data)
    total = len(data)
    entropy = -sum(count / total * math.log2(count / total) for count in counter.values())
    return entropy