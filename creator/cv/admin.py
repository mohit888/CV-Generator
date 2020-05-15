from django.contrib import admin

# Register your models here.
from .models import resume_data,skills,experience,Education

admin.site.register(resume_data)
admin.site.register(skills)
admin.site.register(experience)
admin.site.register(Education)