from rest_framework import serializers, exceptions, fields

from profile.models import WorkExperience, Education, LicenseAndCertification, VolunteerExperience, Course, Project, TestScore, Skill, SocialProfile

from userauth.models import User, UserProfile

from userauth.serializers import UserProfileSerializer

from rest_framework import status 

import json


class WorkExperienceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   = WorkExperience
        fields  = '__all__'
        
    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['user'] = UserProfileSerializer(instance.user, context = {'request': self.context.get('request')}).data
        return response
    
    
    
class EducationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   = Education
        fields  = '__all__'
        
    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['user'] = UserProfileSerializer(instance.user, context = {'request': self.context.get('request')}).data
        return response



class LicenseAndCertificationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   = LicenseAndCertification
        fields  = '__all__'
        
    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['user'] = UserProfileSerializer(instance.user, context = {'request': self.context.get('request')}).data
        return response
    
    
class VolunteerExperienceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   = VolunteerExperience
        fields  = '__all__'
        
    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['user'] = UserProfileSerializer(instance.user, context = {'request': self.context.get('request')}).data
        return response
    
    

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   = Course
        fields  = '__all__'
        
    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['user'] = UserProfileSerializer(instance.user, context = {'request': self.context.get('request')}).data
        return response
    

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   = Project
        fields  = '__all__'
        
    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['user'] = UserProfileSerializer(instance.user, context = {'request': self.context.get('request')}).data
        return response
    
    
class TestScoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   = TestScore
        fields  = '__all__'
        
    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['user'] = UserProfileSerializer(instance.user, context = {'request': self.context.get('request')}).data
        return response
  
  
    
from profile.models import SKILLS
class SkillSerializer(serializers.ModelSerializer):
    
    skills_list        = fields.MultipleChoiceField(choices = SKILLS)
    
    
    class Meta:
        model   = Skill
        fields  = '__all__'
        
    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['user'] = UserProfileSerializer(instance.user, context = {'request': self.context.get('request')}).data
        response['top_skills'] = json.decoder.JSONDecoder().decode(instance.top_skills)
        return response
    
    
class SocialProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   = SocialProfile
        fields  = '__all__'
        
    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['user'] = SkillSerializer(instance.user, context = {'request': self.context.get('request')}).data
        return response