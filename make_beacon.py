import pandas as pd

df = pd.read_csv('./info.csv')
prolog = [
    "#FORMAT: BEACON\n",
    "#NAME: OEBL\n"
]

with open('beacon.txt', 'w') as f:
    f.writelines(prolog)
    for i, row in df.iterrows():
        if isinstance(row['gnd'], str) and isinstance(row['doi'], str):
            f.write(f"{row['gnd']}|{row['name']}|{row['doi']}\n")
