from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=100, default="Creative")
    typed_items = models.CharField(max_length=255, help_text="Comma-separated items for Typed.js")
    description = models.TextField()

    projects_completed = models.PositiveIntegerField(default=0)
    years_experience = models.PositiveIntegerField(default=0)
    happy_clients = models.PositiveIntegerField(default=0)

    cta_primary_text = models.CharField(max_length=50, default="View My Work")
    cta_primary_link = models.URLField(default="#portfolio")
    cta_secondary_text = models.CharField(max_length=50, default="Get In Touch")
    cta_secondary_link = models.URLField(default="#contact")

    image = models.ImageField(upload_to="hero/", null=True, blank=True)

    skill_1_icon = models.CharField(max_length=50, default="bi bi-palette")
    skill_1_title = models.CharField(max_length=50, default="UI/UX Design")

    skill_2_icon = models.CharField(max_length=50, default="bi bi-code-slash")
    skill_2_title = models.CharField(max_length=50, default="Development")

    skill_3_icon = models.CharField(max_length=50, default="bi bi-lightning")
    skill_3_title = models.CharField(max_length=50, default="Creative Ideas")

    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} Section"

    def get_typed_list(self):
        return [item.strip() for item in self.typed_items.split(",")]

