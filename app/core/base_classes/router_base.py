from typing import Annotated, List, Type
from fastapi import APIRouter
from pydantic import UUID4, BaseModel
from app.auth.core.validator import BearerTokenDep
from app.core.base_classes.crud_base import CRUDBase
from app.db.base import SessionDep
from app.schemas.responses import DeleteRecordResponse

class RouterBase:
    def __init__(
        self,
        crud: CRUDBase,
        create_model: Type[BaseModel] = dict,
        read_model: Type[BaseModel] = dict,
        update_model: Type[BaseModel] = dict,
        filter_model: Type[BaseModel] = dict
    ):
        self.crud = crud
        self.create_model = create_model
        self.read_model = read_model
        self.update_model = update_model
        self.filter_model = filter_model or read_model

        self.router = APIRouter(
            prefix=f"/{crud.tag}",
            tags=[crud.tag]
        )

        self._setup_router()

    def _setup_router(self):

        @self.router.get("/{id}")
        async def get_by_id(
            id: UUID4,
            session: SessionDep,
            access_token: BearerTokenDep
        ) -> self.read_model: # type: ignore
            """
            Fetch a single record by its ID.
            """
            return self.crud.get(session=session, id=id)

        @self.router.post("")
        async def create_one(
            data: self.create_model,  # Fixed type annotation # type: ignore
            session: SessionDep,
            access_token: BearerTokenDep
        ) -> self.read_model: # type: ignore
            """
            Create a single record.
            """

            return self.crud.create(session=session, obj_in=data.model_dump())

        @self.router.delete("/{id}", response_model=DeleteRecordResponse)
        async def delete_by_id(
            id: UUID4,
            session: SessionDep,
            access_token: BearerTokenDep
        ) -> self.read_model: # type: ignore
            """
            Delete a single record by its ID.
            """
            return self.crud.delete(session=session, id=id)
        
        @self.router.get("")
        async def get_all(
            session: SessionDep,
            access_token: BearerTokenDep
        ) -> List[self.read_model]: # type: ignore
            
            """
            Get all records
            """

            return self.crud.get_all(session=session)

        @self.router.post("/filter")
        async def filter_by_params(
            data: self.filter_model, # type: ignore
            session: SessionDep,
            access_token: BearerTokenDep
        ) -> List[self.read_model]: # type: ignore
            
            records = self.crud.filter_by_params(session=session , **data.model_dump())

            return records
