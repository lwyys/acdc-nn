import pandas as pd
from scipy.stats import pearsonr
from sklearn.metrics import mean_squared_error
import numpy as np

data = pd.read_csv('/home/liang/result4.csv')

# 获取两列数据
column1 = data['3d_ddg']
column2 = data['DDG']

# 计算皮尔逊相关系数
pearson_corr, _ = pearsonr(column1, column2)
print("皮尔逊相关系数:", pearson_corr)

# 计算 RMSE
rmse = np.sqrt(mean_squared_error(column1, column2))
print("RMSE:", rmse)
