# Create your views here.
from django.http import HttpResponse
from models import Person

def showpeople(response):
	people = Person.objects.all()
	html = "<html><body>"
	for person in people:
		html += "<p>%s %s has an email address that goes a little bit like this: %s</p>" % (person.first_name, person.last_name, person.email)
	html += "</body></html>"
	return(HttpResponse(html))
