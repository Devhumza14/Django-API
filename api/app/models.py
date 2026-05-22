from django.db import models

class Program(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    # This creates the relationship/Foreign Key
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return self.name