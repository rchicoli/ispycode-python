
prices = &#123;
   'AA': 20.00,
   'BB': 10.12,
   'CC': 13.21,
   'DD': 57.15,
   'EE': 44.99
&#125;
minimum = min(zip(prices.keys(), prices.values()))
print( minimum )


