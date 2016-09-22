import datetime
from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from apps.hello.models import PersonalData


class TestContactData(TestCase):

    def setUp(self):
        PersonalData.objects.all().delete()
        PersonalData.objects.create(
            name='name',
            last_name='lastname',
            date_of_birth=datetime.datetime.now().date(),
            bio='bio',
            email='some@email.com',
            jabber='some@jabber.com',
            other_contacts='contacts'
        )

    def test_one(self):
        """ test for one object in database """
        self.client = Client()
        self.url = reverse('home')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertIn('name', response.content)
        self.assertIn('lastname', response.content)
        self.assertIn('bio', response.content)
        self.assertIn('some@email.com', response.content)
        self.assertIn('some@jabber.com', response.content)
        self.assertIn('contacts', response.content)

    def test_more_than_one(self):
        """ test for more than one object in database """
        PersonalData.objects.all().delete()
        PersonalData.objects.get_or_create(
            name='name1',
            last_name='lastname1',
            date_of_birth=datetime.datetime.now().date(),
            bio='bio1',
            email='some1@email.com',
            jabber='some1@jabber.com',
            other_contacts='contacts1'
        )
        PersonalData.objects.get_or_create(
            name='name2',
            last_name='lastname2',
            date_of_birth=datetime.datetime.now().date(),
            bio='bio2',
            email='some2@email.com',
            jabber='some2@jabber.com',
            other_contacts='contacts2'
        )
        self.client = Client()
        self.url = reverse('home')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('name1', response.content)
        self.assertIn('lastname1', response.content)
        self.assertIn('bio1', response.content)
        self.assertIn('some1@email.com', response.content)
        self.assertIn('some1@jabber.com', response.content)
        self.assertIn('contacts1', response.content)
