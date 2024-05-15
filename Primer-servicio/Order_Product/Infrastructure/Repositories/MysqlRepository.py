from Database.mysqlConection import DBConnection, Order_ProducModel
from Order_Product.Domain.Entities.AOrderProduct import AOrderProduct as OrderProductDomain


class Repository:
    def __init__( self ) :
        self.connection = DBConnection()
        self.session = self.connection.Session()

    def save ( self, OrderProductDomain ):
        order_product = Order_ProducModel(
            order_produc_uuid = OrderProductDomain.order_produc_uuid,
            producto_id = OrderProductDomain.producto_id,
            precio = OrderProductDomain.precio,
            cantidad = OrderProductDomain.cantidad,
            

        )
        self.session.add( order_product )
        self.session.commit()

        return order_product
    
    def list_all( self ):
        order_product = self.session.query(Order_ProducModel).all()
        return order_product

