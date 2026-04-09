import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
import plotly.express as px

#=========================================
# 1. ダミーデータ
#=========================================
np.random.seed(42)

# 3 Clusters
cluster1 = np.random.normal(loc=[0,0], scale=0.5, size=(100,2))
cluster2 = np.random.normal(loc=[5,5], scale=0.5, size=(100,2))
cluster3 = np.random.normal(loc=[0,5], scale=0.5, size=(100,2))

# Noise Data
noise = np.random.uniform(low=-1, high=7, size=(30, 2))

# Concat
X = np.vstack([cluster1, cluster2, cluster2, noise])
print(X)

# DataFrame
df = pd.DataFrame(X, columns=["x", "y"])
# print(df)

#=========================================
# 2. DBSCAN Clustering
#=========================================
dbscan = DBSCAN(
    eps=0.6,  # 距離閾値
    min_samples=2,  # クラスタ形成最小サンプル数
)

labels = dbscan.fit_predict(df[["x", "y"]])
# print(labels)

# クラスラベルを追加
df["cluster"] = labels.astype(str)
print(df)

#=========================================
# 3. Visualization
#=========================================
fig = px.scatter(
    df,
    x="x", y="y",
    color="cluster",
    title="DBSCAN Clustering Visualizasion",
    width=800,
    height=600
)

fig.show()