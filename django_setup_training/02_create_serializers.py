# from rest_framework import serializers
# from .models import CustomUser, Role

# class CustomUserSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = CustomUser
#     fields = ["id","image","email","is_email_validated","role","username","password","date_joined","last_login","created_by"]
#     extra_kwargs = {"email":{
#                               "min_length":8,
#                               "error_messages":{
#                                 "blank": "Email is required."
#                               }
#                             },
#                     "username":{
#                                 "min_length":4,
#                                 "error_messages":{
#                                   "blank":"Username is required."
#                                 }
#                                }
#                    }

# class RoleSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Role
#     fields = ["id","name","status","created_by","created_at","updated_at"]
#     extra_kwargs = {"name":{
#                             "min_length":3,
#                             "error_messages":{
#                               "blank":"Role name is required."
#                             }
#                            }
#                    }