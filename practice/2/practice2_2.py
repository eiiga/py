import random

num = 1000
count = 0

# xの2乗とyの2乗の和が1以下の時カウントする
for i in range(num):
    # random()を使用すると0〜1の間でランダムに数字を生成する
    x = random.random()
    y = random.random()
    if x * x + y * y <= 1:
        count += 1

ans = count / num

print(ans)

print(4 * ans)

# 答え：割合を4倍すると円周率（3.14）に近く
