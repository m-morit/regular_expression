import re
from django.shortcuts import render, redirect

def index(request):
    return render(request,'index.html',{})

def confirm(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        age = request.POST.get('age', '')
        zip_code = request.POST.get('zip_Code', '')
        tel = request.POST.get('tel', '')

        # Remove spaces from the name
        name = re.sub(r'\s', '', name)

        # Check if age, zip_code, and tel match the required patterns
        if not re.match(r'^\d+$', age):
            return render(request, 'index.html', {'error_age': 'Invalid age format', 'name': name, 'age': age, 'zip_code': zip_code, 'tel': tel})
        elif not re.match(r'^\d{3}-?\d{4}$', zip_code):
            return render(request, 'index.html', {'error_zip_code': 'Invalid zip code format', 'name': name, 'age': age, 'zip_code': zip_code, 'tel': tel})
        elif not re.match(r'^\d{3}-?\d{4}-?\d{4}$', tel):
            return render(request, 'index.html', {'error_tel': 'Invalid phone number format', 'name': name, 'age': age, 'zip_code': zip_code, 'tel': tel})
        else:
            return render(request, 'confirm.html', {'name': name, 'age': age, 'zip_code': zip_code, 'tel': tel})
    else:
        return render(request, 'index.html')