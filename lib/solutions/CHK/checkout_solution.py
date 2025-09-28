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
            "A": [3, 130],
            "B": [2, 45]
        }
        
        sku_counter = Counter(skus)
            
        for sku, count in sku_counter.items():
            if sku not in item_price_map:
                return -1
            if sku in item_specials_map:
                special_count, special_price = item_specials_map[sku]
                remaining_count = count
                while remaining_count >= special_count:
                    price = special_price
                    price += remaining_count*item_price_map[sku]
                    total_price += price
                    remaining_count - special_count
                    
                total_price += remaining_count*item_price_map[sku]
            else:
                total_price += count*item_price_map[sku]
        
        return total_price
                    

chkout = CheckoutSolution()
price = chkout.checkout("AAAAAA")
print(price)
