from rest_framework import serializers
from .models import JobApplication, StatusHistory, Interview

class StatusHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusHistory
        fields = "__all__"
        read_only_fields = ["id", "changed_at"]

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate(self, attrs):
        application = attrs.get("application")

        if application and application.user != self.context["request"].user:
            raise serializers.ValidationError(
                "You cannot add an interview to another user's application."
            )

        return attrs

class JobApplicationSerializer(serializers.ModelSerializer):
    status_history = StatusHistorySerializer(many=True, read_only=True)
    interviews = InterviewSerializer(many=True, read_only=True)

    class Meta:
        model = JobApplication
        fields = [
            "id",
            "user",
            "company",
            "title",
            "url",
            "location",
            "work_type",
            "salary_min",
            "salary_max",
            "status",
            "source",
            "notes",
            "date_applied",
            "created_at",
            "updated_at",
            "status_history",
            "interviews",
        ]

        read_only_fields = [
            "id",
            "user",
            "created_at",
            "updated_at",
            "status_history",
            "interviews",
        ]

    def validate(self, attrs):
        salary_min = attrs.get("salary_min")
        salary_max = attrs.get("salary_max")

        if salary_min is not None and salary_max is not None:
            if salary_min > salary_max:
                raise serializers.ValidationError(
                    "Minimum salary cannot be greater than maximum salary."
                )

        return attrs