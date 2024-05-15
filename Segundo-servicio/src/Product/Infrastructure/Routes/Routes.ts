import { Router, Application } from 'express';
import { initializeEndpoints as initializeEndpointsCreateProduct } from '../Controllers/CreateProductController';
import { initializeEndpoints as initializeEndpointsListProduct } from '../Controllers/ListProductController';
import { initializeEndpoints as initializeEndpointsDeleteProduct } from '../Controllers/DeleteProductController';

const apiRouter = Router();

function initializeEndpoints(repository: any) {
    initializeEndpointsCreateProduct(repository);
    initializeEndpointsListProduct(repository);
    initializeEndpointsDeleteProduct(repository);
}

function initializeApp(app: Application, repository: any) {
    initializeEndpoints(repository);
    app.use('/api', apiRouter); // Puedes cambiar '/api' según tu preferencia
}

export { apiRouter, initializeApp };
