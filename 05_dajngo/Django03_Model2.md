1. 글 작성버튼을 누르면(/articles/new)
2. form 제공
3. form 제출시 (/articles/create)
4. 글작성(db save)
5. detail 페이지로 이동



[views.py] from django.shortcuts import render, redirect



# Update

article = Article.objects.get(pk=pk)

article.title = '수정할 값'

article.content = '수정할 값'

article.save()



Delete



<a href=" {% url 'articles:edit' article.pk %}">

​    <button>수정</button>

  </a>

..



  {{ article.context | linebreaksbr }}   



{% csrf_token %} // csrf토큰 넣어주기 





## 정렬

- id 오름차순이 기본값

airticles = Article.objects.all()

- id 내림차순(python)

articles = Article.objects.all()[::-1]

- id 내림차순(ORM)

articles = Article.objects.order_py('-pl')

- update_at 내림차순

articles = Article.objects.order_boy(''-updated_at')

## search

keyword = '글'

Article.objects.fileter(title__contains=keyword) # 키워드를 포함하고 있는 것들 

## CRUD with views

### CSRF 공격방어 

서버에 요청을 받을 때마다 전달된 token 값이 유효한지 검증 

모든 POST 방식에는 토큰값이 넘어가야함. 

`'django.middleware.csrf.CsrfViewMiddleware',`

`settings` - `MIDDLEWARE` 에서 이 친구가 동작하는 것.

Cross Site Request Forgery(사이트간 요청 위조)

다른 사이트에서 위조한 요청을 보낸게 아닌지 확인하는 것.

## 정리

BASE DIR / templates