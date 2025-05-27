import time

seconds = int(input("何秒カウントダウンしますか？: "))

for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1)  # 1秒待つ

print("時間です！")
