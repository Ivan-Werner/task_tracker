from django.db import models

from django.contrib.auth.models import AbstractUser

class Employee(AbstractUser):
    position = models.CharField(max_length=100, blank=True, null=True, verbose_name='Должность')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='employee_groups',  # Уникальное имя
        related_query_name='employee',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='employee_permissions',  # Уникальное имя
        related_query_name='employee',
    )

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
