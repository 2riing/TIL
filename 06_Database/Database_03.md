# Database_03

## 1:N 관계 설정

### User-Article

#### django에서 User 모델 참조하기

1. `settings.AUTH_USER_MODEL1` (models.py)

2. `get_user_model()` (models.py를 제외한 다른 모든 곳)

#### Delete 

자신이 쓴 글만 삭제할 수 있도록 설정

```python
if request.user.is.authenticated:
```

### User- Comment

