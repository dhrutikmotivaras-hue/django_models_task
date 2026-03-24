from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from .models import Course, Lesson, Question, Choice, Submission

def submit(request, course_id):
    """
    Function to handle the submission of answers for a course exam.
    """
    course = get_object_or_404(Course, pk=course_id)
    
    if request.method == 'POST':
        # Retrieve the selected choices from the submitted form data
        selected_choices = request.POST.getlist('choice')
        choices = Choice.objects.filter(id__in=selected_choices)

        total_questions = course.question_set.count()
        correct_answers = choices.filter(is_correct=True).count()
        
        # Calculate the score percentage
        score = (correct_answers / total_questions * 100) if total_questions > 0 else 0
        grade = score >= 80  # Assume 80% is the passing mark

        # Save submission results mapping back to questions and choices
        for choice in choices:
            Submission.objects.create(question=choice.question, choice=choice)

        return redirect('show_exam_result', course_id=course.id, score=score, grade=grade)

    return render(request, 'onlinecourse/exam_submission_form.html', {'course': course})


def show_exam_result(request, course_id, score, grade):
    """
    Function to display the exam result after submission.
    """
    course = get_object_or_404(Course, pk=course_id)
    
    context = {
        'course': course,
        'score': score,
        'passed': grade,
    }
    return render(request, 'onlinecourse/exam_result.html', context)
