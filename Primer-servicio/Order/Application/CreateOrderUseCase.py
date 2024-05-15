from Order.Domain.Entities.AOrder import AOrder as OrderDomain

class CreateOrderdUseCase:
    def __init__( self, repository ):
        self.repository = repository

    def execute( self, OrderDomain ):
        try:
            self.repository.save(OrderDomain)
            return True, OrderDomain
        except Exception as e:
            return False, {"error": str(e)}


