# 6주차 : 템플릿상속, 페이지네이션
</br>

## 6주차 내용 요약
1. [(이전에 배운 내용) 기본 CRUD + 모델 구조 구현하기](#기본-CRUD-구현-및-모델-구조)
2. [템플릿 상속, 설정하여 base 템플릿 불러오기](#템플릿-상속받기)
3. [리스트 페이지에 페이지네이션 기능 추가](#페이지네이션)  
</br>

* * *

## **실습 내용**
</BR>

#### **기본 CRUD 구현 및 모델 구조**
   - settings.py : 앱 추가, static 폴더 생성.
   - 프로젝트 / urls.py : include 해주기
   - 앱 / urls.py : 각 페이지와 views.py의 함수 연결, 이름 지정
   - models.py : 모델 구현
        
        verbose_name 필드 : 레이블링에 사용
   - views.py : CRUD 함수 구현
     - new, edit 함수에서 method 방식에 따라 다르게 리턴해주기!
     - 이번 실습에서는 {{ form.as_p }} 등으로 한 번에 구현하지 않고 각 필드별로 뜯어서 인자를 받아 사용했다.
* * *
#### **템플릿 상속받기**
   - 템플릿 프레임(6주차 실습에서는 base.html) 파일 생성
   - 기본 템플릿(base.html)
        ``` html5
        ~ 대충 내용 ~
        {% block header %}
        {% endblock %}
        ~ 대충 내용2 ~
        {% block content %}
        {% endblock %}
        ```
      - block 위아래로 뼈대 내용을 작성해준다.
      - block 내부는 상속받을 페이지에서 작성.
   - 상속받을 페이지(new.html, show.html, edit.html)
        ``` html5
        {% extends 'base.html' %}
        {% block header %}
        대충 헤더에 들어갈 내용
        {% endblock %}

        {% block content %}
        대충 본문
        {% endblock %}
        ```
        맨위에 상속 템플릿 지정, block 내부에 컨텐츠 작성하기.
* * * 
#### **페이지네이션**
   - 그냥 예쁘게 보여주는 것뿐이라, views.py에서 show 메소드와 페이지 일부만 수정해주면 됨.
   - views.py
     - import 부터
        ``` python
        from django.core.paginator import Paginator
        ```
      - show() 메소드
        ``` python
        def show(request):
            todo = Todo.objects
            todolist = Todo.objects.all()
            paginator = Paginator(todolist, 2)
            # 인자 : 분할 될 객체, 한 페이지당 담길 객체 수.
            page = request.GET.get('page')
            posts = paginator.get_page(page)
            # page의 번호를 받아 해당 page를 리턴함.
            return render(request, 'show.html', { 'todo': todo, 'posts': posts })
        ```
   - 템플릿
        ``` html
        <div role="pagintaion" class="text-center">
            {% if posts.has_previous %}
                <a href="?page={{ posts.previous_page_page_number }}">◀</a>
            {% endif %}
            <span>{{ posts.number }} </span>
            <span> / </span>
            <span>{{ posts.paginator.num_pages }}</span>
            {% if posts.has_next %}
                <a href="?page={{ posts.next_page_number }}">▶</a>
            {% endif %}
        </div> 
        ``` 
</BR>

* * *
## **배운 내용**
</BR>

### **추가한 내용 : CRUD 구현 + 모델 구조**
   1. models.py (forms.py 아님에 주의) : verbose_name은 new.html이나 edit.html에서 input field 앞 레이블로 사용된다.
      ``` python
      class Todo(models.Model):
          date = models.DateField(verbose_name="날짜")
          title = models.CharField(max_length=150, verbose_name="제목")
          text = models.TextField(verbose_name="할 일")
      ```
   2. views.py / new 메소드
      ``` python
      def new(request):
          if request.method == "POST":
              form = TodoForm(request.POST)
              if form.is_valid():
                  form.save()
                  return redirect('main:show')
          else:
              form = TodoForm()
          return render(request, 'new.html', { 'form': form })
      ```
      * form이 유효한 정보를 담고 있을 경우 : form.cleaned_data['text'] 등으로 받아와서 필드별로 담아주지 않고 그냥 save() 때려버렸다. 돌아가길래...
      * form_name.cleaned_data : 입력폼 값 검증(validation)을 통과한 데이터(사전 타입)
   3. views.py / edit 메소드
      * form 클래스 인스턴스를 생성할 때 request.POST 쿼리셋과 instance 인자로 get_instance_or_404로 받은 객체(타입???)를 던져주자.
   4. DateField 예쁘게 사용하기 (드디어!)
      * 입력 예쁘게 받기 
        * forms.py 에서 포맷 지정 (models.py 아님 주의)
            ``` python
            date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, help_text="Formats: YYYY-MM-DD", required=True)
            ```
            help_text 인자 : 입력칸 옆에 노출되는 문자열, model 대부분의 field들에 사용할 수 있다.
        * settings.py 에 포맷 변수 추가
            ``` python
            DATE_INPUT_FORMATS = ['%Y-%m-%d']
            ```
      * 출력 예쁘게 하기
        * ```{{ todo.date | date:"Y/m/d l" }}```
        * 템플릿 페이지 내에서 파이프라인을 통해 포맷 지정  
</br>

* * *
### **새롭게 알게된 내용**
  1. [템플릿](#템플릿-상속받기) : 귀찮아서 링크 다는 거 아님...
  2. [페이지네이션](#페이지네이션) : 진짜로...  아마도...?
  3. 귀찮아서 장고 명령어에 alias를 지정해서 사용하는 중.
     * vact, mmig, mig, run, csu 등등
     * 까먹을까봐 적어놓는 단축 명령어들(... 내가 지정했는데...)


* * *
## 스크린샷

![show.html](https://github.com/dadahee/likelion8th/blob/master/Django/lab06/screenshots/todo_show.html.png)   
![show.html_empty](https://github.com/dadahee/likelion8th/blob/master/Django/lab06/screenshots/todo_show_empty.png)  
![edit.html](https://github.com/dadahee/likelion8th/blob/master/Django/lab06/screenshots/todo_edit.html.png)   
![new.html](https://github.com/dadahee/likelion8th/blob/master/Django/lab06/screenshots/todo_new.html.png)   