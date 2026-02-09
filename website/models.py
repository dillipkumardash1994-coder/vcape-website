from django.db import models

class SiteSettings(models.Model):
    institute_name = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255, blank=True)
    logo = models.ImageField(upload_to="site/", blank=True, null=True)

    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    footer_text = models.TextField(blank=True)

    google_map_iframe = models.TextField(
        blank=True,
        help_text="Paste Google Map iframe code"
    )

    def save(self, *args, **kwargs):
        if not self.pk and SiteSettings.objects.exists():
            return
        super().save(*args, **kwargs)

    def __str__(self):
        return self.institute_name

class HomeContent(models.Model):
    welcome_title = models.CharField(max_length=255)
    welcome_text = models.TextField()

    def __str__(self):
        return "Home Page Content"

class AboutContent(models.Model):
    purpose = models.TextField()
    vision = models.TextField()
    mission = models.TextField()

    def __str__(self):
        return "About Page Content"

class Program(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    bullet_points = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def bullet_list(self):
        return [line for line in self.bullet_points.splitlines() if line]

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('leadership', 'Leadership'),
        ('advisor', 'Advisory Board'),
        ('mentor', 'Mentorship Network'),
    ]

    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=200)
    bio = models.TextField()
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    photo = models.ImageField(upload_to="team/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class MentorshipPhilosophy(models.Model):
    content = models.TextField()

    def __str__(self):
        return "Mentorship Philosophy"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
