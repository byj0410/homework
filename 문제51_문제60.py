#51
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#52
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#53
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

#54
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

#55
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

#56^ join()을 사용하면 모든 데이터를 하나의 문자열로 만듦, " "은 이어붙일 때 공백 삽입
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

#57^
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

#58^
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))

#59^
string = "삼성전자/LG전자/Naver"
interest=[]
interest.append(string[0:4])
interest.append(string[5:9])
interest.append(string[10:16])

#60^ split는 문자열을 리스트로 변환, " "에 있는 것을 기준으로 문자열을 자르고 저장
string = "삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"
interest=string.split("/")
