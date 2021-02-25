from django.shortcuts import render
from accounts.models import Profile
from response.models import Response
from .models import Comment

# Create your views here.

def index(request):
    not_evaluated = Profile.objects.filter(current_status = 1)
    evaluated = Profile.objects.filter(current_status = 2)
    eliminated = Profile.objects.filter(current_status = 3)
    data = {}
    data['not_evaluated'] = not_evaluated
    data['evaluated'] = evaluated
    data['eliminated'] = eliminated
    return render(request,'administrator/dashboard.html',{'data':data})

def response_detail(request,id):
    profile = Profile.objects.get(id = id)
    response = Response.objects.filter(profile = profile)
    data = {}
    if request.method == 'POST':
        comment_obj = Comment(profile = profile)
        comment_obj.author = request.POST['author']
        comment_obj.comment = request.POST['comment']
        to_eliminate = request.POST['eliminate']
        comment_obj.save()
        profile.current_status = 2
        if(to_eliminate):
            profile.current_status = 3
        profile.save()
    try:
        comments = Comment.objects.filter(profile=profile).order_by('-date_time')
        data['reviews'] = comments
    except:
        data['reviews'] = []
    data['profile'] = profile
    data['response'] = response
    return render(request,'administrator/detail.html',{'data':data})
