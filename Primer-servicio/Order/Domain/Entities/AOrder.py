from dataclasses import dataclass,field
from Order.Domain.StatusType import StatusType
import uuid

@dataclass
class AOrder:
    order_uuid : str = field(default_factory=uuid.uuid4, init=False)
    total: int
    date: str
    status: StatusType
    order_produc_uuid: str


    def to_dict(self):
        return{
            'order_uuid': self.order_uuid,
            'total': self.total,
            'date': self.date,
            'status': self.status,
            'order_produc_uuid':self.order_produc_uuid,
        }


