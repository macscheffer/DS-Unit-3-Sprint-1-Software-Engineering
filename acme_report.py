import random
from acme import Product

def generate_products(n=30):
    '''
    generates a list of products that we can then return.
    '''
    
    adjs = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    nouns = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']
    
    
    return [Product(
        name = random.choice(adjs) + ' ' + random.choice(nouns),
        price = random.randint(5,100),
        weight = random.randint(5,100),
        flammability = random.uniform(0.0, 2.5)) for _ in range(n)]


def inventory_report(products):
    
    '''
    prints
        - the number of total products
        - the number of unique product names 
        - the average price of those products
        - the average weight of those products
        - the average flammability of those products
    '''
    
    unique = len(set([prod.name for prod in products]))
    avg_price = sum([prod.price for prod in products]) / len(products)
    avg_weight = sum([prod.weight for prod in products]) / len(products)
    avg_flammability = sum([prod.flammability for prod in products]) / len(products)
    
    print('Number of products %s' % len(products))
    print('Number of unique products %s' % round(unique,3))
    print('Average price of products %s' % round(avg_price,3))
    print('Average weight of products %s' % round(avg_weight,3))
    print('Average flammability of products %s' % round(avg_flammability,3))

if __name__ == '__main__':
    inventory_report(generate_products())
