from rest_framework import fields, serializers
from .models import stu,staff
 
class staffserializer(serializers.ModelSerializer):
    class Meta:
        model=staff
        fields=('name','salaty')

class stuserializer(serializers.ModelSerializer):
    class Meta:
        model=stu
        fields=('name','roll_no')