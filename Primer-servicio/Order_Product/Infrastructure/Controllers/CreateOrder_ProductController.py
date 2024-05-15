from flask import Blueprint, request, jsonify
from Order_Product.Application.CreateOrder_ProductUseCase import CreateOrder_ProductUseCase
from Order_Product.Domain.Entities.AOrderProduct import AOrderProduct

create_order_product_blueprint = Blueprint('create_order_product', __name__)

def initialize_endpoints(repository):
    create_order_product_use_case = CreateOrder_ProductUseCase(repository)

    @create_order_product_blueprint.route('/', methods=['POST'])
    def create_order_product():
        try:
            order_product_data = request.get_json()
            success, result = create_order_product_use_case.execute(AOrderProduct(**order_product_data))
            
            if success:
                return jsonify({"message": "Order created", "order_product": result}), 200
            else:
                return jsonify({"message": "Error creating order_product", "error": result}), 400
        except Exception as e:
            return jsonify({"message": "Error in order_product", "error": str(e)}), 400



