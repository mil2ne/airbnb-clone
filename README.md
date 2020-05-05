airbnb clone practice

-- 환경 --

1. pipenv 설치하여, 사용
2. pipenv install Django==2.2.5 설치하여 사용
3. vscode 사용할거고 , lint 는 flake8 / fomatting 은 black

-- 정리 --
가상접근 : pipenv shell

1. django-admin startproject config

   > config 를 생성하고, /config/config 폴더와 , manage.py 파일을 상위디렉토리로 move ( 상위디렉토리의 config 는 버림 )

2. 한문장으로 설명가능한 수준으로 funtions 분리

   > rooms , users , reviews...
   > ex) rooms 에는 방수정,생성,삭제,예약 만..

3. 함수 생성

   > 함수명은 복수형으로 생성
   > django-admin startapp reviews 등

4. 주의

   > 프레임워크를 사용하고 있기때문에, 파일명/폴더명을 수정해선 안된다. , 그러나 생성하는건 상관없음 (urls.py 등)

5. DB수정후에
   python manage.py makemigrations
   python manage.py migrate

---

python manage.py createsuperuser

### https://docs.djangoproject.com/en/3.0/ref/

1. users app recap
   > users 에서는 admin , models.py 코드 수정
   > 장고는 파이썬 코드를 SQL 문으로 바꿔서 데이터베이스가 알아먹을 수 있게 변경해준다.
   > django는 powerful ORM 기능을 갖고 있다.
   > @admin.register(models.User)는 decorator라 부르고 반드시 class 위에 적어야 한다.
   > config 폴더 안에 setting.py 파일 최하단에 아래 코드를 추가해야 장고가 기본적으로 제공하는 모델을 확장할 수 있다.
   > AUTH_USER_MODEL = "users.User"

2) rooms app 중간 정리

   > 방 또는 리뷰 또는 등등이 생성된 날짜 그리고 업데이트된 날짜를 기록해주는 모델을 만들고 싶은데. 이 모델의 특징은 한번 만들어서 rooms app에서도 사용하고 reviews, reservations....등등 각종 앱에서 이 모델 형식을 모두 동일하게 사용한다. 따라서 중복된 코드를 최소화 하고자. core앱을 만들고 다음과 같이 작성한다.
   > (단, 이때 주의할 점은 반드시 class Meta: abstract = True 를 꼭 !! 해줘야 한다. 실제로 db 에 생성되지는 않고, 추상적으로 만 사용 )

   class TimeStampedModel(models.Model):
   """ Time Stampd Model """
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)

   class Meta:
   abstract = True

   # abstract 모델은 데이터베이스에 반영이 되지 않는 모델이다. 확장하기 위해 작성함.

> "django-contries" package 설치하기.
> 설치참조 url : https://pypi.org/project/django-countries/

Installation
pip install django-countries ( pipenv 환경에서 작업하고 있기 때문에, env 쉘에서 pipenv install django-countries 로 설치)
Add django_countries to INSTALLED_APPS

example>
from django.db import models
from django_countries.fields import CountryField

class Person(models.Model):
name = models.CharField(max_length=100)
country = CountryField()

> ForeignKey() 아주 중요하다. relationship 개념을 알아야한다.
> 이 관계는 크게 두가지로 나뉘는데 하나는 다대일 관계이고 나머지 하나는 다대다관계이다.
> 전자는 ForeignKey라고 하고 후자는 ManyToMany라고 한다.
> 이는 추후 수업에서 review_set 등으로 다시 나오는 개념이다.
> rooms와 users가 서로 연결되어 있으므로 이를 ForeignKey로 지정하였다.
> users가 삭제되면 그 users가 게시했던 rooms, reviews,,,,등등이 모두 한꺼번에 동시에 삭제되어야 하므로 이런 관계설정을 해주는 것이다.

> on_delete=models.CASCADE 에 대한 설명
> django 공식 문서 링크 : https://docs.djangoproject.com/en/3.0/ref/models/fields/
> user를 삭제하면 room도 동시에 삭제되는 로직을 구현하고 싶으므로 CASCADE를 사용

> roomType = models.ForeignKey(RoomType, blank=True, on_delete=models.SET_NULL, null=True)
> 이것은 룸타입을 아무것도 선택하지 않는다 하더라도 룸 자체는 삭제되지 않게 하기 위한 설정
> 특히 이부분입니다 on_delete=models.SET_NULL, null=True
