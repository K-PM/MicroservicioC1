from Database.mysqlConection import DBConnection, OrderModel
from Order.Domain.Entities.AOrder import AOrder as OrderDomain

class Repository:
    def __init__( self ):
        self.connection =DBConnection()
        self.session = self.connection.Session()

    def save( self, OrderDomain ):
        order = OrderModel(
            order_uuid= OrderDomain.order_uuid,
            total =   OrderDomain.total,
            date = OrderDomain.date,
            status = OrderDomain.status,  
            order_produc_uuid = OrderDomain.order_produc_uuid   

        )
        self.session.add( order )
        self.session.commit()
        return order
    
    def list_all( self ):
        order = self.session.query(OrderModel).all()
        return order



    

