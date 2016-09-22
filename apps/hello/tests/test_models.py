from django.test import TestCase

from apps.hello.models import PersonalData


class PersonalDataModelTests(TestCase):

    def test_str(self):
        """ test for PersonalData output"""
        data = PersonalData(name='name')
        self.assertEqual(str(data), u'name ')
