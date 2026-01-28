import pandas as pd
# Array bidimensional con valores [name, age]
names=pd.DataFrame(pd.read_csv('.learn/assets/us_baby_names_right.csv'))
agrupacion= len(names.groupby("Name").sum())

# Imprime el DataFrame
print(agrupacion)