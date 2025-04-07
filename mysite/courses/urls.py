from rest_framework import routers

from .views import *
from django.urls import path, include

router = routers.SimpleRouter()

router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'students', StudentViewSet, basename='students')


urlpatterns = [
    path( '', include( router.urls ) ),
    path( 'category/', CategoryAPIView.as_view(), name='category_list' ),
    path( 'category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail' ),
    path( '', CoursesListAPIView.as_view(), name='courses_list' ),
    path( 'create/', CoursesCreateAPIView.as_view(), name='courses_create' ),
    path( '<int:pk>/', CoursesDetailListAPIView.as_view(), name='courses_list' ),
    path( 'lesson/', LessonListAPIView.as_view(), name='lesson_list' ),
    path( 'lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson_list' ),
    path( 'lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create' ),
    path( 'assignment/', AssignmentAPIView.as_view(), name='assignment_list' ),
    path( 'exams/', ExamListAPIView.as_view(), name='exma_list' ),
    path( 'exams/create/', ExamCreateAPIView.as_view(), name='exma_list' ),
    path( 'questions/', QuestionsAPIView.as_view(), name='question_list' ),
    path( 'questions/create/', QuestionsCreateAPIView.as_view(), name='question_list' ),
    path( 'certificate/', CertificateAPIView.as_view(), name='certificate_list' ),
    path( 'certificate/create/', CertificateCreateAPIView.as_view(), name='certificate_list' ),
    path( 'review/', ReviewAPIView.as_view(), name='review_list' ),
    path( 'teacher/', TeacherAPIView.as_view(), name='teacher_list' ),
    path( 'teacher/<int:pk>/', CoursesDetailListAPIView.as_view(), name='teacher_detail' ),

]