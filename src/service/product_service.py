import logging
from fastapi import HTTPException
from pydantic import TypeAdapter
from sqlalchemy.exc import IntegrityError

from src.domain.dto.dtos import ProdutoCreateDTO, ProdutoDTO, ProdutoUpdateDTO
from src.repository.usuario_repository import ProductRepository
from src.domain.model.models import Product

logger = logging.getLogger('fastapi')

class ProductService:

    def __init__(self, usuario_repository: ProductRepository):
        self.usuario_repository = usuario_repository

    def create(self, user_data: ProdutoCreateDTO) -> ProdutoDTO:
        logger.info('Criando um novo Produto!')
        user = Product(**user_data.model_dump())
        try:
            created = self.usuario_repository.save(user)
            return TypeAdapter(ProdutoDTO).validate_python(created)
        except IntegrityError as e:
            logger.error(f'Erro ao criar o Produto: {user_data.model_dump()}')
            raise HTTPException(status_code=409, detail=f'Produto já existe na base: {e.args[0]}')

    def read(self, user_id: int) -> ProdutoDTO:
        logger.info('Buscando um Produto!')
        return TypeAdapter(ProdutoDTO).validate_python(self._read(user_id))

    def _read(self, user_id: int) -> Product:
        user = self.usuario_repository.read(user_id)
        if user is None:
            self.logger.error(f'Produto {user_id} não encontrado!')
            raise HTTPException(status_code=404, detail=f'Produto {user_id} não encontrado!')
        return user

    def find_all(self) -> list[ProdutoDTO]:
        logger.info('Buscando todos os Produtos!')
        users = self.usuario_repository.find_all()
        return [TypeAdapter(ProdutoDTO).validate_python(user) for user in users]

    def update(self, user_id: int, user_data: ProdutoUpdateDTO):
        logger.info('Atualizando o Produto {user_id}!')
        user = self._read(user_id)
        user_data = user_data.model_dump(exclude_unset=True)
        for key, value in user_data.items():
            setattr(user, key, value)
        user_updated = self.usuario_repository.save(user)
        logger.info(f'Produto {user_id} atualizado: {user_updated}')
        return TypeAdapter(ProdutoDTO).validate_python(user_updated)

    def delete(self, user_id: int) -> int:
        user = self._read(user_id)
        self.usuario_repository.delete(user)
        logger.info(f'Produto {user_id} deletado!')
        return user_id