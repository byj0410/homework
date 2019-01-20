lang='python' #21
print(lang[0], lang[2])


license_plate="24가 2210" #22^
print(license_plate[4:8])
print(license_plate[4:])
print(license_plate[-4:])


string="홀짝홀짝홀짝" #23^
print(string[0]+string[2]+string[4])
print(string[::2]) # 두 개씩 건너뛰며 값을 가져옴.
print(string[1::2]) # 짝만 출력


string="PYTHON" #24^
print(string[5:0])
print(string[::-1]) # 증감폭을 음수로 지정하면 역순으로 문자들 가져옴


phone_number="010-111-2222" #25
print(phone_number[0:3], phone_number[4:7], phone_number[8:12])
replace=phone_number.replace('-', ' ') # 다른 방법1
print(replace) # 다른 방법1
print(phone_number[0:3], phone_number[4:7], phone_number[8:12], sep=' ') # 다른 방법2


print(phone_number[0:3]+phone_number[4:7]+phone_number[8:12]) #26


url = "http://sharebook.kr" #27^
print(url[-2:])


#28^ 기존에 생성한 문자열은 변경할 수 없다. 에러 발생한다.


string = 'abcdfe2a354a32a' #29^
revise=string.replace('a', 'A')
print(revise)


string = 'abcd' #30^ abcd replace는 기존의 문자열을 변경하는 것이 아니라 변경된 문자열을 새롭게 생성
new_string=string.replace('b', 'B')
print(string)
print(new_string)
