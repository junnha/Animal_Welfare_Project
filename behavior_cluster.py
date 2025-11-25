from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


# (3개 상태로 가정)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X_scaled)

cluster_means = df.groupby('cluster')['acc_magnitude'].mean().sort_values()
print("클러스터별 평균 가속도:\n")
print(cluster_means)

#클러스터 번호를 매핑
mapping = {cluster_means.index[0]: 'rest',
            cluster_means.index[1]: 'normal',
            cluster_means.index[2]: 'overactive'}

df['state'] = df['cluster'].map(mapping)

#시각화
plt.figure(figsize=(14,5))
plt.scatter(df.index, df['acc_magnitude'], c=df['cluster'], cmap='viridis', s=2)
plt.title('Clustered Animal Activity Patterns (K-Means)')
plt.xlabel('Time')
plt.ylabel('Acceleration Magnitude')
plt.show()
