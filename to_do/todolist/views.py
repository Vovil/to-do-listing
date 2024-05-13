from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoList, Category
 
def redirect_view(request):
	return redirect('/category') # редирект с главной на категории

def todo(request):
	todos = TodoList.objects.all() # все объекты todo через менеджер объектов
	categories = Category.objects.all() # все Категории

	if request.method == "POST": # проверяем то что метод POST
		if "Add" in request.POST: # если пользователь собирается добавить задачу
			title = request.POST["description"] # сам текст
			date = str(request.POST["date"]) # дата, до которой должно быть закончено дело
			category = request.POST["category_select"] # категория, которой может выбрать или создать пользователь.
			content = f'{title} -- {date} {category}' # полный склеенный контент
			TodoList(title=title,
				content=content,
				due_date=date,
				category=Category.objects.get(name=category)
				).save()
			return redirect("/todo")
		if "Delete" in request.POST: # если пользователь собирается удалить задачи
			check_list = request.POST.getlist('checkedbox')
			TodoList.objects.filter(id__in=[int(_id) for _id in check_list]).delete()
	return render(request, "todo.html", {"todos": todos, "categories": categories})

def category(request):
	categories = Category.objects.all()  # все объекты Категорий
	if request.method == "POST": # проверяем что это метод POST
		if "Add" in request.POST: # если собираемся добавить
			Category(name=request.POST["name"]).save()
			return redirect("/category")
		if "Delete" in request.POST: # если собираемся удалить
			check = request.POST.getlist('check')
			try:
				Category.objects.filter(id__in=[int(_id) for _id in check]).delete()
			except BaseException: # тут нужно нормально переписать обработку ошибок, но на первое время хватит
				return HttpResponse('<h1>Сначала удалите карточки с этими категориями)</h1>')

	return render(request, "category.html", {"categories": categories})