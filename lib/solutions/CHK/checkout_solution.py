from collections import Counter


class CheckoutSolution:
    """
    Our price table and offers:
    +------+-------+------------------------+
    | Item | Price | Special offers         |
    +------+-------+------------------------+
    | A    | 50    | 3A for 130, 5A for 200 |
    | B    | 30    | 2B for 45              |
    | C    | 20    |                        |
    | D    | 15    |                        |
    | E    | 40    | 2E get one B free      |
    +------+-------+------------------------+
    """
    item_price_map = {
            "A" : 50,
            "B": 30,
            "C": 20,
            "D": 15,
            "E": 40
        }
        
    item_specials_map = {
        "A": [(5, 200), (3, 130)],
        "B": [(2, 45)]
    }
    
    cross_item_offers_map = {
        "E": [(2, "B", 1)]
    }
    
    
    # skus = unicode string
    def checkout(self, skus: str) -> int:
        
        if not skus:
            return 0
        
        total_price = 0
        sku_counter = Counter(skus)
            
        for sku in set(skus):
            if sku not in self.item_price_map:
                return -1    
        
        for trigger_sku, offers in self.cross_item_offers_map.items():
            num_triggers = sku_counter.get(trigger_sku, 0)
        
        for sku, count in sku_counter.items():
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


