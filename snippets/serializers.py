from rest_framework import serializers
from snippets.models import Snippet, Meal, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')



class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('url', 'name', 'ingredients')