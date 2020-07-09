from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisteration, AddService, AddTeam, AddReview, AddPricing, ContactForm, ProfileSetting
from .models import *
from services.models import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


# Create homepage views here.
def dashboard_views(request):

    if request.user.is_authenticated:
        mobile_obj = Mobile.objects.all()[:5]
        count_review = Review.objects.all().count()
        count_team_member = Team.objects.all().count()
        count_users = UpdateProfile.objects.all().count()
        context = {
            'count_review' : count_review,
            'mobile_obj': mobile_obj,
            'count_team_member' : count_team_member,
            'count_users' : count_users,
        }
        return render(request, 'app/bashboard.html', context)

    else:
        return redirect(singin_views)

    return render(request, 'app/bashboard.html')


# Create homepage views here.
def homepage(request):

    # Message send to email
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            try:
                send_mail(subject, message, from_email, ['mbrsagor@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Message Send Failed')
            return redirect(homepage)

    # Create object model class
    service = Service.objects.all()
    team = Team.objects.all()
    review = Review.objects.all().order_by('-id') [:3]
    pricing = Pricing.objects.all().order_by('-id') [:3]

    context = {
        'service' : service,
        'team' : team,
        'review' : review,
        'pricing' : pricing,
        'form' : form
    }
    return render(request, 'homepage/index.html', context)


# Create Singup views here.
def singup_views(request):

    form = UserRegisteration(request.POST or None)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        return redirect(singin_views)

    context = {
        'form' : form
    }

    return render(request, 'users/page-register.html', context)



# Create Singin views here.
def singin_views(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(username = username, password = password)

        if auth is not None:
            login(request, auth)
            return redirect(dashboard_views)

    return render(request, 'users/page-login.html')



# Create singout views here.
def singout_views(request):
    logout(request)
    return redirect(singin_views)



# Create user profile views here.
def user_profile_views(request):

    try:
        profiles = get_object_or_404(UpdateProfile, user=request.user)
        # profiles = UpdateProfile.objects.filter(user=request.user)
    except:
        return redirect(profile_setting_views)

    context = {
        'user' : request.user,
        'profile' : profiles
    }

    return render(request, 'users/profile.html',context)



# Create profile setting views here.
def profile_setting_views(request):
    if request.user.is_authenticated:
        form = ProfileSetting()
        if request.method == 'POST':
            form = ProfileSetting(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit = False)
                instance.user = request.user
                instance.save()
                return redirect(user_profile_views)
    else:
        return redirect(singin_views)
    context = {
        'form' : form
    }
    return render(request, 'users/profile_edit.html', context)




# Create service views here.
def services_views(request):
    if request.user.is_authenticated:
        form = AddService()
        if request.method == 'POST':
            form = AddService(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit = False)
                instance.save()
                return redirect(services_views)

    else:
        return redirect(singin_views)

    context = {
        'form' : form
    }

    return render(request, 'services/services.html', context)




# Create tem member views here.
def add_teamMember_views(request):

    if request.user.is_authenticated:
        form = AddTeam()
        if request.method == 'POST':
            form = AddTeam(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit = False)
                instance.save()
                return redirect(add_teamMember_views)

    else:
        return redirect(singin_views)

    context = {
        'form' : form
    }

    return render(request, 'services/team.html', context)




# Create tem member views here.
def add_review_views(request):

    if request.user.is_authenticated:
        form = AddReview()
        if request.method == 'POST':
            form = AddReview(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit = False)
                instance.save()
                messages.add_message(request, messages.WARNING, 'Your Review publish successfully')
                return redirect(add_review_views)
            else:
                messages.add_message(request, messages.WARNING, 'Invalid keyword type mista')

    else:
        return redirect(singin_views)

    context = {
        'form' : form
    }

    return render(request, 'services/reviews.html', context)



# Create Add Pricing views here.
def add_pricing_views(request):

    if request.user.is_authenticated:
        form = AddPricing()
        if request.method == 'POST':
            form = AddPricing(request.POST)
            if form.is_valid():
                instance = form.save(commit = False)
                instance.save()
                return redirect(add_review_views)
    else:
        return redirect(singin_views)

    context = {
        'form' : form
    }

    return render(request, 'services/pricing.html', context)
