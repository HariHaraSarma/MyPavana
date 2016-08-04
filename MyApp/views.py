from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from .forms import PostForm, DealerForm, StockForm
import datetime





def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_created == datetime.date.today()
            post.save()
            return HttpResponseRedirect('/person/new/') 
            
    else:
        form = PostForm()
    return render(request, 'person.html', {'form': form})

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