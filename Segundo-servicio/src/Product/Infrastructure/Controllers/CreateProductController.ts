import { Request, Response, Router } from 'express';
import { CreateProductUseCase } from '../../Application/CreateProductUseCase';
import { AProduct } from '../../Domain/Entities/AProduct';

const createProductRouter = Router();

function initializeEndpoints(repository: any) {
    const createProductUseCase = new CreateProductUseCase(repository);
    '/create-product'
    createProductRouter.post('/create-product', async (req: Request, res: Response) => {
        try {
            const productData: AProduct = req.body;
            const [success, result] = await createProductUseCase.execute(new AProduct(
                productData.name,
                productData.precio,
                productData.stock
            ));

            if (success) {
                return res.status(200).json({ message: 'Product created', Product: result });
            } else {
                return res.status(400).json({ message: 'Error creating Product', error: result });
            }
        } catch (e: any) {
            return res.status(400).json({ message: 'Error in Product', error: e.toString() });
        }
    });
}

export { createProductRouter, initializeEndpoints };
