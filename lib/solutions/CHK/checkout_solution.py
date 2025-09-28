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
    
    
    # skus = unicode string
    def checkout(self, skus: str) -> int:
        
        if not skus:
            return -1
        
        total_price = 0
        sku_counter = Counter(skus)
            
        for sku, count in sku_counter.items():
            if sku not in self.item_price_map:
                return -1
            total_price += self._calculate_sku_price(sku, count)
        
        return total_price
                
    def _calculate_sku_price(self, sku: str, count: int) -> int:
        if sku not in self.item_specials_map:
            return count * self.item_price_map[sku]
        else:
            special_count, special_price = self.item_specials_map[sku]
            num_specials = count // special_count
            remainder = count % special_count
            return num_specials*special_price + remainder*self.item_price_map[sku]



