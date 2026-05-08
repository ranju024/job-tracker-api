from rest_framework import serializers
from .models import JobApplication

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:  # u put your configuration about the serializer in Meta class
        model = JobApplication  # which model it is based on
        fields = '__all__'  # include every field from the model in this serializer
        read_only_fields = ['id', 'created_at', 'updated_at', 'user']  # read only fields; user can't update these
