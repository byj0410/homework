#71^
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b = scores 
*valid_score, _, _ = scores # a, b를 사용할 필요가 없을 때 _로 대

#72^
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, _, *valid_score = scores

#73^
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, *valid_score, _ = scores

#74^ 중괄호는 딕셔너리를 정의
temp={}

#75^
icecream_price={'메로나':1000, '폴라포':1200, '빵빠레':1800}

#76^ 딕셔너리에 요소 추가
temp['죠스바']=1200
temp['월드콘']=1500

#77^
print("메로나 가격:", icecream_price['메로나'])

#78^ 딕셔너리 요소 수정
icecream_price['메로나']=1300

#79^
del icecream_price['메로나']

#80^ 딕셔너리에 누가바가 존재하지 않음
