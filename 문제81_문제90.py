#81
inventory = {'메로나':[300, 20], '비비빅':[400, 3], '죠스바': [250, 100]}

#82^
print(inventory['메로나'][0])
item=inventory['메로나'] # 딕셔너리에 있는 값을 리스트로 받아옴
print(item[0]) # 같은 코

#83^
print(inventory['메로나'][1])

#84
inventory['월드콘']=[500, 7]

#85^ 딕셔너리이름.keys(), 이것은 list(icecream.keys()) 사용해서 리스트로 변경 가능
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(icecream.keys())

#86^ 딕셔너리이름.values
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(icecream.values())

#87^
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
sum(icecream.values())

#88^ update()는 기존 딕셔너리에 새로운 딕셔너리를 추가해줌.
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

#89^ zip은 두 개의 자료 구조를 하나로 묶어줌.
keys = ('apple', 'pear', 'peach')
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

#90^
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table =dict(zip(date, close_price))
print(close_table)
