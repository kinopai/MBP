import random

results = [0] * 6  # 1〜6の出目の回数をカウント

for i in range(10):
    roll = random.randint(1, 6)
    print(f"{i+1}回目: {roll}")
    results[roll - 1] += 1

print("\n出目の回数:")
for i in range(6):
    print(f"{i+1}: {results[i]}回")
