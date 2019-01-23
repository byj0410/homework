#61 ['삼성전자', 'LG전자', 'SK Hynix']

#62 ['삼성전자', 'LG전자', 'SK Hynix']

#63^
my_variable=()

#64^ 튜플은 요소의 값을 변경할 수 없다.

#65^ 튜플에 하나의 데이터 저장할 때는 쉼표를 입력해야 한다.
my_tuple=(1,)

#66^ 튜플, 원칙적으로 튜플은 괄호와 함께 정의해야하지만 괄호 없이도 동작한다.
t = 1, 2, 3, 4
print(type(t))

#67^ upper()을 통해 소문자를 대문자
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
t=(t[0].upper(), t[1], t[2])

#68^
interest_tuple = ('삼성전자', 'LG전자', 'SK Hynix')
interest_list= list(interest_tuple)

#69^
interest_list = ['삼성전자', 'LG전자', 'SK Hynix']
interest_tuple=tuple(interest_list)

#70^ 6 우변 튜플에 저장된 값이 좌변의 변수에 차례대로 들어간다. 단 우변과 좌변의 개수는 동일해야 함.
my_tuple = (1, 2, 3)
a, b, c = my_tuple
# 같은 기능
a = my_tuple[0]
b = my_tuple[1]
c = my_tuple[2]
