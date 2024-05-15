export class ListProductUseCase {
    private repository: any;

    constructor(repository: any) {
        this.repository = repository;
    }

    async execute(): Promise<any[]> {
        return this.repository.list_all();
    }
}
