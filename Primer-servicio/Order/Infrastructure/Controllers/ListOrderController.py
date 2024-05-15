
from flask import Blueprint, jsonify
from Order.Application.ListOrderUseCase import ListOrderUseCase

get_list_orders_blueprint = Blueprint('get_list_orders', __name__)

def initialize_endpoints(repository):
    listOrderUseCase = ListOrderUseCase(repository)

    @get_list_orders_blueprint.route('/', methods=['GET'])
    def get_list_order():
        try:
            orders = listOrderUseCase.execute()
            orders = [order.to_dict() for order in orders]
            return jsonify(orders), 200
        except Exception as e:
            return jsonify({"message": "Error getting orders", "error": str(e)}), 400