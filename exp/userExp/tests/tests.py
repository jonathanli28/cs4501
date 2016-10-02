from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from myapp.models import Order, User

class GetOrderDetailsTestCase(TestCase):
  def setUp(self):     #setUp method is called before each test in this class
     pass              #nothing to set up
  def success_response(self):
     response = self.client.get(reverse('all_orders_list', kwargs={'user_id':1}))   #assumes user with id 1 is stored in db
     self.assertContains(response, 'order_list')  #checks that response contains parameter order list & implicitly checks that                                                 #statuscode is 200
  def fails_invalid(self):
     response = self.client.get(reverse('all_orders_list'))
     self.assertEquals(response.status_code, 404)    #user_id not given in url, so error

  def tearDown(self):  #tearDown method is called after each test
     pass              #nothing to tear down