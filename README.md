# DRF 기초

220615  
django 1~2일차 과제

(1) args, kwargs를 사용하는 예제 코드 짜보기  
*args : 가변 인자 (함수의 인자를 몇 개 받을지 모르는 경우)  
초기 로직(직접 짜본 것)  
def test_1(*args):  
      print(args)  
      return args  

sample_list = [1, 2, 3, 4, 5]  
number = test_1(*sample_list)  

for i in number:  
print(i + 1)

개선 로직(구글링)  
def test_1(*args):  
    result = 0  
    for i in args:  
        result += i  
        # result = 1  
        # result = 1 + 2  
        # result = 1 + 2 + 3  
        # result = 1 + 2 + 3 + 33  
    print(result)  

test_1(1, 2, 3, 33)  

**kwargs : args 와 같으면서도 다른, 딕셔너리 형태의 값 전달  
def test_2(**kwargs):  
    print(kwargs)  


test_2(name="홍길동", age="20")  
{'key' : 'value'}  
name, age = key  
"홍길동", "20" = value  

===============================================================

(2) mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기  
mutable : 변경 가능  
자료형 : 리스트, 딕셔너리, 집합  
immutable : 변경 불가능  
자료형 : 정수, 실수, 문자열, 튜플  

immutable 예시  
a의 전역변수 선언  
a = 1  
def var(a):  
    a = a + 1  
var(a)  
print(a)  

===============================================================

(3) DB Field에서 사용되는 Key 종류와 특징 서술하기  
key : 데이터베이스에서 조건에 만족하는 튜플을 찾거나 순서대로 정렬할 때 다른 튜플들과 구별할 수 있는 유일한 기준이 되는 속성  
FK : Foreign Key(외래키)  
- 참조되는 릴레이션의 기본키와 대응되어 릴레이션 간에 참조 관계를 표현하는데 중요한 도구  
- 외래키로 지정되면 참조 테이블의 기본키에 없는 값은 입력할 수 없음  

UK : Unique Key  
- PK(외래키) 와 유사하나 NULL 값을 중복 허용함  
- 테이블 내에서 해당 컬럼 값은 항상 유일  
- 테이블 내에서 여러번 지정 가능  

PK : Primary Key(기본키)  
- 특정 튜플을 유일하게 구별할 수 있는 속성
- Null 값을 가질 수 없음  
- 동일한 값이 중복되어 저장될 수 없음  

CK : Candidate Key(후보키)  
- 유일하게 식별할 수 있는 속성들의 부분집합을 의미  
- 모든 릴레이션은 반드시 하나 이상의 후보키를 가져야 함  
- 유일성과 최소성을 만족시켜야 함  

AK : Alternate Key(대체키)  
- CK 가 둘 이상일 때 기본키를 제외한 나머지 CK  
- 보조키라고도 함  

SK : Super Key(슈퍼키)  
- 슈퍼키는 한 릴레이션 내에 있는 속성들의 집합  
- 유일성은 만족하지만, 최소성은 만족시키지 못함  

===============================================================

(4) django에서 queryset과 object는 어떻게 다른지 서술하기  

Queryset
- 데이터베이스에서 전달받은 객체들의 모음(list)
- DB(SQL) 에서는 row 에 해당
- DB의 객체를 불러오기 위해서는 iterate 시켜야 한다.
- for account in account_set:  
	print(account.name)
  
queryset과 object는 어떻게 다른지?
- object 메서드와 all() 함수를 포함한 다양한 함수를 통해 queryset() 리스트의 value 값을 가져온다.
- Queryset 은 데이터베이스에서 전달받은 객체들의 모음(list)
- object 는 Queryset 의 데이터를 활용하기 위한 명령어(ORM)

object 종류
- object.all() : 모든 데이터를 가져옴
- object.filter() : 특정 데이터로 필터링(필드명=조건값)해서 가져옴
- object.exclude() : 특정 데이터를 제외한(필드명=조건값) 나머지 데이터를 가져옴
- object.get() : 필드명=조건값 을 인자로 가져, 해당하는 데이터가 유일하게 존재해야 함
- object.first() : 가장 첫번째 데이터를 가져옴
- object.last() : 가장 마지막 데이터를 가져옴
- object.index(), slice() : python 의 list 와 같이 인덱싱 및 슬라이싱이 가능
