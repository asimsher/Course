from .filters import CoursesFilter
from .pagination import CategoryPagination, CoursesPagination, ExamPagination, QuestionsPagination
from .permissions import CheckOwner, CheckCourseOwner, CheckUserReview
from .serializers import *
from .models import *
from rest_framework import viewsets, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class TeacherAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class LinksAPIView(generics.ListAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializers


class CoursesListAPIView(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CoursesFilter
    search_fields = ['course_name']
    ordering_fields = ['price']
    pagination_class = CoursesPagination


class CoursesDetailListAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseDetailSerializers
    permission_classes = [CheckCourseOwner]

class CoursesCreateAPIView(generics.CreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesCreateSerializer
    permission_classes = [CheckOwner]

class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name_lesson']


class LessonDetailAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializers
class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = CoursesCreateSerializer
    permission_classes = [CheckOwner]
    
class AssignmentAPIView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name_assignment']


class ExamListAPIView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name_exam']
    pagination_class = ExamPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ExamCreateAPIView(generics.CreateAPIView):
    serializer_class = ExamCreateSerializers
    permission_classes = [CheckOwner]

class QuestionsAPIView(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name_question']
    pagination_class = QuestionsPagination
class QuestionsCreateAPIView(generics.CreateAPIView):
    serializer_class = QuestionCreateSerializer
    permission_classes = [CheckOwner]

class AnswersAPIView(generics.ListAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer

class CertificateAPIView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateListSerializers


class CertificateCreateAPIView(generics.CreateAPIView):
    serializer_class = CertificateCreateSerializers
    permission_classes = [CheckOwner]
class ReviewAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

