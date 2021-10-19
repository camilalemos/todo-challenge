from django.db import models

# Create your models here.

class Task(models.Model): 
    description = models.TextField(max_length=50)
    completed = models.BooleanField(default=False)
    creation_date = models.DateTimeField()

    def __str__(self):
        return "("+self.description+", "+str(self.completed)+", "+str(self.creation_date)+" )" 