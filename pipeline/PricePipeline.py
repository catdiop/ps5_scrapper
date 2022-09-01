from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

from settings import BUDGET_MIN, BUDGET_MAX

class PricePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        price = adapter.get('price')
        if price and price >= BUDGET_MIN and price <= BUDGET_MAX:
            return item
        else:
            raise DropItem(f"{price} supérieur à budget")