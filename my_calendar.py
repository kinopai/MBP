import calendar

try:
    year = int(input("西暦を入力してください（例: 2024）: "))
    month = int(input("月を入力してください（1〜12）: "))
    
    if month < 1 or month > 12:
        print("月は1から12の間で入力してください。")
    else:
        print(f"\n{year}年{month}月のカレンダー:")
        print(calendar.month(year, month))
except ValueError:
    print("数字を入力してください。")
