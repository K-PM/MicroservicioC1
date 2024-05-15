
from Order.Infrastructure.Routes.Routes import initialize_app as initialize_app_order
from Order.Infrastructure.Repositories.MysqlRepository import Repository as RepositoryOrder

from Order_Product.Infrastructure.Routes.Routes import initialize_app as initialize_app_order_product
from Order_Product.Infrastructure.Repositories.MysqlRepository import Repository as RepositoryOrderProduct

from flask import Flask
app = Flask(__name__)

repository_order = RepositoryOrder()
repository_order_product = RepositoryOrderProduct()

initialize_app_order(app, repository_order)
initialize_app_order_product(app, repository_order_product)

if __name__ == "__main__":
    app.run(debug=True, port='3002')