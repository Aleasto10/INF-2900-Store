#Cart logic

def get_or_create_cart(user):
    #given an user, get his undone cart
    #create a cart if none

    cart, created = Cart.objects.get_or_create(
        account = user,
        status = 'active'
    )

    return cart

def get_active_cart(user):
    #given an user, get his active cart
    #if none, return None

    try:
        return Cart.objects.get(account=user, status='active')
    except Cart.DoesNotExist:
        return None

def add_product_to_cart(user, product, quantity=1):
    #add a prodcut to the user's cart (must exist)
    #update the quantity of a product that's already on the cart
    #or add the product if new

    cart = get_or_create_cart(user)
    
    item, created = CartItem.objects.get_or_create(
        cart = cart,
        product = product
    )
    
    if not created: #old product
        item.item_quantity += quantity
    else: #new product
        item.item_quantity = quantity
    
    item.save()

def decrease_product_from_cart(user, product, quantity=1):
    #decrease a prodcut to the user's cart (must exist)
    #update the quantity of a product that's already on the cart
    #delete product if quantity reaches 0

    cart = get_active_cart(user)
    if not cart:
        return

    item = CartItem.objects.get(cart=cart, product=product)
    
    new_quantity = item.item_quantity - quantity
    if new_quantity > 0:
        item.item_quantity = new_quantity
        item.save()
    else:
        item.delete()

def remove_product_from_cart(user, product):
    #remove a product from the user's cart (must exist)

    cart = get_active_cart(user)
    if not cart:
        return

    item = CartItem.objects.get(cart=cart, product=product)
    
    item.delete()

def set_quantity_of_a_product_in_a_cart(user, product, quantity):
    #set the quantity of a product in the user's cart
    #if the product is new, add it and then set its quantity
    #if existent product, update quantity

    cart = get_or_create_cart(user)

    item, created = CartItem.objects.get_or_create(
        cart = cart,
        product = product
    )
    
    if quantity > 0:
        item.item_quantity = quantity
        item.save()
    else:
        item.delete()

def update_status(user, status):
    #change the status of the user's cart

    cart = get_or_create_cart(user)

    cart.status = status

    cart.save()