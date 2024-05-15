
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  ForeignKey, create_engine, Column, Integer, String, Float,Enum
from Order.Domain.StatusType import StatusType 
from sqlalchemy.orm import relationship


Base = declarative_base()


class OrderModel(Base):
    __tablename__ = 'orders'

    id = Column( Integer, primary_key = True )
    order_uuid = Column(String(36), unique=True)
    total = Column( Integer,nullable=False )
    date = Column( String(50),nullable=False )
    status = Column( Enum(StatusType) )
    
    # Relación uno a uno con Order_ProducModel
    order_produc = relationship("Order_ProducModel", uselist=False, back_populates="order")

    def to_dict(self):
        return{
            'id': self.id,
            'order_uuid': self.order_uuid,
            'total': self.total,
            'date': self.date,
            'status': self.status,

            'order_produc_uuid': self.order_produc.order_produc_uuid if self.order_produc else None,
        }

class Order_ProducModel(Base):
    __tablename__='order_products'

    id = Column( Integer, primary_key = True )
    order_produc_uuid = Column(String(36), unique=True)
    producto_id = Column( Integer, nullable=False )
    precio = Column( Float, nullable=False )
    cantidad = Column( Integer, nullable=False )

    # foránea que apunta a la tabla orders
    order_uuid = Column(String(36), ForeignKey('orders.order_uuid'))
    # Relación inversa con OrderModel
    order = relationship("OrderModel", back_populates="order_produc")
    
    def to_dict(self):
        return{
            'id':id,
            'order_produc_uuid':self.order_produc_uuid,
            'producto_id':self.producto_id,
            'precio':self.precio,
            'cantidad':self.cantidad,
            
            'order_uuid': self.order_uuid
        }
    

class DBConnection:
    def __init__(self):
        load_dotenv()

        host = os.getenv('DB.HOST_MYSQL')
        port = os.getenv('DB.PORT_MYSQL')
        user = os.getenv('DB.USER_MYSQL')
        password = os.getenv('DB.PASSWORD_MYSQL')
        database = os.getenv('DB.DATABASE_MYSQL')

        try:
            self.engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
            Base.metadata.create_all(self.engine)
            self.Session = sessionmaker(bind=self.engine)
            print("Conexión exitosa a la base de datos con MySQL LISTA!")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {str(e)}")
