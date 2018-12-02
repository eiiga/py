import numpy as np

# 20人分の点数を格納
score = [80, 78, 84, 69, 77, 73, 88, 64, 91, 72, 75, 62, 90, 83, 92, 60, 76, 89, 68, 70]

# 要素数を確認
# print(len(score))

# 標準偏差を算出
def standardize(x):
    return (x - np.mean(x)) / np.std(x)

# 標準偏差から、それぞれの偏差値を算出し、表示　↓ここから↓
standardize_value = standardize(score)

standardize_score = standardize_value * 10 + 50

print(standardize_score)
# 標準偏差から、それぞれの偏差値を算出し、表示　↑ここまで↑
