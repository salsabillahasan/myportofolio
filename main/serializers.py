
from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Project, Experience, Education


class ProjectSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()
    tech_list = serializers.SerializerMethodField()
    image_src = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "tech_stack",
            "tech_list",
            "project_url",
            "project_image_url",
            "project_image",    
            "image_src",
            "star_count",
            "is_starred",
            "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Title cannot be empty."
            )
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_tech_stack(self, value):
        return strip_tags(value)

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(
            user.username for user in obj.starred_by.all()
        )

    def get_tech_list(self, obj):
        return obj.tech_list

    def get_image_src(self, obj):
        return obj.image_src


class ExperienceSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()
    logo_src = serializers.SerializerMethodField()
    photo_src = serializers.SerializerMethodField()
    clear_logo_image = serializers.BooleanField(
        write_only=True,
        required=False,
        default=False,
    )

    clear_photo_image = serializers.BooleanField(
        write_only=True,
        required=False,
        default=False,
    )


    class Meta:
        model = Experience
        fields = [
            "id",
            "title",
            "role",
            "category",
            "started_at",
            "ended_at",
            "description",
            "thumbnail",
            "photo_url",
            "logo_image",
            "photo_image",
            "clear_logo_image",
            "clear_photo_image",
            "logo_src",
            "photo_src",
            "star_count",
            "is_starred",
            "starred_by_names",
        ]
        read_only_fields = ["id"]
        extra_kwargs = {
            "logo_image": {"write_only": True},
            "photo_image": {"write_only": True},
        }

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Title cannot be empty."
            )
        return value

    def validate_role(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Role cannot be empty."
            )
        return value

    def validate_description(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Description cannot be empty."
            )
        return value

    def validate(self, attrs):
        start = attrs.get(
            "started_at",
            getattr(self.instance, "started_at", None)
        )
        end = attrs.get(
            "ended_at",
            getattr(self.instance, "ended_at", None)
        )

        if start and end and end < start:
            raise serializers.ValidationError({
                "ended_at": "End date cannot be earlier than start date."
            })

        return attrs

    def create(self, validated_data):
        validated_data.pop("clear_logo_image", None)
        validated_data.pop("clear_photo_image", None)

        return super().create(validated_data)

    def update(self, instance, validated_data):
        clear_logo = validated_data.pop(
            "clear_logo_image", False
        )

        clear_photo = validated_data.pop(
            "clear_photo_image", False
        )

        if clear_logo:
            instance.logo_image = None

        if clear_photo:
            instance.photo_image = None

        return super().update(instance, validated_data)

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(
            user.username for user in obj.starred_by.all()
        )

    def get_logo_src(self, obj):
        return obj.logo_src

    def get_photo_src(self, obj):
        return obj.photo_src


class EducationSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()
    logo_src = serializers.SerializerMethodField()
    clear_logo_image = serializers.BooleanField(
        write_only=True,
        required=False,
        default=False,
    )


    class Meta:
        model = Education
        fields = [
            "id",
            "institution",
            "degree",
            "field_of_study",
            "started_at",
            "ended_at",
            "description",
            "thumbnail",
            "logo_image",
            "clear_logo_image",
            "logo_src",
            "star_count",
            "is_starred",
            "starred_by_names",
        ]
        read_only_fields = ["id"]
        extra_kwargs = {
            "logo_image": {"write_only": True},
        }

    def validate_institution(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Institution cannot be empty."
            )
        return value

    def validate_degree(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Degree cannot be empty."
            )
        return value

    def validate_field_of_study(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Field of study cannot be empty."
            )
        return value

    def validate_description(self, value):
        return strip_tags(value).strip()

    def validate(self, attrs):
        start = attrs.get(
            "started_at",
            getattr(self.instance, "started_at", None)
        )
        end = attrs.get(
            "ended_at",
            getattr(self.instance, "ended_at", None)
        )

        if start and end and end < start:
            raise serializers.ValidationError({
                "ended_at": "End date cannot be earlier than start date."
            })

        return attrs
    
    def create(self, validated_data):
        validated_data.pop("clear_logo_image", None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        clear_logo = validated_data.pop(
            "clear_logo_image", False
        )

        if clear_logo:
            instance.logo_image = None

        return super().update(instance, validated_data)


    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")

        if request is None or not request.user.is_authenticated:
            return False

        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(
            user.username for user in obj.starred_by.all()
        )

    def get_logo_src(self, obj):
        return obj.logo_src

