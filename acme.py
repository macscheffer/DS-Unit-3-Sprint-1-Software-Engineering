
import random

'''
Product Classes for Acme 
'''


class Product():

    '''
    Base product for Acme.
    '''
    
    def __init__(self, name, price=10, weight=20, flammability=.5):
        
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)
        
    def stealability(self):
        
        '''
        Returns the stealability of a product.
        '''

        stealability_score = float(self.price) / float(self.weight)
        
        if stealability_score < .5:
            return 'not so stealable'
        if stealability_score >= .5 and stealability_score < 1:
            return 'kinda stealable'
        else:
            return 'very stealable'
        
    def explode(self):
        
        '''
        returns a message regarding the fact boxing gloves dont explode.
        '''
        
        flammability_score = float(self.flammability) * float(self.weight)
        
        if flammability_score < 10:
            return '...fizzle'
        if flammability_score >= 10 and flammability_score < 50:
            return '...boom!'
        else:
            return '...BABOOM!!!'
        
class BoxingGlove(Product):

    '''
    Boxing glove product.
    '''
    
    def __init__(self, name, price=10, weight=10, flammability=.5):
        
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)
    
    def explode(self):
        return '...its a glove'
    
    
    def punch(self):
        
        '''
        takes a good swing at someone 
        and returns their response based on the gloves weight.
        '''
        
        if self.weight < 5:
            return 'That tickles.'
        
        if self.weight >= 5 and self.weight < 15:
            return 'Hey that hurt!'
        
        else:
            return 'OUCH!'

