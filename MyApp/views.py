from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from .forms import PersonForm, DealerForm, StockForm
from .forms import Person, DealersInfo, ComplteStockDetails
import datetime





def person_new(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_created == datetime.date.today()
            post.save()
            return HttpResponseRedirect('/person/new/')
            
            
    else:
        form = PersonForm()
    return render(request, 'person.html', {'form': form})

def person_list(request):
    queryset=Person.objects.all()
    if request.user.is_authenticated():
        context={
            "person_list":queryset,
            
        }
    
    return render(request, 'person_list.html', context)


def dealer_new(request):
    if request.method == "POST":
        form = DealerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/dealer/new/')
    else:
        form = DealerForm()
    return render(request, 'dealer.html', {'form': form})

def dealer_list(request):
    dealer=DealersInfo.objects.all()
    if request.user.is_authenticated():
        dealer_list={
            "dealer_list":dealer,
            
        }
    
    return render(request, 'dealer_list.html', dealer_list)



def stock_new(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/stock/new/')
    else:
        form = StockForm()
    return render(request, 'stock.html', {'form': form})


def stock_list(request):
    stock=ComplteStockDetails.objects.all()
    if request.user.is_authenticated():
        stock_list={
            "stock_list":stock,
            
        }
    
    return render(request, 'stock_list.html', stock_list)
