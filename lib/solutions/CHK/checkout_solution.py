from collections import Counter


class CheckoutSolution:
    """
    Our price table and offers:
    +------+-------+----------------+
    | Item | Price | Special offers |
    +------+-------+----------------+
    | A    | 50    | 3A for 130     |
    | B    | 30    | 2B for 45      |
    | C    | 20    |                |
    | D    | 15    |                |
    +------+-------+----------------+
    """
    
    # skus = unicode string
    def checkout(self, skus: str) -> int:
        
        total_price = 0
        
        item_price_map = {
            "A" : 50,
            "B": 30,
            "C": 20,
            "D": 15
        }
        
        item_specials_map = {
            "A": [3, 150],
            "B": [2, 45]
        }
        
        sku_counter = Counter(skus)
            
        for sku, count in sku_counter.items():
            if sku not in item_price_map:
                return -1
            if sku in item_specials_map:
                special_count, special_price = item_specials_map[sku]
                if count >= special_count:
                    
                    
            
            
        

chkout = CheckoutSolution()
price = chkout.checkout("abaacdef")
print(price)




