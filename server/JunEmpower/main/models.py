from django.contrib.auth.models import AbstractUser
from django.db import models



class Specialization(models.Model):
    specialization = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.specialization
    
    
    
class Technology(models.Model):
    technology = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.technology
    
    
    

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to="uploads/profile/", blank=True, null=True)
    specialization_id = models.ForeignKey(Specialization, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.username



class Project(models.Model):
    author_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    technology = models.ForeignKey(Technology, on_delete=models.SET_NULL, blank=True, null=True)
    
    

class Like(models.Model):
    author_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)



class Comment(models.Model):
    author_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

