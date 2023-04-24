from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Assignment, Course, Enrollment, Lesson, Progress, Submission
from .serializers import AssignmentSerializer, CourseSerializer, EnrollmentSerializer, LessonSerializer, ProgressSerializer, SubmissionSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class LessonViewSet(viewsets.ModelViewSet):
    queryset= Lesson.objects.all()
    serializer_class=LessonSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer


from rest_framework.permissions import IsAuthenticated


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    #permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(instructor=self.request.user.instructor)

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    #permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(student=self.request.user.student)    

