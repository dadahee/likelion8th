from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    text = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        if len(self.text)>100: return self.text[:100] + "..."
        return self.text