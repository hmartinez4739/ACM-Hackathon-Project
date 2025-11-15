from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    sdsu_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    profile_picture_url = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    def set_password(self, password):
        """Hash and set the password"""
        self.password_hash = make_password(password)

    def check_password(self, password):
        """Verify password against stored hash"""
        return check_password(password, self.password_hash)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.sdsu_id})"

