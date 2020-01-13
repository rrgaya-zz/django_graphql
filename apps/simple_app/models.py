from django.db import models
from django.contrib import auth



class Tenant(models.Model):
    name = models.CharField(max_length=100)
    subdomain_prefix = models.CharField(max_length=100, unique=True)
        
    def __str__(self):
        return self.name


class TenantAwaredModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Messages(TenantAwaredModel):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    create_date = models.DateField(auto_now=True)
    message = models.TextField()

    def __str__(self):
        return f"USER: {self.user} - MESSAGE: {self.message}"
    