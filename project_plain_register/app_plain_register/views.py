from django.shortcuts import render
from .models import User

def	home(request):
	return render(request, 'users/home.html')

def users(request):
	new_user = User()
	new_user.name = request.POST.get('name')
	if ( request.POST.get('age').isnumeric()):
		new_user.age = request.POST.get('age')
	else:
		new_user.age = 0
	new_user.save()

	#creating a new dictionary to handle all the created users and display it
	users = {
		'users': User.objects.all()
	}
	return render(request, 'users/users.html', users)

def confirm_delete_all(request):
    if request.method == 'POST':
        User.objects.all().delete()
        return render(request, 'users/home.html')
    return render(request, 'users/confirm_delete_all.html')
