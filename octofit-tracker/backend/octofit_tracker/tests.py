from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class SimpleModelTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='test')
        self.assertEqual(str(team), 'test')
    def test_user_create(self):
        team = Team.objects.create(name='test2')
        user = User.objects.create(name='hero', email='hero@test.com', team=team)
        self.assertEqual(str(user), 'hero')
