from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
import userinfo.views
from django.contrib import messages
from django.views import View



# Create Mobile Phone views here.
def adpost_views(request):

    if request.user.is_authenticated:
        form = Adnew_Post()
        if request.method == 'POST':
            form = Adnew_Post(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.add_message(request, messages.WARNING, 'অাপনার অ্যাডটি লাইফ হয়েছে')
                return redirect(adpost_views)
            else:
                messages.add_message(request, messages.WARNING, 'দুঃখিত!! অাপনার পােষ্টটি সম্পন্যভাবে অাপডেট হয়নি')

    else:
        return redirect('http://127.0.0.1:8000/singin')

    context = {
        'form' : form
    }
    return render(request, 'services/mobile.html',context)



# Create Television views here.
def adpost_television_views(request):

    if request.user.is_authenticated:
        form = Adnew_television_Post()
        if request.method == 'POST':
            form = Adnew_television_Post(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.add_message(request, messages.WARNING, 'অাপনার অ্যাডটি লাইফ হয়েছে')
                return redirect(adpost_television_views)
            else:
                messages.add_message(request, messages.WARNING, 'দুঃখিত!! অাপনার পােষ্টটি সম্পন্যভাবে অাপডেট হয়নি')
    else:
        return redirect('http://127.0.0.1:8000/singin')
    context = {
        'form' : form
    }
    return render(request, 'services/television.html',context)



# Create Computing views here.
def adpost_computing_views(request):

    if request.user.is_authenticated:
        form = Adnew_computing_Post()
        if request.method == 'POST':
            form = Adnew_computing_Post(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.add_message(request, messages.WARNING, 'অাপনার অ্যাডটি লাইফ হয়েছে')
                return redirect(adpost_computing_views)
            else:
                messages.add_message(request, messages.WARNING, 'দুঃখিত!! অাপনার পােষ্টটি সম্পন্যভাবে অাপডেট হয়নি')
    else:
        return redirect('http://127.0.0.1:8000/singin')
    context = {
        'form' : form
    }
    return render(request, 'services/computing.html',context)



# Create Property views here.
def adpost_property_views(request):

    if request.user.is_authenticated:
        form = Adnew_property_Post()
        if request.method == 'POST':
            form = Adnew_property_Post(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.add_message(request, messages.WARNING, 'অাপনার অ্যাডটি লাইফ হয়েছে')
                return redirect(adpost_property_views)
            else:
                messages.add_message(request, messages.WARNING, 'দুঃখিত!! অাপনার পােষ্টটি সম্পন্যভাবে অাপডেট হয়নি')
    else:
        return redirect('http://127.0.0.1:8000/singin')
    context = {
        'form' : form
    }
    return render(request, 'services/property.html',context)



# Create Education views here.
def adPost_study_views(request):

    if request.user.is_authenticated:
        form = Adnew_Post_Study()
        if request.method == 'POST':
            form = Adnew_Post_Study(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit = False)
                instance.save()
                messages.add_message(request, messages.WARNING, 'অাপনার অ্যাডটি লাইফ হয়েছে')
                return redirect(adPost_study_views)
            else:
                messages.add_message(request, messages.WARNING, 'দুঃখিত!! অাপনার পােষ্টটি সম্পন্যভাবে অাপডেট হয়নি')

    else:
        return redirect('http://127.0.0.1:8000/singin')
    context = {
        'form' : form
    }
    return render(request, 'services/study.html', context)




# Display all service form here

# all category product
def all_service_display(request):

    mobile_obj = Mobile.objects.all().order_by('-id')[:2]
    tv_obj = Television.objects.all().order_by('-id')[:2]
    property_obj = Property.objects.all().order_by('-id')[:2]
    study_obj = Study.objects.all().order_by('-id')[:2]
    computing_obj = Computing.objects.all().order_by('-id')[:2]
    category_obj = Category.objects.all()
    context = {
        'mobile_obj' : mobile_obj,
        'tv_obj' : tv_obj,
        'property_obj' : property_obj,
        'study_obj' : study_obj,
        'computing_obj' : computing_obj,
        'category_obj' : category_obj
    }
    return render(request, 'homepage/project-list.html', context)




# all product details
class Details_product(View):

    def get(self, request, id):

        single_post = get_object_or_404(Mobile, id = id)
        related_project = Mobile.objects.filter(category = single_post.category).exclude(id = id)[:4]
        context = {
            'single_post' : single_post,
            'related_project' : related_project
        }
        return render(request, 'homepage/single.html', context)


# list of all product dispaly admin
def list_of_display(request):

    if request.user.is_authenticated:
        mobile_obj = Mobile.objects.all().order_by('-id')
        # Search Queary
        query = request.GET.get('product')
        if query:
            mobile_obj = mobile_obj.filter(name__icontains = query)

        context = {
            'mobile_obj' : mobile_obj,
        }
    else:
        return redirect('http://127.0.0.1:8000/singin')
    return render(request, 'services/list_of_product.html', context)



# list of all product delete admin
def list_of_delete(request, id):

    if request.user.is_authenticated:
        delete_item = get_object_or_404(Mobile, id = id)
        delete_item.delete()
        messages.add_message(request, messages.WARNING, 'অ্যাডটি ডিলিট হয়েছে')
        return redirect(list_of_display)

    else:
        return redirect('http://127.0.0.1:8000/singin')



# 404 page

def error_404(request):
        data = {}
        return render(request,'app/error_404.html', data)
