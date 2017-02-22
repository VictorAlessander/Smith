# coding: UTF-8


import unittest
import requests
from bs4 import BeautifulSoup as BSoup


class TestSmith(unittest.TestCase):

	def setUp(self):
		self.link = requests.get("https://github.com/VictorAlessander")


	def test_response(self):
		self.assertTrue(self.link)
		self.assertNotEqual(self.link.status_code, 404)

	def test_soup(self):
		self.soup = BSoup(self.link.content, "html.parser")
		#self.name = self.assertNotEqual(
		#	self.soup.find('h1', attrs={'class': 'vcard-names'}), None)
		self.result = self.assertIn(
			self.soup.find('span',
			attrs={'class': 'vcard-fullname d-block', 
				'itemprop': 'name'}).text, "Victor Alessander")


if __name__ == "__main__":
	unittest.main()