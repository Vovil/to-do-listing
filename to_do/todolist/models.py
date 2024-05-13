from django.utils import timezone #мы будем получать дату создания todo
from django.db import models

class Category(models.Model): #Таблица категория, которая наследует models.Model
	name = models.CharField(max_length=100) #varchar. Имя категории

	class Meta:
		verbose_name = ("Category") # имя в ед. числе
		verbose_name_plural = ("Categories")  # имя в множ. числе

	def __str__(self):
		return self.name  # __str__ применяется для отображения объекта в интерфейсе


class TodoList(models.Model):
	title = models.CharField(max_length=250)
	content = models.TextField(blank=True) # текстовое поле
	created = models.DateField(auto_now_add=True) # дата создания
	due_date = models.DateField(auto_now_add=True) # дата окончания
	category = models.ForeignKey(Category, default="general",on_delete=models.PROTECT) # foreignkey связь с таблицей Категорий
	class Meta: # вспомогательный класс мета для сортировки
		ordering = ["-created"] # сортировка дел по времени их создания
	def __str__(self):
		return self.title