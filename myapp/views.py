from django.shortcuts import render

# Create your views here.
def sample(request):
    context = {
        'names' : ["Vamshi","krishna","Chandra"]
    }
    return render(request, 'index.html',context)

def table(request):
    context = {
        'names' : ["Vamshi","krishna","Chandra"]
    }
    return render(request, 'table.html',context)

def task(request):
    context ={
        'data':[
            {'name':'vamshi', 'age':21,'gender':'male','email':'vamshi@gmail.com'},
            {'name':'krishna', 'age':23,'gender':'male','email':'krishna@gmail.com'},
            {'name':'chandra', 'age':21	,'gender':'male','email':'chandra@gmail'}
        ]
    }
    return render(request, 'task.html',context)
def student(request):
    names = {
        'student_details' :[
            {'first_name':'Vamshikrishna', 'last_name':'chandra', 'email':'vamshikrishna@gmail.com','gender':'male'},
            {'first_name':'Sreeja', 'last_name':'ramjari', 'email':'sreeja@gmail.com','gender':'female'},
            {'first_name':'Sanjana', 'last_name':'reddisteety', 'email':'sanjayana@gmail.com','gender':'female'},
            {'first_name':'Soujnaya', 'last_name':'penta', 'email':'sounjaya@gmail.com','gender':'female'}
        ]
    }
    return render(request,'student.html',names)