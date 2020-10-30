from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cutlery, Prep
from .forms import SharpenForm, CutleryForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
# ------------------------------ STATIC PAGES
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# ------------------------------- CUTLERY

@login_required
def cutlery_index(request):
    cutlery = Cutlery.objects.all()

    return render(request, 'cutlery/index.html', {'cutlery': cutlery})

def cutlery_detail(request, cutlery_id):
    cutlery = Cutlery.objects.get(id=cutlery_id)
    # get the prep the cutlery doesn't have
    prep_cutlery_doesnt_have = Prep.objects.exclude(id__in=cutlery.prep.all().values_list('id'))
    sharpen_form = SharpenForm()

    return render(request, 'cutlery/detail.html', {
        'cutlery': cutlery,
        'sharpen_form': sharpen_form,
        'prep': prep_cutlery_doesnt_have
    })

def add_cutlery(request):
    if request.method == 'POST':
        cutlery_form = CutleryForm(request.POST)
        if cutlery_form.is_valid():
            new_cutlery = cutlery_form.save(commit=False)
            new_cutlery.user = request.user
            new_cutlery.save()

            return redirect('detail', cutlery_id=new_cutlery.id)
    else: 
        form = CutleryForm()
        context = {'form': form}
        return render(request, 'cutlery/new.html', context)

def delete_cutlery(request, cutlery_id):
    Cutlery.objects.get(id=cutlery_id).delete()
    return redirect('cutlery_index')

def edit_cutlery(request, cutlery_id):
    cutlery = Cutlery.objects.get(id=cutlery_id)
    if request.method == 'POST':
        cutlery_form = CutleryForm(request.POST, instance=cutlery)
        if cutlery_form.is_valid():
            updated_cutlery = cutlery_form.save()
            return redirect('detail', cutlery_id=updated_cutlery.id)
    else:
        form = CutleryForm(instance=cutlery)
        context = {'form': form}
        return render(request, 'cutlery/edit.html', context)

# ---------------------------------- CUTLERY PREP
def assoc_prep(request, cutlery_id, prep_id):
    # find cutlery by id
    cutlery = Cutlery.objects.get(id=cutlery_id)
    prep = Prep.objects.get(id=prep_id)
    cutlery.prep.add(prep)
    return redirect('detail', cutlery_id)

def remove_prep(request, cutlery_id, prep_id):
    cutlery = Cutlery.objects.get(id=cutlery_id)
    prep = Prep.objects.get(id=prep_id)
    cutlery.prep.remove(prep)
    return redirect('detail', cutlery_id)


# ---------------------------------- CUTLERY SHARPEN
def add_sharpen(request, cutlery_id):
    form = SharpenForm(request.POST)
    
    #if form is valid
    if form.is_valid():
        #submit the form
        new_form = form.save(commit=False)
        new_form.cutlery_id = cutlery_id
        new_form.save()

    return redirect('detail', cutlery_id=cutlery_id)

# ------------------------------------ AUTH

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to createa a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('cutlery_index')
        else: 
            error_message = 'Invalid sign up - try again'

            form = UserCreationForm()
            context = {'form': form, 'error_message': error_message}
            return render(request, 'registration/signup.html', context)
# A GET or a bad POST request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)