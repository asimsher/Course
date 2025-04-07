from rest_framework import serializers
from .models import *



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'profile_picture', 'bio']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['full_name']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['full_name', 'profile_picture', 'bio']


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ['id', 'students', 'links_url']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class CourseListSerializers(serializers.ModelSerializer):
    category = CategorySerializer()
    created_by = TeacherSerializer()

    class Meta:
        model = Courses
        fields = ['id', 'category', 'course_name', 'created_by', 'price', 'level']

class CoursesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class LessonListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name_lesson']

class LessonDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name_lesson', 'video_url', 'content']

class LessonCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = ['id', 'name_assignment', 'description', 'dua_date', 'course', 'students']


class ExamListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['name_exam', 'course', 'passing_score', 'duration']


class ExamCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'



class QuestionListSerializer(serializers.ModelSerializer):
    exam = ExamListSerializers()
    class Meta:
        model = Questions
        fields = ['exam', 'name_questions']

class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ['id', 'questions', 'answers', 'true_answers']


class CertificateListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['issued_at', 'certificate_file']

class CertificateCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'course', 'rating', 'comment']


class CategoryDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name',]


class CourseDetailSerializers(serializers.ModelSerializer):
    created_by = TeacherSerializer()
    course_lesson = LessonListSerializers(read_only=True, many=True)
    ratings = ReviewSerializer(read_only=True, many=True)
    created_at = serializers.DateTimeField(format('%d-%m-%Y'))
    updated_at = serializers.DateTimeField(format('%d-%m-%Y'))
    class Meta:
        model = Courses
        fields = ['course_name', 'description', 'level', 'price', 'course_lesson',
                  'created_by', 'ratings', 'created_at', 'updated_at']