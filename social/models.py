from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    
    class Meta:
        verbose_name_plural = "people"
        
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Question(models.Model):
	title = models.CharField(max_length=120)
	body = models.TextField()
	date_added = models.DateTimeField()
	author = models.ForeignKey(Person,related_name='questions')
	score = models.IntegerField()

class Answer(models.Model):
	body = models.TextField()
	date_added = models.DateTimeField()
	score = models.IntegerField()
	author = models.ForeignKey(Person,related_name='answers')
