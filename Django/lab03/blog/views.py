from django.shortcuts import render, redirect, get_object_or_404

# db의 객체를 불러와야 하므로
# 블로그 클래스로 만들어진 테이블 객체를 불러온다.
from .models import Blog
from django.utils import timezone


# Create your views here.

def list(request):
    blogs = Blog.objects.all()
    # Blog라는 클래스로 만들어진 객체를 싹다 가져오렴
    return render(request, "list.html", { 'blogs': blogs })

def detail(request, blog_id):
    # blog_id는 객체의 고유 번호.
    # data가 이 id값에 있는 객체 하나를 달라고 요청한다.
    blog = get_object_or_404(Blog, pk=blog_id) #숫자에 맞는 객체를 찾아오기. 없으면 404 띄움 / 예외처리.
    # 가져올 객체의 테이블로 만들어진 클래스 이름과 pk값(primary key): id랑 똑같음
    # pk란 ? 제목, 날짜, 본문이 아예 같으면 동일한 객체를 어떻게 구별하나?
    # 객체 하나하나를 식별할 수 있는 객체값
    return render(request, 'detail.html', { 'blog': blog })

    # 이 id를 어떻게 넘길까? : path converter (urls.py 참고)


def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.date = timezone.datetime.now()
    new_blog.text = request.POST['body']
    new_blog.save()
    return redirect('/blog/'+str(new_blog.id))


def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'blog': edit_blog})


def update(request, blog_id):
    update_blog = get_object_or_404(Blog, pk=blog_id)
    update_blog.title = request.POST['title']
    update_blog.date = timezone.datetime.now()
    update_blog.text = request.POST['body']
    update_blog.save()
    #return redirect('/blog/'+str(update_blog.id))
    return redirect('detail', update_blog.id)

def delete(request, blog_id):
    to_be_deleted = get_object_or_404(Blog, pk=blog_id)
    to_be_deleted.delete()
    return redirect('list')