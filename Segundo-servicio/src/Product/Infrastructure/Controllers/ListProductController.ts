import { Request, Response, Router } from 'express';
import { ListProductUseCase } from '../../Application/ListProductUseCase';

const getListProductsRouter = Router();

function initializeEndpoints(repository: any) {
    const listProductUseCase = new ListProductUseCase(repository);

    getListProductsRouter.get('/list-products', async (req: Request, res: Response) => {
        try {
            const products = await listProductUseCase.execute();
            const productDicts = products.map(product => product.toDict());
            return res.status(200).json(productDicts);
        } catch (e: any) {
            return res.status(400).json({ message: 'Error getting products', error: e.toString() });
        }
    });
}

export { getListProductsRouter, initializeEndpoints };
