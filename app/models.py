from django.db import models
from django.contrib.auth.models import User
# Create your models here.
def upload_here(instance,filename):
    return "updates/{user}/{filename}".format(user=instance.user,filename=filename)
class Status(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    image=models.ImageField(upload_to=upload_here,null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.content)[:50]
    class Meta:
        verbose_name='Status Post'
        verbose_name_plural='Status posts'