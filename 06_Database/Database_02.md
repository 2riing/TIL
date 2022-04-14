# Database 02

## Foregin Key

다른데이터 베이스와의 관계를 나타내기 위해서 존재 



#### 참조 무결성

#### ForeginKey Field

`on-delete`

- CASCADE : 부모가 삭제 됐을 때 이를 참조하는 객체도 삭제 

```python
article = models.ForeignKey(article, ondelete=models.CASCADE)
```





### Comment CREATE

### Comment READ

### Comment DELETE



## Customizing authentication in Django

### Substituting a custom User model

#### User 모델 대체하기 

`AUTH_USER_MODEL`을 제공하여 override할 수 있도록함

커스텀 유저 모델을 강력하게 권장(개체를 다룰 줄 알아야함)

* 단 migration/migrate를 실행하기 전에 해야함

#### AUTH USER_MODEL

⭐(필수)⭐ 프로젝트가 진행되는 동안 **변경할 수 없음**

(엄밀히 말하면 불가능한 것은 아니지만 어려움)

```PYTHON 
AUTH_USER_MODEL = 'auth.User'
AUTH_USER_MODEL = 'acconts.User'
```

#### Custom User 모델 정의하기

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

초기화 방법: db.sqlite3 파일삭제, migrations파일 모두 삭제 

### Custom user & Built-in auth forms

- UserCreateForm
- UserChangeForm

#### get_user_model()

User 클래스를 직접 참조 X

get_user_modle()을 사용해야함
