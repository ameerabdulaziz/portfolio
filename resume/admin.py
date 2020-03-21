from django.contrib import admin

from resume.models import Experience, Project, Certificate, Field, Skill


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('course', 'university', 'field', 'date')


admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Field)
admin.site.register(Skill)
