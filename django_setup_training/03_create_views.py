# from rest_framework.views import APIView, Response, status
# from 01_create_models import CustomUser, Role
# from 02_create_serualizers import CustomUserSerializer, RoleSerializer

# class RoleDisplay(APIView):

#   def get(self, request):

#      role_filter_id = CustomUser.objects.all().values_list("created_by", flat=True).distinct()   

#     data = {
#       "role_data": RoleSerializer(Role.objects.all(), many=True).data
#       "role_order_data": RoleSerializer(Role.objects.order_by("-created_at"), many=True).data
#       "role_filter_data": RoleSerializer(Role.objects.filter(id__exact=1,name__icontains="ceo",created_at__range=[date_from,date_to]), many=True).data,  
#       "role_filter_exclude_data": RoleSerializer(Role.objects.filter(is_cancelled=False,user__in=role_filter_id).exclude(user__isnull=True).value_list("user",flat=True))
#     }

#     return Response(data, status=status.HTTP_200_OK)

#   def post(self, request):

#     data = {
#       "role_name":request.data["name"]
#     }

#     role_data = RoleSerializer(data=data):

#     if role_data.is_valid():

#       role_data.save()

#       return Response(role_data.data, status=status.HTTP_201_CREATED)

#     else:

#       return Response(role_data.errors, status=status.HTTP_400_BAD_REQUEST)

#   def put(self, request):

#     data = {
#       "role_name":request.data["name"]
#     }

#     update_role = Role.objects.get(pk=request.data["id"])

#     new_role = RoleSerializer(update_role, data=data, partial=True)

#     if new_role.is_valid():

#       new_role.save()

#       return Response(new_role.data, status=status.HTTP_201_CREATED)
#     else:
#       return Response(new_role.errors, status=status.HTTP_400_BAD_REQUEST)
  
#   def delete(self, request):

#     delete_role = Role.objects.get(pk=request.data["id"]) 

#     delete_role.delete()

#     return Response(status=status.HTTP_200_OK) 
