from django.contrib.auth.models import AbstractUser
from django.db import models

USER_ROLE = (
    ('клиент', 'клиент'),
    ('преподователь', 'преподователь'),
    ('администиратор', 'администиратор'),
)


class UserProfile(AbstractUser):
    full_name = models.CharField(max_length=35)
    profile_picture = models.ImageField(default='клиент')
    bio = models.TextField()
    role = models.CharField( max_length=25, choices=USER_ROLE, default='клиент' )

    def __str__(self):
        return self.username


class Teacher(UserProfile):
    experience = models.PositiveSmallIntegerField()
    teacher_role = models.CharField(max_length=25, choices=USER_ROLE, default='преподователь')

    class Meta:
        verbose_name = 'Teacher'

    def __str__(self):
        return self.username


class Student(UserProfile):
    student_role = models.CharField(max_length=25, choices=USER_ROLE, default='клиент')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Student'


class Links(models.Model):
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
    links_url = models.URLField()

    def __str__(self):
        return f'{self.students}, {self.links_url}'


class Category(models.Model):
    category_name = models.CharField(max_length=34)

    def __str__(self):
        return self.category_name


COURSE_LEVEL_CHOUCES = (
    ('начальный', 'начальный'),
    ('средний', 'средний'),
    ('предвинутый', 'предвинутый'),
)


class Courses(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=65)
    description = models.TextField(null=True, blank=True)
    level = models.CharField(max_length=20, choices=COURSE_LEVEL_CHOUCES, default='начальный')
    price = models.DecimalField(max_digits=10, decimal_places=2, )
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.category} - {self.course_name}'


class Lesson(models.Model):
    name_lesson = models.CharField(max_length=32)
    video_url = models.URLField()
    content = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='course_lesson')
    def __str__(self):
        return f'{self.name_lesson} - {self.content}'


class Assignment(models.Model):
    name_assignment = models.CharField(max_length=35)
    description = models.TextField()
    dua_date = models.DateTimeField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    students = models.ManyToManyField(UserProfile, related_name='students')


    def __str__(self):
        return f'{self.name_assignment}, {self.course}'
class Exam(models.Model):
    name_exam = models.CharField(max_length=43)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    passing_score = models.PositiveSmallIntegerField()
    duration = models.TimeField()

    def __str__(self):
        return self.name_exam

class Questions(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    name_questions = models.CharField(max_length=32)


    def __str__(self):
        return self.name_questions

class Answers(models.Model):
    questions = models.ForeignKey(Questions, on_delete=models.ForeignKey)
    answers = models.CharField(max_length=64)
    true_answers = models.BooleanField()


class Certificate(models.Model):
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    issued_at = models.DateField(auto_now_add=True)
    certificate_file = models.FileField(upload_to='certificate_file')


class Review(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()







