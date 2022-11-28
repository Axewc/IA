

# Shannon Entropy Calculator
# parameter: data - string to calculate entropy
# parameter: iterator - number of characters to iterate over
# parameter: base - base of the logarithm
from collections import Counter
import math


def shannon_entropy(data, iterator = 1, base = 2):
    if iterator > len(data):
        return 0
    freqdist = Counter(data[i:i+iterator] for i in range(len(data)-iterator+1))
    probs = [freqdist[ch]/len(data) for ch in freqdist]
    entropy = - sum([p * math.log(p, base) for p in probs])
    return entropy

# main function
def main():
    # read file
    with open("data.txt", "r") as f:
        data = f.read()
    # calculate entropy
    entropy = shannon_entropy(data, iterator = 1)
    # print result
    print("Entropy: %s" % entropy)
