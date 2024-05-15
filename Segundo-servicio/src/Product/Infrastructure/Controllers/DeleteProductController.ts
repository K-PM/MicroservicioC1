import { Request, Response, Router } from 'express';
import { DeleteProductUseCase } from '../../Application/DeleteProductUseCase';

const deleteProductRouter = Router();

function initializeEndpoints(repository: any) {
    const deleteProductUseCase = new DeleteProductUseCase(repository);

    deleteProductRouter.delete('/delete:id', async (req: Request, res: Response) => {
        try {
            const id: string = req.params.id;
            await deleteProductUseCase.execute(id);
            return res.status(200).json({ message: 'Product deleted' });
        } catch (e: any) {
            return res.status(400).json({ message: 'Error deleting Product', error: e.toString() });
        }
    });
}

export { deleteProductRouter, initializeEndpoints };

