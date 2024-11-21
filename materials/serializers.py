from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import validate_youtube_link


class LessonSerializer(serializers.ModelSerializer):
    linc_to_video = serializers.CharField(validators=[validate_youtube_link], read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)

    def get_count_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ('title', 'preview', 'description', 'owner', 'count_lessons', 'lessons',)


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
