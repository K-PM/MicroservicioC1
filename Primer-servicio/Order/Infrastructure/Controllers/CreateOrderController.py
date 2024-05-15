from flask import Blueprint, request, jsonify
from Order.Application.CreateOrderUseCase import CreateOrderdUseCase
from Order.Domain.Entities.AOrder import AOrder

create_order_blueprint = Blueprint('create_order', __name__)

def initialize_endpoints(repository):
    create_order_use_case = CreateOrderdUseCase(repository)

    @create_order_blueprint.route('/', methods=['POST'])
    def create_order():
        try:
            order_data = request.get_json()
            success, result = create_order_use_case.execute(AOrder(**order_data))
            
            if success:
                return jsonify({"message": "Order created", "order": result}), 200
            else:
                return jsonify({"message": "Error creating order", "error": result}), 400
        except Exception as e:
            return jsonify({"message": "Error in order", "error": str(e)}), 400