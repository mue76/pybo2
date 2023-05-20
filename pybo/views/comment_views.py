from django.shortcuts import render, get_object_or_404, redirect
from ..models import Question
from django.utils import timezone
from ..forms import CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    """
    pybo 질문 댓글 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = CommentForm()
    context = {'form':form}
    return render(request, 'pybo/comment_form.html', context)