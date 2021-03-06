from django.db import models

# Create your models here.

class Lecture(models.Model):
    title = models.CharField(max_length=200)
    room = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.pk} : {self.title}'


class Student(models.Model):
    name = models.CharField(max_length=10)
    major = models.CharField(max_length=10)
    lectures = models.ManyToManyField(
        Lecture,
        through = 'Enrollment', # 커스텀 중계모델
        related_name='students',
    )

    def __str__(self):
        return f'{self.pk} : {self.title}'


class Enrollment(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField(default=0)
    semester = models.CharField(max_length=100, default='22-1')


