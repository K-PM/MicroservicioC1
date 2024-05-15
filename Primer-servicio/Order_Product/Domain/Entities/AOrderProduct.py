from dataclasses import dataclass,field
import uuid

@dataclass
class AOrderProduct:
    order_produc_uuid: str = field( default_factory=uuid.uuid4, init=False )
    producto_id: int
    precio: float
    cantidad: int
    

    def to_dict(self):
        return{
            'order_produc_uuid':self.order_produc_uuid,
            'producto_id':self.producto_id,
            'precio':self.precio,
            'cantidad':self.cantidad,
            
        }