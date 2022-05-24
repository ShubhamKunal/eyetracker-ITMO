import re
import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans2, whiten

with open('eyepoints.csv','r') as f:
    data = f.read()
df = pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
# To replace all line breaks in all textual columns
for col in df.columns: 
    if df[col].dtype == np.object_:
        df[col] = df[col].str.replace('\n','');
# df.to_csv('./output.csv')
# print(df.values)
coordinates = np.array(df.values)
print(coordinates)
x,y = coordinates.T
plt.scatter(x,y)
plt.show()