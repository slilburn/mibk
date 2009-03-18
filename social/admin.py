from django.contrib import admin
from mibk.social.models import Person, Group, Question, Answer

admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Question)
admin.site.register(Answer)
