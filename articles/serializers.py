from rest_framework import serializers
from .models import NYT, Guardian, NYT_Comment, Guardian_Comment


class NYT_CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = NYT_Comment
        fields = ['post', 'user', 'created_at', 'comment']
        read_only_fields = ['user']



class Guardian_CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    post = serializers.PrimaryKeyRelatedField(queryset=NYT.objects.all(), write_only=True)

    class Meta:
        model = Guardian_Comment
        fields = ['post', 'user', 'created_at', 'comment']
        read_only_fields = ['user']




class NYTSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()
    class Meta:
        model = NYT
        fields = ['id', 'title', 'abstract', 'url', 'img_url', 'section', 'paper', 'comment']

    def get_comment(self, obj):
        comment = NYT_Comment.objects.filter(post=obj)
        serializer = NYT_CommentSerializer(comment, many=True)
        return serializer.data


class GuardianSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()
    class Meta:
        model = Guardian
        fields = ['id', 'title', 'url', 'section', 'paper', 'comment']

    def get_comment(self, obj):
        comment = Guardian_Comment.objects.filter(post=obj)
        serializer = Guardian_CommentSerializer(comment, many=True)
        return serializer.data
