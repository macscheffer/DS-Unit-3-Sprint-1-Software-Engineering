import unittest
import random

from acme import Product, BoxingGlove
from acme_report import generate_products


class AcmeProductTests(unittest.TestCase):

    '''
    Making sure Acme products are the tops!
    '''

    def test_default_product_price(self):
        '''
        Test default price being 10.
        '''
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

        
    def test_default_product_weight(self):
        '''
        Test default weight being 20
        '''
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

 
    def test_default_product_flammability(self):
        '''
        Test default flammability being 0.5
        '''
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_default_product_stealability(self):
        '''
        Test default product stealability
        '''
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), 'kinda stealable')

    def test_default_product_explosion(self):
        '''
        Test default product flammability
        '''
        prod = Product('Test Product')
        self.assertEqual(prod.explode(), '...boom!')

    def test_nondefault_product_explosion(self):
        '''
        Test non-default product flammability
        '''
        prod = Product('Test Product', flammability=500)
        self.assertEqual(prod.explode(), '...BABOOM!!!')

class AcmeReportTests(unittest.TestCase):

    '''
    Ensuring Acme reporting is as great as it should be
    '''

    def test_default_num_products(self):
        '''
        Ensures we report 30 products by default
        '''
        self.assert_(len(generate_products()), 30)

    def test_legal_names(self):
        '''
        ensures product names in reports are valid
        '''
        adjs = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

        prods = generate_products()

        non_adjs = []
        non_nouns = []
        for prod in prods:
            if prod.name.split()[0] not in adjs:
                non_adjs.append(prod.name.split()[0])
            if prod.name.split()[1] not in nouns:
                non_nouns.append(prod.name.split()[1])
        self.assertEqual(len(non_adjs), 0)
        self.assertEqual(len(non_nouns), 0)

if __name__ == '__main__':
    unittest.main()


