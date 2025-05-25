# pages/admin.py
from django.contrib import admin
from .models import Project, TeamMember, ProjectImage # Import ProjectImage

# Inline for ProjectImage
class ProjectImageInline(admin.TabularInline): # Or admin.StackedInline for a different layout
    model = ProjectImage
    extra = 1 # Number of empty forms to display for adding new images (e.g., show 1 by default)
    fields = ('image', 'caption') # Specify fields to show in the inline form
    # readonly_fields = ('uploaded_at',) # If you want to show readonly fields

# Custom Admin for Project
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'focus_area', 'status', 'is_signature_project', 'created_at')
    list_filter = ('status', 'is_signature_project', 'focus_area')
    search_fields = ('title', 'description_short', 'description_long')
    prepopulated_fields = {'slug': ('title',)} # Auto-fills slug from title as you type
    inlines = [ProjectImageInline] # Add the ProjectImage inline here

# Unregister the default Project admin if it was registered simply
# admin.site.unregister(Project) # Only if you previously did admin.site.register(Project)
# Then register Project with the custom ProjectAdmin
admin.site.register(Project, ProjectAdmin)

# Ensure TeamMember is still registered
admin.site.register(TeamMember) # Or create a TeamMemberAdmin if you want to customize it too

# You can also register ProjectImage separately if you want a dedicated admin page for it,
# but managing it via inlines is often more convenient.
# admin.site.register(ProjectImage)