def discounted(price, discount,max_discount=50):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Maximum discount too high')
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount

#product = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 50}

#product['with_discount'] = discounted(product['price'], product['discount'])


print(discounted(100,40))

