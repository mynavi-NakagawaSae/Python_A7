#人数の入力
children = int(input("子供料金（13歳未満）は何人？"))
normal = int(input("通常料金（13‐64歳）は何人？"))
elder = int(input("年配者料金（65歳以上）は何人？"))

total_num = children + normal + elder
children_price = children*500
normal_price = normal*1000
elder_price = elder*700 
total_price = children_price + normal_price + elder_price
#割引
if total_num >=10:
    print("団体割引があります")
    total_price=total_price*0.8
else:
    print("割引はありません")
#結果を表示
print("子供料金　：{0}人×500={1}".format(children,children_price))
print("通常料金　：{0}人×1000={1}".format(normal,normal_price))
print("年配者料金　：{0}人×800={1}".format(elder,elder_price))
print("合計:{0}人{1}円".format(total_num,total_price))
