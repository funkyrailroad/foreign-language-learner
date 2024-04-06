from django.test import TestCase

class Test(TestCase):
    def test(self):
        resp = self.client.get("/example_app/")
        self.assertEqual(resp.status_code, 200)
