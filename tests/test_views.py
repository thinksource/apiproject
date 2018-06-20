from django.test.testcases import TestCase
from django.test import Client
import json
import csv
from pulse.models import Pulse

pulse_dict = {
    "name": "My",
    "ctype": "primitive",
    "maximum_rabi_rate": "10",
    "polar_angle": "0.5"
}

post_data={
    "name": "Test",
    "type": "cinbb",
    "maximum_rabi_rate": "20",
    "polar_angle": "0.2"
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
        self.assertIn('name',keys)
        self.assertIn('type',keys)
        self.assertIn('maximum_rabi_rate', keys)
        self.assertIn('polar_angle', keys)

    def test_create(self):
        response=self.client.post('/api/create_pulse/', data=post_data)
        self.assertEqual(response.status_code,201)
        keys=list(json.loads(response.content).keys())
        self.assertIn('id', keys)
        self.assertIn('name',keys)
        self.assertIn('type',keys)
        self.assertIn('maximum_rabi_rate', keys)
        self.assertIn('polar_angle', keys)

    def test_view_error(self):
        response=self.client.get('/api/pulse/0')
        self.assertEqual(response.status_code, 404)
        
    # def test_view(self):
    #     response=self.client.get('/api/pulse/1')
    #     self.assertEqual(response.status_code, 200)
    #     keys=list(json.loads(response.content).keys())
    #     self.assertIn('id', keys)
    #     self.assertIn('name',keys)
    #     self.assertIn('type',keys)
    #     self.assertIn('maximum_rabi_rate', keys)
    #     self.assertIn('polar_angle', keys)
    
    def test_view_update(self):
        response=self.client.post('/api/pulse/4', data=post_data)
        self.assertEqual(response.status_code, 201)
        jobj=json.loads(response.content)
        keys=list(jobj.keys())
        self.assertIn('name',keys)
        self.assertIn('type',keys)
        self.assertIn('maximum_rabi_rate', keys)
        self.assertIn('polar_angle', keys)
        self.assertEqual(jobj['name'],'Test')

    def test_view_delete(self):
        response=self.client.delete('/api/pulse/4')
        self.assertEqual(response.status_code,404)


def CSVTestCase(TestCase):

    def setUp(self):
        Pulse.objects.create(**pulse_dict)
        self.client = Client()

    def test_upload(self):
        with open('files/pulse.csv') as fp:
            response=self.client.post('/api/csv', {'file':fp})
            self.assertEqual(response.status_code, 201)
            jobj=json.loads(response.content)
            self.assertEqual(len(jobj), 5)
            keys=list(jobj[0].keys())
            self.assertIn('name',keys)
            self.assertIn('type',keys)
            self.assertIn('maximum_rabi_rate', keys)
            self.assertIn('polar_angle', keys)

    def test_download(self):
        response=self.client.get('/api/csv')
        self.assertEqual(response.status_code,200)
        csvobj=list(csv.reader(response.content))
        self.assertEqual(len(csvobj), 5)
        self.assertEqual(len(csvobj), 4)

  