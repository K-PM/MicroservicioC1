import { AProduct as ProductDomain } from '../Domain/Entities/AProduct';

export class CreateProductUseCase {
    private repository: any;

    constructor(repository: any) {
        this.repository = repository;
    }

    async execute(product: ProductDomain): Promise<[boolean, ProductDomain | { error: string }]> {
        try {
            await this.repository.save(product);
            return [true, product];
        } catch (e: any) { // Captura cualquier tipo de error
            return [false, { error: e.toString() }];
        }
    }
}
