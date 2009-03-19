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
	author = models.ForeignKey(Person, related_name='questions')
	score = models.IntegerField()
	
	def __unicode__(self):
		return self.title

class Answer(models.Model):
	body = models.TextField()
	date_added = models.DateTimeField()
	score = models.IntegerField()
	author = models.ForeignKey(Person, related_name='answers')
	question = models.ForeignKey(Question, related_name='answers')
	
	def __unicode__(self):
	    return "Answer to Question %s (%s)" % (self.question.title, self.date_added)
	
	
class Group(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField()
    members = models.ManyToManyField(Person, related_name="group_members")

    class Meta:
        verbose_name_plural = "groups"
	def __unicode__(self):
		return self.name
