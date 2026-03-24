from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # Route for submitting the exam for a specific course
    path(
        '<int:course_id>/submit/',
        views.submit,
        name='submit'
    ),
    
    # Route for showing the exam results after submission
    path(
        'course/<int:course_id>/submission/<int:score>/<str:grade>/result/',
        views.show_exam_result,
        name='show_exam_result'
    ),
]
