from Order.Infrastructure.Controllers.CreateOrderController import create_order_blueprint, initialize_endpoints as initialize_endpoints_create_order
from Order.Infrastructure.Controllers.ListOrderController import get_list_orders_blueprint, initialize_endpoints as initialize_endpoints_list_order

def initialize_app ( app, repository ):
    initialize_endpoints_create_order( repository )
    initialize_endpoints_list_order( repository )

    app.register_blueprint( create_order_blueprint, url_prefix="/create-order" )
    app.register_blueprint( get_list_orders_blueprint, url_prefix="/list-order" )



