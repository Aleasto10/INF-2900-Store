from django.test import TestCase
from decimal import Decimal

# importing the service functions and model from our app
from courses import product as product_service
            
            
class ProductServiceTests(TestCase):
    def create_sample(self, **overrides):
        
        params = {
            "name": "sample",
            "description": "a sample product",
            "price": Decimal("9.99"),
            "stock": 10,
            "origin": "Norway",
        }

        params.update(overrides)
        return product_service.create_product(
            name=params["name"],
            description=params["description"],
            price=params["price"],
            stock=params["stock"],
            origin=params["origin"],
        )

    def test_create_product(self):
        product = self.create_sample(name="lootbox", description="loot", price=Decimal("12.99"), stock=5, origin="China")

        self.assertIsNotNone(product.id)
        self.assertEqual(product.name, "lootbox")
        self.assertEqual(product.description, "loot")
        self.assertEqual(product.price, Decimal("12.99"))
        self.assertEqual(product.stock_quantity, 5)
        self.assertEqual(product.origin_country, "China")

    # test get_product_by_id
    def test_get_product(self):
        p = self.create_sample()

        found = product_service.get_product_by_id(p.id)
        self.assertIsNotNone(found)
        self.assertEqual(found.id, p.id)

        not_found = product_service.get_product_by_id(999999)
        self.assertIsNone(not_found)


    def test_get_all_products(self):
        p1 = self.create_sample(name="p1")
        p2 = self.create_sample(name="p2")

        all_products = product_service.get_all_products()
        self.assertGreaterEqual(len(all_products), 2)
        names = [p.name for p in all_products]
        self.assertIn("p1", names)
        self.assertIn("p2", names)


    def test_update_product(self):
        p = self.create_sample()

        p_name = product_service.update_product_name(p.id, "new-name")
        self.assertEqual(p_name.name, "new-name")

        p_desc = product_service.update_product_description(p.id, "new-desc")
        self.assertEqual(p_desc.description, "new-desc")

        p_price = product_service.update_product_price(p.id, Decimal("1.23"))
        self.assertEqual(p_price.price, Decimal("1.23"))

        p_stock = product_service.update_product_stock(p.id, 42)
        self.assertEqual(p_stock.stock_quantity, 42)

        p_country = product_service.update_product_country(p.id, "Sweden")
        self.assertEqual(p_country.origin_country, "Sweden")

    def test_delete_product_success_and_failure(self):
        p = self.create_sample()
        # delete existing
        result = product_service.delete_product(p.id)
        self.assertTrue(result)
        self.assertIsNone(product_service.get_product_by_id(p.id))

        # delete non-existing
        self.assertFalse(product_service.delete_product(999999))


def __main__():
    unittest.main()



