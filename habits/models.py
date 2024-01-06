from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):

    PERIOD_CHOICES = [
        ('daily', 'Ежедневная'),
        ('weekly', 'Раз в неделю')
    ]

    ACTION_CHOICES = [
        ('walk', 'Гулять на свежем воздухе'),
        ('drink', 'Пить больше воды'),
        ('good_mood', 'Быть всегда в хорошем настроении')

    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='создатель привычки', **NULLABLE)
    place = models.CharField(max_length=200, verbose_name='место', **NULLABLE)
    time = models.DateTimeField(verbose_name='время', **NULLABLE)
    action = models.CharField(max_length=200, choices=ACTION_CHOICES,
                              verbose_name='действие', **NULLABLE)
    is_nice = models.BooleanField(default=False,
                                  verbose_name='признак приятной привычки')
    habits = models.ForeignKey('Habit', on_delete=models.CASCADE,
                               verbose_name='связанная привычка', **NULLABLE)
    period = models.CharField(max_length=50, choices=PERIOD_CHOICES,
                              verbose_name='периодичность', **NULLABLE)
    lead_time = models.IntegerField(verbose_name='время на выполнение',
                                    **NULLABLE)
    reward = models.CharField(max_length=100,
                              verbose_name='вознаграждение', **NULLABLE)
    is_public = models.BooleanField(default=False,
                                    verbose_name='признак публичности')

    def __str__(self):
        return f'{self.user} - {self.action}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
