
from django.db import models
from djongo import models as djongo_models
from bson import ObjectId

# Team model

class Team(djongo_models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# User model

class User(djongo_models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = djongo_models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')

    def __str__(self):
        return self.name

# Activity model

class Activity(djongo_models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    user = djongo_models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.name} - {self.activity_type} on {self.date}"

# Workout model

class Workout(djongo_models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for = djongo_models.ManyToManyField(User, blank=True, related_name='suggested_workouts')

    def __str__(self):
        return self.name

# Leaderboard model

class Leaderboard(djongo_models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    team = djongo_models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')
    total_points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.team.name} - {self.total_points} points"
