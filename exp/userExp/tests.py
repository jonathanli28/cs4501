from django.test import TestCase, Client
from django.core.urlresolvers import reverse
import unittest


class GetItemTestCase(TestCase):
  def setUp(self):     #setUp method is called before each test in this class
     pass              #nothing to set uunpit

  def test_success_response(self):
     #response = self.client.get(reverse('itemPage', kwargs={'pk':'1'}))   #assumes user with id 1 is stored in db
     #self.assertContains(response, 'pk')  #checks that response contains parameter order list & implicitly checks that                                                 #statuscode is 200
     #self.assertEqual(response.status_code, 200)
    
  def tearDown(self):  #tearDown method is called after each test
     pass  

#  def test_fails_invalid(self):
 #    response = self.client.get(reverse('itemPage'))
  #   self.assertEquals(response.status_code, 404)    #user_id not given in url, so error
            #nothing to tear down

class GetHomePageTestCase(TestCase):
    def setUp(self):     #setUp method is called before each test in this class
        pass              #nothing to set uunpit

    def test_success_response(self):
        response = self.client.get(reverse('homePage'))  #assumes user with id 1 is stored in db
        self.assertEqual(response.status_code, 200)
    def tearDown(self):  #tearDown method is called after each test
        pass
