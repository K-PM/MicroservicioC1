from Order_Product.Infrastructure.Controllers.CreateOrder_ProductController import create_order_product_blueprint, initialize_endpoints as initialize_endpoints_create_order_product
from Order_Product.Infrastructure.Controllers.ListOrder_ProductController import get_list_orders_products_blueprint, initialize_endpoints as initialize_endpoints_list_order_product

def initialize_app ( app, repository ):
    initialize_endpoints_create_order_product( repository )
    initialize_endpoints_list_order_product( repository )

    app.register_blueprint( create_order_product_blueprint, url_prefix="/create-order-product" )
    app.register_blueprint( get_list_orders_products_blueprint, url_prefix="/list-order-product" )



