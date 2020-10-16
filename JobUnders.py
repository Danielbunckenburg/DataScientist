import csv
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

Data = pd.read_excel('test1.xlsx')

Data2 = Data[['Titel','ledighed_nyudd']]

Datasetecon = []


for i in range(len(Data2)):
    if Data2.Titel[i] == 'Økonomi':
        Datasetecon.append(Data.ledighed_nyudd[i])
    else:
        pass

print(Datasetecon)