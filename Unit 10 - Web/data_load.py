import pandas as pd
import numpy as np

df = pd.read_csv("Resources/cities.csv")
df.to_html('data_copy.html', classes=["table-bordered", "table-striped", "table-hover"])