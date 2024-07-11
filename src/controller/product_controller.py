# import sys
# import os
# Adiciona o diretório base do projeto ao PYTHONPATH
# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../')

from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.repository.usuario_repository import ProductRepository
from src.config.dependencies import get_authenticated_user, get_product_service
from src.domain.dto.dtos import ProdutoCreateDTO, ProdutoUpdateDTO, ProdutoDTO
from src.service.auth_service import AuthService
from src.service.product_service import ProductService

product_router = APIRouter(prefix='/products', tags=['Products'], dependencies=[Depends(get_authenticated_user)])

# auth

auth_service = AuthService()

''' TO DO: utilizar as anotações adequadamente
 async def create(request: ProdutoCreateDTO, service: ProductService = Depends(get_product_service)):
    return service.create(request) '''

@product_router.post('/', status_code=201, description='Cria um novo Produto!', response_model=ProdutoDTO)
async def create (request: ProdutoCreateDTO, user_repo: ProductRepository = Depends(get_product_service), authorization: str = Depends(get_product_service)):
    # authorization: str = Header(alias='Authorization')
    # auth_service.validate_token(authorization)
    product_service = ProductService(user_repo),
    return product_service.create(request)

# TO DO: implementar método para buscar produto por ID
# async def find_by_id(user_id: int, service: ProductService = Depends(get_product_service)):
#     return service.find_by_id(user_id=user_id)

@product_router.get('/{user_id}', status_code=200, description='Buscar o Produto por id!', response_model=ProdutoDTO)
async def find_by_id(user_id: int, user_repo: ProductService = Depends(get_product_service), authorization: str = Depends(get_product_service)):
    # auth_service.validate_token(authorization)
    product_service = ProductService(user_repo)
    return product_service.find_by_id(user_id=user_id)

# TO DO: implementar método para buscar todos os produtos
# async def find_all(service: ProductService = Depends(get_product_service)):
#     return service.find_all()

@product_router.get('/', status_code=200, description='Buscar todos os Produtos!', response_model=list[ProdutoDTO])
async def find_all (user_repo: ProductRepository = Depends(get_product_service), authorization: str = Depends(get_product_service)):
    # auth_service.validate_token(authorization)
    product_service = ProductService(user_repo)
    return product_service.find_all()

# TO DO: implementar método para atualizar produto
# async def update(user_id: int, user_data: ProdutoUpdateDTO, service: ProductService = Depends(get_product_service)):
#     return service.update(user_id, user_data)

@product_router.put('/{user_id}', status_code=200, description='Atualizar um Produto!', response_model=ProdutoDTO)
async def update (user_id: int, user_data: ProdutoUpdateDTO, user_repo: ProductRepository = Depends(get_product_service), authorization: str = Depends(get_product_service)):
    # auth_service.validate_token(authorization)
    product_service = ProductService(user_repo)
    return product_service.update(user_id, user_data)

# TO DO: implementar método para deletar produto
# async def delete(user_id: int, service: ProductService = Depends(get_product_service)):
#     service.delete(user_id=user_id)

@product_router.delete('/{user_id}', status_code=204, description='Deletar o Produto por id!')
async def delete (user_id: int, user_repo: ProductRepository = Depends(get_product_service), authorization: str = Depends(get_product_service)):
    # auth_service.validate_token(authorization)
    product_service = ProductService(user_repo)
    product_service.delete(user_id=user_id)