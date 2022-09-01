from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class AvailabilityPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('availability'):
            return item
        else:
            raise DropItem(f"Produit indisponible {item}")