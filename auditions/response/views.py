from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, response


from .models import Question,Response
from accounts.models import Profile

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request,'response/index.html')

@login_required(login_url='/accounts/login/')
def get_question(request):
    user = request.user
    profile = Profile.objects.get(user = user)
    try:
        question = Question.objects.get(ques_round = profile.curr_round)
    except:
        if(profile.curr_round >= 5):
            return render(request,'response/end.html')
    if(request.method == 'POST'):
        response = Response(profile = profile)
        response.question = question
        response.response = request.POST["response"] ##Assuming form input name = response
        response.save()
        profile.curr_round += 1
        profile.save()
        return redirect('get-question')
    if(question.question_type == 'N'):
        return render(request,'response/get_question.html',{'question':question})
    elif(question.question_type == 'I'):
        return render(request,'response/get_question_image.html',{'question':question})
