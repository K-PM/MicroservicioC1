from Order_Product.Domain.Entities.AOrderProduct import AOrderProduct as OrderProductDomain

class CreateOrder_ProductUseCase:
    def __init__( self, repository ):
        self.repository = repository

    def execute( self, OrderProductDomain ):
        try:
            self.repository.save(OrderProductDomain)
            return True, OrderProductDomain
        except Exception as e:
            return False, {"error": str(e)}


