
3주차 : model, crud
=============


## 1. Model

* **데이터베이스(Database)** :  다수의 사용자가 데이터들의 공유와 운영을 위해 저장해 놓는 공간
    * 쉽게 말해 데이터 수집, 저장, 보관을 위한 시스템
    * 종류 : 계층형 / 네트워크형 / 관계형 / NoSQL
        * 계층형 DB: 데이터 관계를 트리 구조로 정의. 데이터 중복 문제.
        * 네트워크형 DB: 레코드 간의 관계를 그물처럼 갖는 구조. 구조 변경 어려움.
        * 관계형 DB: 행(row)과 열(column)로 구성된 테이블간의 관계를 나타낼 때 사용. SQL(Structed Query Language) 사용하여 데이터 관리, 접근.
        * NoSQL DB: key-value 형태로 저장, 키를 사용해 데이터 접근
        -> 우리는 장고 ORM(Object Relational Mapper, 파이썬-DB 통역사 역할)을 이용해 관계형 DB 구현.

* **장고 ORM** : 앱 폴더 안 models.py 파일에서 정의된 class와 db 테이블이 1:1 대응

    ```
    from django.db import models

    class Blog(models.Model):
        title = models.CharField(max_length=200)
        date = models.DataTimeField()
        text = models.TextField()
    ```
  장고가 제공해주는 models를 상속받아 orm 가능한 class를 작성할 수 있다.

  > Blog 테이블이 생성되어, 각각의 필드가 column으로 구조화된다. column이 어떤 자료형의 field로 구성되는지 설정한다. (CharField는 **반드시 max_length 인자를 지정해주어야 함**)  
  종류가 짱 많으니 필요할 때 성실하게 찾아볼 것. 제발...

    > 각각의 클래스 객체(row 단위)는 id, 즉 PK(Primary Key)를 가지며 이를 통해 객체를 구분할 수 있다. 
    >  

---
## 2. Migrations
* **Migration?** : Models.py에서 테이블을 추가하거나 변경사항이 있을 때 터미널에 적을 명령어

    * 데이터베이스 스키마의 버전 관리 시스템과 같다. (git commit과 유사)
        + 스키마? : 데이터베이스에서 자료의 구조, 표현 방법, 자료 간의 관계를 형식 언어로 정의한 구조
        + 데이터베이스 관리 시스템(DBMS)이 주어진 설정에 따라 데이터베이스 스키마를 생성하며, 데이터베이스 사용자가 자료를 저장, 조회, 삭제, 변경할 때 DBMS는 자신이 생성한 데이터베이스 스키마를 참조하여 명령을 수행한다.

    #

* **Migration vs Migrate**
    * migrations는 DB 변경 내용을 저장하고, migarte는 그 내용을 테이블(migration files)에 적용시킨다.
    * migrations file : 각 app 안의 migrations 디렉토리 안에 존재, commited 되어 코드로서 분배되도록 디자인되어있다.
    * 데이터베이스 변화 내용을 실제 테이블에 적용하는 것.

    #
* **명령어들**

        python manage.py makemigrations

    models.py에서 적용한 변경사항이나 추가된 혹은 삭제된 사항들을 감지하여 파일로 생성 
    #
    
        python manage.py migrate

    적용되지 않은 migrations들을(설정값들을) 적용시키는 역할  
    #

    > **migrate** : migrations를 적용하거나 적용 해제(applying or unapplying)  
    > **makemigrations** : models에 적용한 변화를 기반으로 새로운 migrations 생성   
    > **sqlmigrate** : migration을 위한 SQL statements를 보여준다.  
    > **showmigrations** : project의 migrations list와 그들의 상태(체크박스)를 보여준다.  
    #
* **그래서 언제 쓰는데**  
  **models.py에서 class의 필드를 만들거나 수정할 때마다** db에게 해당 변경 내용을 알려주어야(migration) 한다.

---
## 3. admin
* admin 페이지를 통해 models에서 작성한 db 구조를 확인할 수 있다.

* admin.py (Blog: 만든 클래스 정보)
  ```
  from django.contrib import admin
  from .models import Blog

  admin.site.register(Blog)
  ```
  위 방법을 통해 작성한 모델 정보를 admin 페이지에 알려주어야 함.

    #
* 슈퍼 유저 만들기 (터미널)
  ```
  python manage.py createsuperuser
  ```

    #
* 슈퍼유저 계정 생성 및 admin 파일 수정 후 로컬주소/admin 통해 나의 노고를 확인할 수 있다.
  * 객체 add 시 가시적으로 확인할 수 있는 필드는 내가 클래스에서 정의한 필드.
  * 좀더 예쁜 객체 구경을 원한다면 객체를 문자열로 반환하는 메소드(str, 클래스 정의 시 자동 생성)를 오버라이딩하여 사용할 것.  
  
    ```
    from django.db import models

    class Blog(models.Model):
        title = models.CharField(max_length=200)
        date = models.DataTimeField()
        text = models.TextField()

        def __str__(self):
            return self.title

        def summary(self):
            return self.body[:100]+"..."
    ```
    > **메소드 생성 및 재정의는 테이블을 건드리지 않기 때문에 migrations 대상이 아님.**  

---
## 4. CRUD
드디어 페이지 만든다...

> **CRUD** : Create, Read, Update, Delete.  
장고 orm을 통해 데이터베이스에 정보 생성/수정/삭제하는 것.

#
### 4-1. READ 구현
#### home.html(블로그 포스트 목록) 만들기
* views.py : home 함수 생성
  ```
  from .models import blog

  def home(request):
    blogs = Blog.objects.all()
    # Blog 테이블 객체들을 all() 메소드를 통해 전부 가져와 blogs 객체에 담는다.
    return render(request, 'home.html', { 'blogs': blog})
    # dictionary 형태로 home.html에 객체들을 같이 보내준다.
  ```

* urls.py : home 함수와 home.html 연결
  ```
  import blog.views

  urlpatterns = [
      ...
    path('', blog.views.home, name="home"),
    # path('로컬주소 뒤에 붙는 url', views.py에 있는 함수, namespace)
  ]
  ```

* blog(app이름)/templates/home.html : 목록을 보여줄 페이지 작성
    ```
    {% for blog in blogs %}
    <a href="{%url 'detail' blog.id %}" style="text-decoration: none;">
    <hr>{{blog.title}}
    <br> {{blog.date}}
    <br> {{blog.summary}}{% endfor %}
    </a>
    ```
  > {{ blogs }} : queryset 형태로 출력됨.
  > {{ blog }} : object

#
#### detail.html(블로그 상세 페이지) 만들기

~ 5/18 오늘은 여기까지~~ 으하하 0(-(