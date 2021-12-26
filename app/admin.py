from django.contrib import admin
from .models import Profile, Experience, Education, Software, Technical, Publications, ScholarShip, Certifications
# Register your models here.

admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Software)
admin.site.register(Technical)
admin.site.register(Publications)
admin.site.register(ScholarShip)
admin.site.register(Certifications)