from django.test import TestCase
from accounts.models import UserProfile
from communication.models import Icon
from notifications.models import Notification
from django.contrib.auth.models import User


class NotificationModelTest(TestCase):
    def setUp(self):
        # Create a caregiver user profile
        caregiver_user = User.objects.create_user(
            username='caregiver',
            password='password123'
        )
        self.caregiver = UserProfile.objects.create(
            user=caregiver_user,
            name='Caregiver Test',
            email='caregiver@example.com',
            role='CG'
        )

        # Create an end user profile
        user_user = User.objects.create_user(
            username='enduser',
            password='password123'
        )
        self.end_user = UserProfile.objects.create(
            user=user_user,
            name='End User Test',
            email='enduser@example.com',
            role='USER'
        )

        # Create an icon
        self.icon = Icon.objects.create(
            caregiver=self.caregiver,
            name='Test Icon',
            is_active=True
        )

    def test_notification_creation(self):
        # Create a notification
        notification = Notification.objects.create(
            caregiver=self.caregiver,
            user=self.end_user,
            icon=self.icon,
            is_sent=True
        )

        # Assertions
        self.assertEqual(notification.caregiver, self.caregiver)
        self.assertEqual(notification.user, self.end_user)
        self.assertEqual(notification.icon, self.icon)
        self.assertTrue(notification.is_sent)
        self.assertIsNotNone(notification.notified_at)

    def test_notification_string_representation(self):
        notification = Notification.objects.create(
            caregiver=self.caregiver,
            user=self.end_user,
            icon=self.icon,
            is_sent=True
        )
        caregiver = self.caregiver
        icon_name = self.icon_name
        expected_string = f"Notification to {caregiver} about {icon_name}"
        self.assertEqual(str(notification), expected_string)
