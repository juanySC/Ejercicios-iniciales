from upsetplot import UpSet, from_memberships
import matplotlib.pyplot as plt

# Convertimos los conjuntos en listas de membresía
memberships = []
data_values = []

for combo in zip(*sets.values()):
    memberships.append(tuple(sorted(combo)))
    data_values.append(1)

# Si querés hacerlo bien a partir del diccionario de sets:
from itertools import chain, combinations

def get_memberships(sets_dict):
    all_elements = set(chain.from_iterable(sets_dict.values()))
    memberships = []

    for element in all_elements:
        present_in = tuple(k for k, v in sets_dict.items() if element in v)
        memberships.append(present_in)
    return memberships

# Generamos data
data = from_memberships(get_memberships(sets), data=1)
upset = UpSet(data)
upset.plot()
plt.show()



