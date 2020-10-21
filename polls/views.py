from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse

from django.views.generic import(
    ListView,
    DetailView,
)
#ADDED FXNS
from .extra import get_client_ip, add_ip, has_voted

from .models import Question, Choice, Voters


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
    

def Vote(request, id, *args, **kwargs):
    question_ = get_object_or_404(Question, id=id)
    queryset = get_list_or_404(Choice, question = question_)
    context = {
        'question'    : question_,
        'object_list' : queryset,
    }
    status_ = has_voted(question_, request)
    print(status_)
    if status_[0]==True:
        return HttpResponse(f'<h1>You Have already Voted Your Choice Was: {status_[1]}')


    vote = request.POST.get('vote_given')
    if request.method == 'POST' and vote is not None :
        choice_voted  = get_object_or_404(Choice, choice_text=vote, question = question_)

        #vote saving
        question_.votes+=1
        choice_voted.votes+=1

        question_.save()
        choice_voted.save()
        #adding IP
        add_ip(question_, choice_voted, request)


        return redirect('../')
    
    return render(request, 'polls/polls_vote.html', context)


