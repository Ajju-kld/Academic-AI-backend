from rest_framework import serializers
from .models import User, Task, Assesments

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    subject = serializers.StringRelatedField(source='subject.subject_name', read_only=True)
    class Meta:
        model = Task
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = User
        fields = ('clg_id','name','is_admin','password', 'dept', 'semester', 'scheme', 'credits', 'study_time')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        
        user = User.objects.create_user(**validated_data)
      
        return user
    
class AssesmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assesments
        fields = '__all__'
