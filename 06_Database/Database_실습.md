장고, 익스텐션, ipython설치 

$ pip install django==3.2.12 django_extensions ipython[kernal]



requirement.txt 만들어주기

$ pip freeze > requirements.txt



base dir설정

 'DIRS': [BASE_DIR /'templates'],



models.py

```python
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.id}>{self.content}'
```







$ python manage.py shell_plus --print-sql





python manage.py shell_plus --print-sql

a1 = Article.objects.get(pk=1)

c1 = Comment.objects.get(pk=1)



c1.article

a1.comment_set.all()

Article.objects.all()

Comment.objects.filter(article_id = 1)



`settings.py`

AUTH_USER_MODEL = 'accounts.User'