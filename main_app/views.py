from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cutlery, Prep
from .forms import SharpenForm
# from .models import blades

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

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


def add_sharpen(request, cutlery_id):
    form = SharpenForm(request.POST)
    
    #if form is valid
    if form.is_valid():
        #submit the form
        new_form = form.save(commit=False)
        new_form.cutlery_id = cutlery_id
        new_form.save()

    return redirect('detail', cutlery_id=cutlery_id)
