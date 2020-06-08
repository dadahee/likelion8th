from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'title', 'date', 'text' ]
    # admin 페이지가 열렸을 때 어떤 순서로 모델을 보여줄 거야?

admin.site.register(Todo, TodoAdmin)