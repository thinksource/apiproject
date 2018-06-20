import unittest
from django.test.testcases import TestCase
from django.test import Client
import json

from pulse.models import Pulse

pulse_dict = {
    "name": "My",
    "ctype": "primitive",
    "maximum_rabi_rate": "10",
    "polar_angle": "0.5"
}

post_data={
    "name": "My",
    "type": "primitive",
    "maximum_rabi_rate": "10",
    "polar_angle": "0.5"
}

class ViewTestCase(TestCase):
    def setUp(self):
        Pulse.objects.create(**pulse_dict)
        self.client = Client()


    def test_list(self):
        response=self.client.get('/api/pulses?page=1')
        # self.assertValidJSONResponse(response)
        self.assertEqual(response.status_code,200)
        jobj=json.loads(response.content)
        self.assertTrue(len(jobj)<=5)
        self.assertTrue(len(jobj)>=0)
        keys=list(jobj[0].keys())
        self.assertIn('id', keys)
        self.assertIn('type',keys)
        self.assertIn('maximum_rabi_rate', keys)
        self.assertIn('polar_angle', keys)

    def test_create(self):
        response=self.client.post('/api/create_pulse/', data=post_data)
        self.assertEqual(response.status_code,201)
        keys=list(json.loads(response.content).keys())
        self.assertIn('id', keys)
        self.assertIn('type',keys)
        self.assertIn('maximum_rabi_rate', keys)
        self.assertIn('polar_angle', keys)

    def test_view_error(self):
        response=self.client.get('/api/pulse/0')
        self.assertEqual(response.status_code, 404)
    
    