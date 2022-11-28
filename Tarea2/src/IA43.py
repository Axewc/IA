

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
    data1 = '010100110001110101001100011101010011000111'
    data2 = '000000000000000000000000000000000000000000'
    data3 = '010101010101101101110110010101010010111010'
    
    entropy = shannon_entropy(data, iterator=1)
    entropy1 = shannon_entropy(data, iterator=1)
    entropy2 = shannon_entropy(data2, iterator=1)
    entropy3 = shannon_entropy(data3, iterator=1)
    # print result
    print("Entropy: %s" % entropy)
    print("Entropy: %s" % entropy1)
    print("Entropy: %s" % entropy2)
    print("Entropy: %s" % entropy3)
    
main();
# 010100110001110101001100011101010011000111
# 000000000000000000000000000000000000000000
# 010101010101101101110110010101010010111010
