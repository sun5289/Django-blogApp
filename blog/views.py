from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from blog.modleforms import PostModelForm, PostForm
from .models import Post
# Create your views here.



def post_list(request): # 글 목록
    # name = "첫번째 Django 입니다.11"
    # return HttpResponse(' <h1>  Hello {}</h1>'.format(name))
    # query set 사용해서 Post 목록 가져오기
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request,pk): #글 상세조회
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# 글등록 모델폼 사용
def post_new(request):
    if request.method== "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # 검증에성공한값들을dict타입으로제공받아서이값을DB에저장하기
            post = form.save(commit=False)
            post.author= request.user
            post.published_date= timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            form.errors
    else: # 검증에실패하면, form.errors와form.각필드.errors 에오류정보를저장
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})

# 글등록 Form을 사용
def post_new_form(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        # print(form)
        if form.is_valid():
            # print(form.cleaned_data)
            post = Post(author=request.user,title=form.cleaned_data['title'],text=form.cleaned_data['text'],published_date=timezone.now())
            post.save()
            return redirect('post_detail',pk=post.pk)
        else:   #검증 실패
            print(form.errors)
    else:
        form = PostForm()

    return render(request,'blog/post_form.html',{'form': form})


