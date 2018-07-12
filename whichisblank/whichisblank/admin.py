from django.contrib import admin
from .models import Question, Author
import views

admin.site.register(Question)
admin.site.register(Author)