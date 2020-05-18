3주차 실습 : model, crud
=============

## 1. Model
* * *

* 데이터베이스(Database) :  다수의 사용자가 데이터들의 공유와 운영을 위해 저장해 놓는 공간
 * 쉽게 말해 데이터 수집, 저장, 보관을 위한 시스템
 * 종류 : 계층형 / 네트워크형 / 관계형 / NoSQL
   * 계층형 DB: 데이터 관계를 트리 구조로 정의. 데이터 중복 문제.
   * 네트워크형 DB: 레코드 간의 관계를 그물처럼 갖는 구조. 구조 변경 어려움.
   * 관계형 DB: 행(row)과 열(column)로 구성된 테이블간의 관계를 나타낼 때 사용. SQL(Structed Query Language) 사용하여 데이터 관리, 접근.
   * NoSQL DB: key-value 형태로 저장, 키를 사용해 데이터 접근
   -> 우리는 장고 ORM(Object Relational Mapper, 파이썬-DB 통역사 역할)을 이용해 관계형 DB 구현.

* 장고 ORM
 * 앱 폴더 안 models.py 파일에서 정의된 class와 db 테이블이 1:1 대응

 '''
 from django.db import models

 class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DataTimeField()
    text = models.TextField()
 '''
 Blog 테이블이 생성되고, 각각의 필드가 column(title, data, text)으로 구조화.


## 2. Migrations
* * *
* Migration ?
  Models.py에서 테이블을 추가하거나 변경사항이 있을 때 터미널에 적을 명령어

 * 데이터베이스 스키마의 버전 관리 시스템과 같다. (git commit과 유사)
  + 스키마? : 데이터베이스에서 자료의 구조, 자료의 표현 방법, 자료 간의 관계를 형식 언어로 정의한 구조
  + 데이터베이스 관리 시스템(DBMS)이 주어진 설정에 따라 데이터베이스 스키마를 생성하며, 데이터베이스 사용자가 자료를 저장, 조회, 삭제, 변경할 때 DBMS는 자신이 생성한 데이터베이스 스키마를 참조하여 명령을 수행한다.

* Migration vs Migrate
 * migrations는 DB 변경 내용을 저장하고, migarte는 그 내용을 테이블에 적용시킨다.
 * 각 app 안에 있는 migrations file은 해당 app 안의 migrations 디렉토리 안에 존재하고, commited 되어 코드로서 분배되도록 디자인되어있다.

makemigrations는 내장 앱이나 새로 만든 앱의 SQL command를 생성한다. 하지만 변경 사항만 저장할 뿐이지 내 데이터베이스에서 실행되는 것은 아니다. 그래서 makemigrations를 한 뒤에 테이블이 생기거나 하지 않는다.

1번 뒤에 sqlmirate를 하면 makemigrations를 통해 생성된 것들을 모든 SQL commands를 볼 수 있다.

migrate는 2번의 SQL commands를 데이터베이스 파일에서 실행한다. 그래서 migrate를 하고 나면 내 데이터베이스 파일 안의 앱의 테이블들이 생성된다. migrate command를 실행하고 db.sqlite3를 실행하면 모든 테이블이 생긴 것을 볼수 있을 것이다.

> migrate : migrations를 적용하거나 적용 해제(applying or unapplying)한다.
> makemigrations : models에 적용한 변화를 기반으로 새로운 migrations를 만들어낸다.
> sqlmigrate: migration을 위한 SQL statements를 보여준다.
> showmigrations: project의 migrations list와 그들의 상태(체크박스)를 보여준다.


 * 내 모델에 적용된 변화를 모아서 migration files에 적용하는 것.
 * 데이터베이스 변화 내용을 실제 테이블에 적용하는 것.



* 명령어들

    python manage.py makemigrations

models.py에서 적용한 변경사항이나 추가된 혹은 삭제된 사항들을 감지하여 파일로 생성


    python manage.py migrate

적용되지 않은 migrations들을(설정값들을) 적용시키는 역할

* 