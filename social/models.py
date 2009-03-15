from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "people"
        
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
        
