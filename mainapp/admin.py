from django.contrib import admin
from .models import Project, ProjectImage, Patner, Advert


# Register your models here.

admin.site.site_header = "Aicad Administration"
admin.site.site_title = "AICAD"

# admin.site.register(Project)
class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage

admin.site.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin]

    class Meta:
        model=Project

admin.site.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Patner)


admin.site.register(Advert)
