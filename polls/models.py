from django.db import models
from django.utils import timezone

# se trabaja todo lo relacionado a datos de la app
# Create your models here.
''' transformar la programacion ortientada  a objetos a lenguaje relaional para la base de datos ''' 
class Question (models.Model):
    #id -- es automatico y el framework lo hace por debajo 
    question_test = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_test;
    
    def was_published_recientely(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
    
    
class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)   #on_delete=models.CASCADE significa que todas las respuestas se van a almacenar en cascada
    choise_test = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choise_test;
    


