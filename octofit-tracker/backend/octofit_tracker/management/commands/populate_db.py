from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # 既存データ削除（forループで個別削除）
        for model in [Activity, Workout, Leaderboard, User, Team]:
            for obj in model.objects.all():
                if obj.pk:
                    obj.delete()

        # チーム作成
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # ユーザー作成
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # アクティビティ作成
        Activity.objects.create(user=users[0], type='run', duration=30, date=date(2026, 5, 1))
        Activity.objects.create(user=users[1], type='cycle', duration=45, date=date(2026, 5, 2))
        Activity.objects.create(user=users[2], type='swim', duration=25, date=date(2026, 5, 3))
        Activity.objects.create(user=users[3], type='run', duration=40, date=date(2026, 5, 1))
        Activity.objects.create(user=users[4], type='cycle', duration=35, date=date(2026, 5, 2))
        Activity.objects.create(user=users[5], type='swim', duration=50, date=date(2026, 5, 3))

        # ワークアウト作成
        w1 = Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes')
        w2 = Workout.objects.create(name='Strength Training', description='Strength for all heroes')
        w1.suggested_for.set(users[:3])
        w2.suggested_for.set(users[3:])

        # リーダーボード作成
        Leaderboard.objects.create(team=marvel, score=100)
        Leaderboard.objects.create(team=dc, score=120)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
