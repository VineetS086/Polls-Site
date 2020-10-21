from .models import Voters, Question, Choice

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def has_voted(question_, request):
    return_bool = False
    return_choice = None
    ip = get_client_ip(request)
    all_voters = question_.voters_set.all()
    all_voters_ip = [voter.ip_adress for voter in all_voters]
    
    if len(all_voters_ip) and ip in all_voters_ip:
        return_choice = question_.voters_set.get(ip_adress = ip).choice
        return_bool   = True
        return_choice = return_choice.choice_text
    return(return_bool, return_choice)


def add_ip(question_,choice_, request):
    ip = get_client_ip(request)
    voter = Voters(question=question_, choice=choice_, ip_adress=ip)
    voter.save()
