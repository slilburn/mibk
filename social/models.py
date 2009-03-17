from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    
    class Meta:
        verbose_name_plural = "people"
        
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
        
class Group(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField()
    members = models.ManyToManyField(Person)
    
    class Meta:
        verbose_name_plural = "groups"
        
