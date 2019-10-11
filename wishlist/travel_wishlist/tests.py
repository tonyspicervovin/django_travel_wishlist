from django.test import TestCase
from django.urls import reverse

from .models import Place
# Create your tests here.

class TestHomePageIsEmptylist(TestCase):

    def test_load_home_page_shows_empty_list(self):

        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assertFalse(response.context['places'])
        self.assertContains(response, 'You have no places in your wishlist')


class TestWishList(TestCase):

    fixtures = ['test_places']

    def test_view_wishlist_contains_not_visited_places(self):

        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        self.assertContains(response, 'Tokyo')
        self.assertContains(response, 'New York')
        self.assertNotContains(response, 'San Francisco')
        self.assertNotContains(response, 'Moab')
#tests places are displayed with test data, only not visited

class TestNotVisited(TestCase):

    def test_visited_displays_you_have_not_visited(self):

        response = self.client.get(reverse('places_visited'))
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')
        self.assertFalse(response.context['visited'])
        self.assertContains(response, 'You have not visited any places yet')
#tests that displays you have not visited any places on visited tab with no data

class TestOnlyVisited(TestCase):

    fixtures = ['test_places']

    def test_only_visited_displayed(self):

        response = self.client.get(reverse('places_visited'))
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')

        self.assertContains(response, 'Moab')
        self.assertContains(response, 'San Francisco')
        self.assertNotContains(response, 'Jamaica')
        self.assertNotContains(response, 'Colorado')
    #tests that only visited places are shown on visited tab
