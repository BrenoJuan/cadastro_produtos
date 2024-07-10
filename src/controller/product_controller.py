from fastapi import APIRouter, Depends

from src.config.dependencies import get_authenticated_user, get_product_service
from src.domain.dto.dtos import ProdutoCreateDTO, ProdutoUpdateDTO
from src.service.product_service import ProductService

product_router = APIRouter(prefix='/products', tags=['Products'], dependencies=[Depends(get_authenticated_user)])


# TODO: utilizar as anotações adequadamente
async def create(request: ProdutoCreateDTO, service: ProductService = Depends(get_product_service)):
    return service.create(request)


# TODO: implementar método para buscar produto por ID
async def find_by_id(user_id: int, service: ProductService = Depends(get_product_service)):
    return service.find_by_id(user_id=user_id)


# TODO: implementar método para buscar todos os produtos
async def find_all(service: ProductService = Depends(get_product_service)):
    return service.find_all()


# TODO: implementar método para atualizar produto
async def update(user_id: int, user_data: ProdutoUpdateDTO, service: ProductService = Depends(get_product_service)):
    return service.update(user_id, user_data)


# TODO: implementar método para deletar produto
async def delete(user_id: int, service: ProductService = Depends(get_product_service)):
    service.delete(user_id=user_id)
