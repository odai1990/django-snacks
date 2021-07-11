from django.test import TestCase,SimpleTestCase
from django.urls import reverse

class Snacks_Test(SimpleTestCase):

    def testing_urls(self):

        # for home
        url_home=reverse('home')
        expacted_status_code_home=self.client.get(url_home).status_code
        actual_status_code_home=200
        self.assertEqual(expacted_status_code_home,actual_status_code_home)

        # for about

        url_about=reverse('about')
        expacted_status_code_about=self.client.get(url_about).status_code
        actual_status_code_about=200
        self.assertEqual(expacted_status_code_about,actual_status_code_about)

    def testing_templates(self):      

        # for home
        url_home=reverse('home')
        expacted_template_home=self.client.get(url_home)
        actual_template_home='home.html'
        self.assertTemplateUsed(expacted_template_home,actual_template_home)

        # for about

        url_about=reverse('about')
        expacted_template_about=self.client.get(url_about)
        actual_template_about='about.html'
        self.assertTemplateUsed(expacted_template_about,actual_template_about)