from marshmallow import Schema, fields, validate

class BaseSerializer(Schema):
    @classmethod
    def serialize(cls, obj, many=False):
        """
        Shortcut method for using a serializer to serialize a Python object
        to a Python dictionary
        """
        return cls().dump(obj, many=many)

    @classmethod
    def deserialize(cls, obj, many=False):
        """
        Shortcut method for using a serializer to deserialize data
        """
        return cls().load(obj, many=many)

class Achievement(BaseSerializer):
    name = fields.Str(required=True)
    description = fields.Str(required=True)

class Achievements(Achievement):
    achievements: fields.List(fields.Nested(Achievement))

class AchievementProfileAchievement(Achievement):
    achievement = fields.Nested(Achievement)
    achieved_at = fields.DateTime(required=True)

class AchievementProfile(BaseSerializer):
    achievementProfile = fields.List(fields.Nested(AchievementProfileAchievement))
