from django.db import models

from django.db import models
from employees.models import Employee

class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('assigned', 'Назначена'),
        ('in_progress', 'В работе'),
        ('completed', 'Завершена'),
        ('cancelled', 'Отменена')
    ]

    title = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(blank=True, verbose_name='Описание')
    parent_task = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subtasks', verbose_name='Родительская задача')
    assignee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks', verbose_name='Исполнитель')
    deadline = models.DateTimeField(verbose_name='Срок выполнения')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    priority = models.IntegerField(default=1, verbose_name='Приоритет')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    @property
    def has_active_dependencies(self):
        return self.subtasks.filter(status__in=["assigned", "in_progress"]).exists()
