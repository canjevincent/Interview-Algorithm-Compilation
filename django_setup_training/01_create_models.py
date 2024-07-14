# from django.db import models
# from datetime import datetime
# from django.conf import settings
# from django.core.validators import validate_email


# def file_image_size(value):

#   if value != None:
#     limit = 5 * 1024 * 1024

#     if value.size > limit:
#       raise validationError("File too large. Size should not exceed 5 MB.")
    
#     ext = os.splitext(value.name)[1]
#     valid_extensions = [".jpg",".png",".jpeg",".gif"]

#     if not ext.lower() in valid_extensions:
#       raise validationError("Unsupported file extension.")
    
# class Role(models.Model):
#   id = models.AutoField(primary_key=True)
#   name = models.CharField(max_length=60, validators=[])
#   description = models.TextField(max_length=60, validators=[])
#   status = models.BooleanField(default=True)
#   created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="role_created_by", null=False)
#   created_at = models.DateTimeField(default=datetime.now, blank=True)
#   updated_at = models.DateTimeField(auto_now=True)

# class CustomUser(models.Model):
#   id = models.AutoField(priamry_key=True)
#   image = models.ImageField(null=True, blank=True, validators=[file_image_size], upload_to="file_folder")
#   email = models.EmailField(max_length=60, unique=True, validators=[validate_email])
#   is_email_validated = models.BooleanField(default=False)
#   role = models.ForeignKey(Role, on_delete=models.DO_NOTHING, default=2, blank=False, null=False)
#   username = models.CharField(max_length=30, unique=True, blank=False)
#   password = models.charField(max_length=300)
#   date_joined = models.DateTimeField(auto_now_add=True)
#   last_login = models.DatetimeField(auto_now=True)
#   created_by = models.ForeignKey("self", on_delete=models.DO_NOTHING, default=None, blank=False, null=False)