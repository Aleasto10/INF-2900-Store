#cart testing

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Cart, CartItem, Product
from .cart_service import (
    add_product_to_cart,
    decrease_product_from_cart,
    remove_product_from_cart,
    set_quantity_of_a_product_in_a_cart,
    update_status,
)

class CartBackendTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="1234"
        )

        self.product = Product.objects.create(
            name="Laptop",
            description="Test product",
            price=100,
            stock_quantity=10,
            origin_country="Norway"
        )

    def test_add_product_creates_cart(self):
        add_product_to_cart(self.user, self.product, 1)

        cart = Cart.objects.get(account=self.user, status='active')
        self.assertEqual(cart.items.count(), 1)

    def test_add_same_product_increases_quantity(self):
        add_product_to_cart(self.user, self.product, 1)
        add_product_to_cart(self.user, self.product, 3)

        cart = Cart.objects.get(account=self.user, status='active')
        item = cart.items.first()

        self.assertEqual(item.item_quantity, 4)

    def test_decrease_product(self):
        add_product_to_cart(self.user, self.product, 3)
        decrease_product_from_cart(self.user, self.product, 1)

        cart = Cart.objects.get(account=self.user, status='active')
        item = cart.items.first()

        self.assertEqual(item.item_quantity, 2)

    def test_decrease_to_zero_removes_item(self):
        add_product_to_cart(self.user, self.product, 1)
        decrease_product_from_cart(self.user, self.product, 1)

        cart = Cart.objects.get(account=self.user, status='active')
        self.assertEqual(cart.items.count(), 0)

    def test_remove_product(self):
        add_product_to_cart(self.user, self.product, 2)
        remove_product_from_cart(self.user, self.product)

        cart = Cart.objects.get(account=self.user, status='active')
        self.assertEqual(cart.items.count(), 0)

    def test_set_quantity(self):
        add_product_to_cart(self.user, self.product, 1)
        set_quantity_of_a_product_in_a_cart(self.user, self.product, 5)

        cart = Cart.objects.get(account=self.user, status='active')
        item = cart.items.first()

        self.assertEqual(item.item_quantity, 5)

    def test_checkout_updates_status(self):
        add_product_to_cart(self.user, self.product, 1)
        update_status(self.user, 'checked_out')

        cart = Cart.objects.get(account=self.user)
        self.assertEqual(cart.status, 'checked_out')