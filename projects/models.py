from django.db import models

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  technology = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  # updated_at = models.DateTimeField(auto_now=True)
  # owner = models.ForeignKey('auth.User', related_name='projects', on_delete=models.CASCADE)
  # collaborators = models.ManyToManyField('auth.User', related_name='shared_projects')
  
  def __str__(self):
    return self.title
  
