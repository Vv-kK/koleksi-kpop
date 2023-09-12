from django.test import TestCase, Client

# Create your tests here.
from django.test import TestCase, Client
from main.models import Item
import datetime

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
                
    def test_created_items(self):
        Item.objects.create(name="Attaca", amount=3, artist="Seventeen",
                            release_date=datetime.date(2021, 10, 21), 
                            description = "9th mini album from Seventeen with the title trach ""Rock With You""")
        
        Item.objects.create(name="The War", amount=3, artist="EXO",
                            release_date=datetime.date(2017, 7, 18),
                            description="4th full album from EXO with the title track ""Ko Ko Bop""")

        attaca = Item.objects.get(name="Attaca")
        the_war_exo = Item.objects.get(name="The War")
        self.assertEqual(attaca.name, "Attaca")
        self.assertEqual(the_war_exo.name, "The War")