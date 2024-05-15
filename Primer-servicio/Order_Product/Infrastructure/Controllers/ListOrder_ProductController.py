
from flask import Blueprint, jsonify
from Order_Product.Application.ListOrder_ProductUseCase import ListOrder_ProductUseCase

get_list_orders_products_blueprint = Blueprint('get_list_orders_products', __name__)

def initialize_endpoints(repository):
    listOrderProductUseCase = ListOrder_ProductUseCase(repository)

    @get_list_orders_products_blueprint.route('/', methods=['GET'])
    def get_list_order_product():
        try:
            ordersProducts = listOrderProductUseCase.execute()
            ordersProducts = [orderProduct.to_dict() for orderProduct in ordersProducts]
            return jsonify(ordersProducts), 200
        except Exception as e:
            return jsonify({"message": "Error getting ordersProducts", "error": str(e)}), 400