# pages/models.py
from django.db import models
from django.utils.text import slugify # To help create URL-friendly slugs
from django.urls import reverse # To help generate URLs for specific projects

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    focus_area = models.CharField(max_length=100, blank=True, help_text="e.g., Education, Environment, Health")
    description_short = models.TextField(help_text="A brief summary for the project card.")
    description_long = models.TextField(blank=True, null=True, help_text="Detailed information for the project's own page.")

    image = models.ImageField(
        upload_to='project_images/', # Images will be stored in MEDIA_ROOT/project_images/
        blank=True,
        null=True,
        help_text="A representative image for the project (optional)."
    )

    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if ongoing")
    status = models.CharField(
        max_length=50,
        choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed'), ('Planned', 'Planned')],
        default='Planned'
    )

    is_signature_project = models.BooleanField(default=False, help_text="Check if this is one of the main signature projects.")
    slug = models.SlugField(max_length=255, unique=True, blank=True, help_text="Leave blank to auto-generate from title, or provide a custom one.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            original_slug = self.slug
            counter = 1
            while Project.objects.filter(slug=self.slug).exists(): # Check for existing slugs
                # Check if the current instance is the one causing the conflict (for updates)
                conflicting_project = Project.objects.get(slug=self.slug)
                if conflicting_project.id == self.id:
                    break
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pages:project_detail', kwargs={'project_slug': self.slug})

# New TeamMember Model
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, help_text="e.g., President, Secretary, Member. For general members, can be 'Member'.")
    bio = models.TextField(blank=True, null=True, help_text="A short biography or role description.")
    photo = models.ImageField(
        upload_to='team_photos/',
        blank=True,
        null=True,
        help_text="Profile picture (optional)."
    )
    email = models.EmailField(blank=True, null=True, help_text="Contact email (optional).")
    official_term_start_year = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Enter the starting year of the term this person is an official (e.g., 2024 for the 2024-25 term). Leave blank if not an official or for general members."
    )
    display_order = models.PositiveIntegerField(
        default=100,
        help_text="Order of appearance for officials (e.g., 0 for President, 1 for VP). General members can have a higher number or default."
    )

    # New Fields to Add:
    joining_year = models.PositiveIntegerField(
        null=True, blank=True,
        help_text="Year the member joined the Rotaract club (e.g., 2023)."
    )
    rotaract_id = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Rotaract International ID (if applicable)."
    )
    contact_number = models.CharField(
        max_length=20,  # Increased length for international numbers with country code
        blank=True, null=True,
        help_text="Phone number (e.g., +91-9876543210) (optional)."
    )

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
        ('Unknown', 'Unknown/Not Specified'),
    ]
    blood_group = models.CharField(
        max_length=20, # Max length to accommodate "Unknown/Not Specified"
        choices=BLOOD_GROUP_CHOICES,
        blank=True, null=True,
        default='Unknown'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', 'name']

    def __str__(self):
        return f"{self.name} - {self.position}"

class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        related_name='gallery_images', # How we'll access these images from a Project object
        on_delete=models.CASCADE  # If a Project is deleted, its images are also deleted
    )
    image = models.ImageField(
        upload_to='project_gallery/', # Images will go to MEDIA_ROOT/project_gallery/
        help_text="Upload an image for the project gallery."
    )
    caption = models.CharField(max_length=200, blank=True, null=True, help_text="Optional caption for the image.")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['uploaded_at'] # Show images in the order they were uploaded

    def __str__(self):
        # Try to return the project title and image filename, handle if project is None (though unlikely with CASCADE)
        return f"Image for {self.project.title if self.project else 'N/A'} - {self.image.name.split('/')[-1]}"