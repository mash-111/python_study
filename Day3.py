num = int(input("数字を入力して下さい："))

if num>0:
    print("正の数字です")
elif num<0:
    print("負の数字です")
else:
    print("0です")


total = 0

for i in range(1,11):
    total += i
print("合計", total)


def add(a, b):
    return a+b

result = add(5, 7)
print("結果:", result)