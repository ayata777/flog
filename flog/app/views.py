from django.shortcuts import render
from .forms import CategoryForm,RegisterForm,SpecifyForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from app.models import Category,Specify,BigCategory
from .forms import CategoryForm,RegisterForm,SpecifyForm,BigCategoryForm

def index(request):
    categories = BigCategory.objects.all()
    context = {
        'categories' : categories,
    }
    return render(request,'app/index.html',context)

def category(request,pk):
    categories = Category.objects.filter(bigcategory=pk)
    context = {
        'categories' : categories,
        'pk' : pk
    }
    return render(request,'app/category.html',context)
def specify(request,pk):
    pk = pk
    specify = Specify.objects.filter(category=pk)
    context = {
        'specify' : specify,
        'pk' : pk
    }
    return render(request,'app/specify.html',context)
def bigcategory_new(request):
    if request.method == "POST":
        form = BigCategoryForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('app:index')
    else:
        form = BigCategoryForm()
        context={
        'form':form,
        }
    return render(request, 'app/bigcategory_new.html', context)
def category_new(request,pk):
    pk = pk
    category = get_object_or_404(BigCategory,pk=pk)
    a = category.categories

    if request.method == "POST":
        form = CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.bigcategory = category
            post.bigcategory_name = category.categories
            post.save()
            return redirect('app:category', pk=pk)
    else:
        context = {
        'form': CategoryForm(),
        'a' : a
        }
    return render(request, 'app/category_new.html', context)
def specify_new(request,pk):
    pk = pk
    category = get_object_or_404(Category,pk=pk)
    a = category.categories

    if request.method == "POST":
        form = SpecifyForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.category = category
            post.category_name = category.categories
            post.save()
            return redirect('app:detail', pk=post.pk)
    else:
        context = {
        'form': SpecifyForm(),
        'a' : a
        }
    return render(request, 'app/specify_new.html', context)

def detail(request,pk):
    context = {
    'detail' : get_object_or_404(Specify,pk=pk),
    }
    return render(request, 'app/detail.html', context)
def specify_del(request,pk):
    """書籍の削除"""
#     return HttpResponse('書籍の削除')
    specify = get_object_or_404(Specify, pk=pk)
    specify.delete()
    return redirect('app:profile')
@login_required
def profile(request):
    user = request.user
    specify = Specify.objects.filter(author=user)
    context = {
        'user':user,
        'specify':specify
    }
    return render(request, 'app/profile.html', context)
 
 
def regist(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'app/regist.html', context)
 
 
@require_POST
def regist_save(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('app:index')
 
    context = {
        'form': form,
    }
    return render(request, 'app/regist.html', context)
