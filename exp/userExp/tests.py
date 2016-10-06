from django.test import TestCase, Client
from django.core.urlresolvers import reverse
import unittest, json

class GetItemTestCase(TestCase):
  def setUp(self):     #setUp method is called before each test in this class
     pass              #nothing to set uunpit

     #test if response is successful given a legitimate pk 
  def test_success_response(self):
     response = self.client.get(reverse('itemPage', kwargs={'pk':'1'}))   #assumes user with id 1 is stored in db
     self.assertContains(response, 'pk')  #checks that response contains parameter order list & implicitly checks that                                                 #statuscode is 200
     self.assertEqual(response.status_code, 200)
    
  #primary key does not exist 
  def test_fails_invalid(self):
     response = self.client.get(reverse('itemPage', kwargs={'pk':'0'}))
     jsonResponse = json.loads(str(response.content, encoding='utf8'))
     self.assertEquals(jsonResponse["status"], False)  

  def test_itemFields(self):
     response = self.client.get(reverse('itemPage', kwargs={'pk':'1'}))
     jsonResponse = json.loads(str(response.content, encoding='utf8'))
     #test for the most essential fields of the bike model
     self.assertEquals(jsonResponse["status"], True)  
     self.assertContains(response, 'pk')
     self.assertContains(response, 'name')
     self.assertContains(response, 'bike_description')
     self.assertContains(response, 'average_star_rating')

  def tearDown(self):  #tearDown method is called after each test
     pass  

class GetItemDescriptionTestCase(TestCase):
  def setUp(self):     #setUp method is called before each test in this class
     pass              #nothing to set uunpit

     #test if response is successful given a legitimate pk 
  def test_success_response(self):
     response = self.client.get(reverse('itemPage', kwargs={'pk':'1'}))   #assumes user with id 1 is stored in db
     self.assertContains(response, 'pk')  #checks that response contains parameter order list & implicitly checks that                                                 #statuscode is 200
     self.assertEqual(response.status_code, 200)
    
  #primary key does not exist 

  def test_itemDescription(self):
     response = self.client.get(reverse('itemPage', kwargs={'pk':'1'}))
     jsonResponse = json.loads(str(response.content, encoding='utf8'))
     #test for the most essential fields of the bike model
     self.assertEquals(jsonResponse["status"], True)  
     self.assertContains(response, 'bike_description')

  def tearDown(self):  #tearDown method is called after each test
     pass  

class GetItemRatingTestCase(TestCase):
  def setUp(self):     #setUp method is called before each test in this class
     pass              #nothing to set uunpit

     #test if response is successful given a legitimate pk 
  def test_success_response(self):
     response = self.client.get(reverse('itemPage', kwargs={'pk':'1'}))   #assumes user with id 1 is stored in db
     self.assertContains(response, 'pk')  #checks that response contains parameter order list & implicitly checks that                                                 #statuscode is 200
     self.assertEqual(response.status_code, 200)
    
  #primary key does not exist 

  def test_itemReview(self):
     response = self.client.get(reverse('itemPage', kwargs={'pk':'1'}))
     jsonResponse = json.loads(str(response.content, encoding='utf8'))
     #test for the most essential fields of the bike model
     self.assertEquals(jsonResponse["status"], True)  
     self.assertContains(response, 'average_star_rating')

  def tearDown(self):  #tearDown method is called after each test
     pass  

  
class GetItemStyleTestCase(TestCase):
  def setUp(self):     #setUp method is called before each test in this class
     pass              #nothing to set uunpit

     #test if response is successful given a legitimate pk 
  def test_success_response(self):
     response = self.client.get(reverse('itemPage', kwargs={'pk':'1'}))   #assumes user with id 1 is stored in db
     self.assertContains(response, 'pk')  #checks that response contains parameter order list & implicitly checks that                                                 #statuscode is 200
     self.assertEqual(response.status_code, 200)
    
  #primary key does not exist 

  def test_itemStyle(self):
     response = self.client.get(reverse('itemPage', kwargs={'pk':'1'}))
     jsonResponse = json.loads(str(response.content, encoding='utf8'))
     #test for the most essential fields of the bike model
     self.assertEquals(jsonResponse["status"], True)  
     self.assertContains(response, 'bike_style')

  def tearDown(self):  #tearDown method is called after each test
     pass  

class GetHomePageTestCase(TestCase):
    def setUp(self):     #setUp method is called before each test in this class
        pass              #nothing to set uunpit

    def test_success_response(self):
        response = self.client.get(reverse('homePage'))  #assumes user with id 1 is stored in db
        self.assertEqual(response.status_code, 200)

    def test_success_recentBikeFields(self):
        response = self.client.get(reverse('homePage'))  #assumes user with id 1 is stored in db
        self.assertEqual(response.status_code, 200)
        jsonResponse = json.loads(str(response.content, encoding='utf8'))
        self.assertContains(response, 'bike1')
        self.assertContains(response, 'bike2')
        self.assertContains(response, 'bike3')
    def tearDown(self):  #tearDown method is called after each test
        pass
