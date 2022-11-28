

# Calculadora de entropía de Shannon
# parametro data: cadena para calcular la entropía
# parametro iterator: número de iteraciones para calcular la entropía
# parametro base: base del logaritmo
from collections import Counter
import math

# Función para calcular la entropía de Shannon
def shannon_entropy(data, iterator = 1, base = 2):
    if iterator > len(data):
        return 0
    freqdist = Counter(data[i:i+iterator] for i in range(len(data)-iterator+1)) # Contador de frecuencias
    probs = [freqdist[ch]/len(data) for ch in freqdist] # Probabilidad de cada símbolo
    entropy = - sum([p * math.log(p, base) for p in probs]) # Entropía
    return entropy

# Función main para probar el código
def main():
    # datos de prueba
    data1 = '010100110001110101001100011101010011000111'
    data2 = '000000000000000000000000000000000000000000'
    data3 = '010101010101101101110110010101010010111010'
    
    # Prueba de la función
    entropy1 = shannon_entropy(data1, iterator=1)
    entropy2 = shannon_entropy(data2, iterator=1)
    entropy3 = shannon_entropy(data3, iterator=1)
    
    # Resultados
    print("Entropy: %s" % entropy1)
    print("Entropy: %s" % entropy2)
    print("Entropy: %s" % entropy3)
    
main();