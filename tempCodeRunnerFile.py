import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

from sklearn.datasets import load_iris
data=load_iris()
x=data.data
y=data.target
df=pd.DataFrame(x)
df