from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse

from django.views.generic import(
    ListView,
    DetailView,
)

from .models import Question, Choice
'''
def list_view(request):
    queary_set = Question.objects.all()

    context = {
        'title' : 'Polls',
        'object_list': queary_set
        }


    return render(request, 'polls/polls_list.html', context)
'''

class Polls_list_view(ListView):
    template_name = 'polls/polls_list.html'
    model = Question
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Polls'
        return context


class Polls_detail_view(DetailView):
    template_name = 'polls/polls_detail.html'
    queryset = Question.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Question, id=id_)
    
"""
class blog_view(DetailView):
    queryset = Blog.objects.all()
    
    def get_object(self):
        title_ = self.kwargs.get('blog_title')
        return get_object_or_404(Blog, title=title_)
"""

def Vote(request, id, *args, **kwargs):
    question_ = get_object_or_404(Question, id=id)
    queryset = get_list_or_404(Choice, question = question_)
    context = {
        'question'    : question_,
        'object_list' : queryset,
    }
    vote = request.POST.get('vote_given')
    if request.method == 'POST' and vote is not None :

        choice_voted  = Choice.objects.get(choice_text=vote, question = question_)

        #vote saving
        question_.votes+=1
        choice_voted.votes+=1

        question_.save()
        choice_voted.save()
        
    return render(request, 'polls/polls_vote.html', context)

