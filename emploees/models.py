from django.db import models

from django.contrib.auth.models import AbstractUser

class Employee(AbstractUser):
    position = models.CharField(max_lenght=100, verbose_name='Должность')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.position})"

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    @property
    def active_tasks_count(self):
        return self.tasks.filter(status__in=['in_progress', 'assigned']).count()
