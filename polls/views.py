from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.views.generic import(
    ListView,
    DetailView,
)

from .models import Question
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