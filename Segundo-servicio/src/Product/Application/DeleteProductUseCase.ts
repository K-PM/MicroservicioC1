export class DeleteProductUseCase {
    private repository: any;

    constructor(repository: any) {
        this.repository = repository;
    }

    async execute(productId: string): Promise<boolean> {
        const product = await this.repository.get_by_id(productId);
        if (!product) {
            throw new Error('Product_id not found');
        } else {
            await this.repository.delete(productId);
            return true;
        }
    }
}
