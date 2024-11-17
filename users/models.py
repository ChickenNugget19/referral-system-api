from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    referral_code = models.CharField(max_length=10, unique=True, null=True, blank=True)
    password = models.CharField(max_length=255)  # Store hashed passwords in real projects
    referrer = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='referees')
    registration_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Automatically generate a unique referral code
        if not self.referral_code:
            import uuid
            self.referral_code = str(uuid.uuid4())[:8]
        super().save(*args, **kwargs)
