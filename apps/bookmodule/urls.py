"""
URL configuration for libraryproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
  path('html5/links/', views.links, name="books.links"),
  path('html5/text/formatting/', views.formatting, name="books.formatting"),
  path('html5/listing/', views.listing, name="books.listing"),
  path('html5/tables/', views.tables, name="books.tables"),
  path('search/', views.search, name="books.search"),
  path('simple/query', views.simple_query),
  path('complex/query', views.complex_query),
#   path('lab8/task1/', views.task1),
#   path('lab8/task2/', views.task2),
#   path('lab8/task3/', views.task3),
#   path('lab8/task4/', views.task4),
#   path('lab8/task5/', views.task5),
#   path('lab8/task7/', views.task7),
  path('lab9/task1', views.task1 ),
  path('lab9/task2', views.task2 ),
  path('lab9/task3', views.task3 ),
  path('lab9/task4', views.task4 ),
#   path('lab9_part1/listbooks', views.listbooks, name = "list_books"),
#   path('lab9_part1/addbook/<int:id>' , views.addbook, name = "add_books"),
#   path('lab9_part1/editbook/<int:id>' , views.editbook, name = "edit_books"),
#   path('lab9_part1/deletebook/<int:id>' , views.deletebook, name = "delete_books"),
  path('lab9_part1/listbooks', views.list_books, name='list_books'),
  path('lab9_part1/addbook', views.add_book, name='add_book'),
  path('lab9_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
  path('lab9_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),
  path('lab9_part2/listbooks', views.list_books2, name='list_books2'),
  path('lab9_part2/addbook', views.add_book2, name='add_book2'),
  path('lab9_part2/editbook/<int:id>', views.edit_book2, name='edit_book2'),
  path('lab9_part2/deletebook/<int:id>', views.delete_book2, name='delete_book2'),
  path('list_product/', views.list_product, name='list_product'),
  path('landing/', views.landing, name='landing'),
  path('view_product/<int:id>', views.view_product, name='view_product'),
  path('editt/<int:id>', views.editt, name='editt'),
  path('deletee/<int:id>', views.deletee, name='deletee'),
  path('lab11_part1/list_students', views.list_students, name='list_students'),
  path('lab11_part1/add_student', views.add_student, name='add_student'),
  path('lab11_part1/delete_student/<int:id>', views.delete_student, name='delete_student'),
  path('lab11_part1/edit_student/<int:id>', views.edit_student, name='edit_student'),
  path('lab11_part2/list_students2', views.list_students2, name='list_students2'),
  path('lab11_part2/add_student2', views.add_student2, name='add_student2'),
  path('lab11_part2/delete_student2/<int:id>', views.delete_student2, name='delete_student2'),
  path('lab11_part2/edit_student2/<int:id>', views.edit_student2, name='edit_student2'),
  path('add_document/', views.add_document, name='add_document'),
  path('list_documents/', views.list_documents, name='list_documents'),
  ]