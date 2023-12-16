import numpy as np;

print("size = None");
print(np.random.uniform(low=-10, high=10, size=None));
print("size inteiro");
print(np.random.uniform(low=-10, high=10, size=1));
print("size com tupla de inteiros");
print(np.random.uniform(low=-10, high=10, size=(5, 2, 3)));

# Size determina o tamanho do resultado na saída
# Se for um número inteiro N, então é gerada uma lista com N valores
# Se for uma tupla de inteiros (a, b, c), por exemplo, são geradas "a"
#   listas, onde cada elemento dela é uma lista com "b" elementos, que 
#   por sua vez também são listas, cada um com "c" elementos
#   Por exemplo, com (2, 3) seria gerado algo como:
#       [   
#           [6,2  8,2  -5,2]
#           [5,2  -1,2  8,5]
#       ]
#       (uma lista com 2 sublistas e cada uma tendo 3 elementos)