from django.test import TestCase

from pulse.models import Pulse


pulse_dict = {
    "name": "My",
    "ctype": "primitive",
    "maximum_rabi_rate": "10",
    "polar_angle": "0.5"
}


class PulseTestCase(TestCase):
    def setUp(self):
        Pulse.objects.create(**pulse_dict)

    def tearDown(self):
        #Clean up run after every test method.
        pass

    def test_model(self):
        t = Pulse.objects.get(name="My")
        self.assertEqual(t["name"], "My")
        self.assertEqual(t["ctype"], "primitive")
        self.assertEqual(t['maximum_rabi_rate'], 10)
        self.assertEqual(t["polar_angle"], 0.5)

