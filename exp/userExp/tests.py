from django.test import TestCase, Client
from django.core.urlresolvers import reverse
import unittest, json

#project 3 test cases 
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
     self.assertContains(response, 'speeds')

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
     self.assertContains(response, 'speeds')

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

 #project 4 test cases        
#tests login and logout cases, two separate test cases combined into one
class loginLogoutTestCase(TestCase):
    def setUp(self):     #setUp method is called before each test in this class
        pass              #nothing to set uunpit

    def test_success_response(self):
        response = self.client.post(reverse('loginPage'), {'username': 'ianian', 'passwd': 'hello'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'status')
        self.assertContains(response, 'auth')

    def test_success_loginCapability(self):

        response = self.client.post(reverse('loginPage'), {'username': 'ianian', 'passwd': 'hello'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'status')
        self.assertContains(response, 'auth')
        ret = response.content.decode('utf-8')
        ret = json.loads(ret)
        self.assertEqual(ret['status'], True)
        
        response = self.client.post(reverse('logoutPage'), {'auth': ret['auth']})
        ret = response.content.decode('utf-8')
        ret = json.loads(ret)
        self.assertEquals(ret['status'], True)
        self.assertEqual(response.status_code, 200)
        

    def tearDown(self):  #tearDown method is called after each test
        pass

class createItemTestCase(TestCase):
    def setUp(self):     #setUp method is called before each test in this class
        pass              #nothing to set uunpit

    def test_success_CreateCapability(self):
        #login first 
        response = self.client.post(reverse('loginPage'), {'username': 'ianian', 'passwd': 'hello'})
        ret = response.content.decode('utf-8')
        ret = json.loads(ret)
        response = self.client.post(reverse('createitemPage'), {"picture": "",
                "name": 'big bike',
                "bike_style": 'pretty',
                "brake_style": 'great brakes',
                "color": 'green',
                "frame_material": 'kryptonite',
                "speeds": 'high speed',
                "package_height": '20 ft',
                "shipping_weight": '20 pounds',
                "wheel_size": '10 inches',
                "bike_description": 'super awesome bike bro',
                "auth":ret['auth']
                })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ret['status'], True)

        response = self.client.post(reverse('logoutPage'), {'auth': ret['auth']})
       
    def tearDown(self):  #tearDown method is called after each test
        pass

#tests account creation and account creation right after one is created
class CreateAccountTestCase(TestCase):
    def setUp(self):     #setUp method is called before each test in this class
        pass              #nothing to set uunpit

    def test_success_createAccount(self):
        response = self.client.post(reverse('createaccountPage'),
         {'username': 'super_unique', 'passwd': 'super_unique_pass', 'first_name':'tester', 'last_name':'tester', 'email':'tester@virginia.edu'})
        ret = response.content.decode('utf-8')
        ret = json.loads(ret)
        self.assertEqual(response.status_code, 200)
        self.assertEquals(ret['status'], True)

    def test_success_createFailAccount(self):
        
        response = self.client.post(reverse('createaccountPage'),
         {'username': 'super_unique', 'passwd': 'super_unique_pass', 'first_name':'tester', 'last_name':'tester', 'email':'tester@virginia.edu'})
        ret = response.content.decode('utf-8')
        ret = json.loads(ret)
        self.assertEqual(response.status_code, 200)
        self.assertEquals(ret['status'], False)


    def tearDown(self):  #tearDown method is called after each test
        pass

class GetCreateInvalidAccountTestCase(TestCase):
    def setUp(self):     #setUp method is called before each test in this class
        pass              #nothing to set uunpit

    def test_success_createFailAccount(self):
        
        response = self.client.post(reverse('createaccountPage'),
         {'username': 'ianian', 'passwd': 'super_unique_pass', 'first_name':'tester', 'last_name':'tester', 'email':'tester@virginia.edu'})
        ret = response.content.decode('utf-8')
        ret = json.loads(ret)
        self.assertEqual(response.status_code, 200)
        self.assertEquals(ret['status'], False)


    def tearDown(self):  #tearDown method is called after each test
        pass
