from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Address, department, Student, course, product, company,Student2, Student3, Document
from django.db.models import Q
from django.db.models import Count, Min, Max, Sum, Avg
from .forms import BookForm, StudentForm, Student3Form, DocumentForm, DocumentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
def index(request):
    name = request.GET.get("name") or "world!"  #add this line
    return render(request, "bookmodules/index.html", {"name": name})

def index2(request, val1 = 0):   #add the view function (index2)
    return HttpResponse("value1 = "+str(val1))


def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodules/show.html', context)

def index(request):
 return render(request, "bookmodules/index.html")
def list_books(request):
 return render(request, 'bookmodules/list_books.html')
def viewbook(request, bookId):
 return render(request, 'bookmodules/one_book.html')
def aboutus(request):
 return render(request, 'bookmodules/aboutus.html')
def links(request):
 return render(request, 'bookmodules/links.html')
def formatting(request):
 return render(request, 'bookmodules/formatting.html')
def listing(request):
 return render(request, 'bookmodules/listing.html')
def tables(request):
 return render(request, 'bookmodules/tables.html')
def search(request):
 if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodules/bookList.html', {'books':newBooks})
 

 return render(request, 'bookmodules/search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodules/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodules/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodules/index.html')

# def task1(request):
#     books=Book.objects.filter(Q(price__lte=50))
#     return render(request, 'bookmodules/bookList.html', {'books':books})

# def task2(request):
#     books=Book.objects.filter((Q(edition__gt=2)) & (Q(title__icontains = 'co')) | (Q(author__icontains = 'co')))
#     return render(request, 'bookmodules/bookList.html', {'books':books})

# def task3(request):
#     books=Book.objects.filter((~Q(edition__gt=2)) & (~Q(title__icontains = 'co')) | (~Q(author__icontains = 'co')))
#     return render(request, 'bookmodules/bookList.html', {'books':books})

# def task4(request):
#     books = Book.objects.order_by('title')
#     return render(request, 'bookmodules/bookList.html', {'books':books})


# def task5(request):
#     Query = Book.objects.aggregate(NumBooks = Count('id'),total = Sum('price',default=0), average = Avg('price',default=0),max = Max('price',default=0), min = Min('price',default=0) )
#     print(Query)
#     return render(request, 'bookmodules/task5.html',{'Query':Query})

# def task7(request):
#     cities = Address.objects.annotate(student_count=Count('student'))
#     return render(request, 'bookmodules/task7.html', {'cities':cities})

def task1(request):
    departments = department.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodules/department_student_count.html', {'departments': departments})


def task2(request):
    courses = course.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodules/course_student_count.html', {'courses': courses})

# def task3(request):
#     # For each department, find the student with the lowest ID
#     departments = department.objects.all()
#     department_students = []

#     for dept in departments:
#         oldest_student = Student.objects.filter(department=dept).order_by('id').first()
#         if oldest_student:
#             department_students.append({
#                 'department': dept.name,
#                 'student': oldest_student.name,
#                 'student_id': oldest_student.id
#             })

#     return render(request, 'bookmodules/oldest_student_per_department.html', {'data': department_students})


def task3(request):
    
    departments = department.objects.annotate(oldest_student_id=Min('student__id'))

    department_students = []
    for dept in departments:
        student = Student.objects.filter(id=dept.oldest_student_id).first()
        if student:
            department_students.append({
                'department': dept.name,
                'student': student.name,
                'student_id': student.id
            })

    return render(request, 'bookmodules/oldest_student_per_department.html', {'data': department_students})


def task4(request):
    departments = department.objects.annotate(student_count=Count('student')) \
                                    .filter(student_count__gt=2) \
                                    .order_by('-student_count')
    return render(request, 'bookmodules/departments_with_many_students.html', {'departments': departments})


def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodules/list_books1.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        edition = request.POST['edition']

        Book.objects.create(
            title=title,
            author=author,
            price=price,
            edition=edition
        )
        return redirect('list_books')

    return render(request, 'bookmodules/add_book.html')




def edit_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.edition = request.POST['edition']
        book.save()
        return redirect('list_books')

    return render(request, 'bookmodules/edit_book.html', {'book': book})



def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('list_books')



def list_books2(request):
    books = Book.objects.all()
    return render(request, 'bookmodules/list_books2.html', {'books': books})

def add_book2(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books2')
    else:
        form = BookForm()
    return render(request, 'bookmodules/add_book2.html', {'form': form})



def edit_book2(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books2')
    else:
        form = BookForm(instance=book)

    return render(request, 'bookmodules/edit_book2.html', {'form': form})



def delete_book2(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('list_books2')

def list_product(request):
    pro = product.objects.all()
    return render(request, 'bookmodules/list_product.html', {'pro': pro})
def landing(request):
   return render(request, 'bookmodules/landing.html')

def view_product(request, id):
   pro = product.objects.get(id=id)
   return render(request, 'bookmodules/view_product.html', {'pro': pro})

def editt(request, id):
   pro = product.objects.get(id=id)

   if request.method == 'POST':
      pro.kind = request.POST.get('kind')
      pro.expir_year = request.POST.get('expir_year')
      company_id = request.POST.get('company_id')
      pro.company = company.objects.get(id=company_id)
      pro.save()
      return redirect('list_product')
   
   comp = company.objects.all()
   return render(request, 'bookmodules/editt.html', {'pro': pro ,'comp':comp})
def deletee(request, id):
   pro = product.objects.get(id=id)
   pro.delete()
   return redirect('list_product')

def list_students(request):
   st = Student2.objects.all()
   return render(request, 'bookmodules/list_students.html', {'st':st})

@login_required
def add_student(request):
   if request.method == 'POST':
      form = StudentForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('list_students')
   else: form = StudentForm()
   return render(request, 'bookmodules/add_student.html', {'form':form})

@login_required
def edit_student(request, id):
   student = Student2.objects.get(id=id)
   form = StudentForm(instance=student)

   if request.method == 'POST':
      form = StudentForm(request.POST, instance=student)
      if form.is_valid():
         form.save()
         return redirect('list_students')
      else: form = StudentForm(instance=student)
            
   return render(request, 'bookmodules/edit_student.html', {'form':form})

@login_required
def delete_student(request, id):
   student = Student2.objects.get(id=id)
   student.delete()
   return redirect('list_students')


def list_students2(request):
   st = Student3.objects.all()
   return render(request, 'bookmodules/list_students2.html', {'st':st})

@login_required
def add_student2(request):
   if request.method == 'POST':
      form = Student3Form(request.POST)
      if form.is_valid():
         form.save()
         return redirect('list_students2')
   else: form = Student3Form()
   return render(request, 'bookmodules/add_student2.html', {'form':form})

@login_required
def edit_student2(request, id):
   student = Student3.objects.get(id=id)
   form = Student3Form(instance=student)
   
   if request.method == 'POST':
      form = Student3Form(request.POST, instance=student)
      if form.is_valid():
         form.save()
         return redirect('list_students2')
      else: form = Student3Form(instance=student)
            
   return render(request, 'bookmodules/edit_student2.html', {'form':form})

@login_required
def delete_student2(request, id):
   student = Student3.objects.get(id=id)
   student.delete()
   return redirect('list_students2')

# def add_document(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('list_documents')
#     else:
#         form = DocumentForm()
#     return render(request, 'bookmodules/add_document.html', {'form': form})

def list_documents(request):
    documents = Document.objects.all()
    return render(request, 'bookmodules/list_documents.html', {'documents': documents})

@login_required
def add_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('list_documents')  
    else:
        form = DocumentForm()
    return render(request, 'bookmodules/add_document.html', {'form': form})