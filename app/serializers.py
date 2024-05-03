from rest_framework import serializers
from .models import NoteApp

class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = NoteApp
        fields = '__all__'