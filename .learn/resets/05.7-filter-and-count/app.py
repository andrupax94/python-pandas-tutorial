import pandas as pd
# Array bidimensional con valores [name, age]
pokemones=pd.DataFrame(pd.read_csv('.learn/assets/pokemon_data.csv'))

cantidad=len(pokemones.loc[pokemones.loc["Legendary"]==True])
# Imprime el DataFrame
print(cantidad)