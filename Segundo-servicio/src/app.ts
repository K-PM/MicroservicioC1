import express, { Application } from 'express';
import { initializeApp } from './Product/Infrastructure/Routes/Routes';
import { Repository as RepositoryProduct } from './Product/Infrastructure/Repositories/MysqlRepository';

const app: Application = express();
const repositoryProduct: RepositoryProduct = new RepositoryProduct();

initializeApp(app, repositoryProduct);

const PORT: number = 3001;

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
