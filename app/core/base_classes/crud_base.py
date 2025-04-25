import logging
from typing import List, Literal, Protocol
from fastapi import HTTPException , status
from pydantic import UUID4
from sqlalchemy.orm import Session , Query
from sqlalchemy.exc import IntegrityError , SQLAlchemyError

from app.schemas.responses import DeleteRecordResponse


class QueryFilter(Protocol):

    def __call__(self, query: Query , **kwargs) -> Query:
        ...


class CRUDBase():

    def __init__(self , model):
        self.model = model
        self.tag: str = model.__tablename__

    def create(self,session: Session,  obj_in: dict):

        try:
            record = self.model(**obj_in)
            session.add(record)
            session.commit()
            session.refresh(record)
            session.close()
            return record
        except IntegrityError as ie:
            session.rollback()
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail=f"record already exists; {ie}")
        except Exception as e:
            session.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail=f'{e}')

    def merge(self , session: Session , obj_in: dict):

        try:
            record = self.model(**obj_in)
            session.merge(record)
            session.commit()
            session.refresh(record)
            session.close()
            return record
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail=f'{e}')

    def get(self,session: Session ,id : UUID4):
        image = session.query(self.model).filter_by(id=id).first()
        session.close()
        return image
    
    def get_all(self, session: Session):

        return session.query(self.model).all()


    def update(self,session: Session, id: UUID4, obj: dict):

        try:
            record = self.get(session=session , id=id)
            if not record:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{self.tag.capitalize()} record with id {id} not found")

            # Update record in bulk
            session.query(self.model).filter_by(id=id).update(obj)
            session.commit()

            return self.get(session=session , id=id)

        except SQLAlchemyError as e:
            session.rollback()  # Ensure rollback on failure
            logging.error(f"Database error: {e}")
            raise HTTPException(status_code=500 , detail=f"Database error: {e}")

    def delete(self,session: Session, id: UUID4) -> DeleteRecordResponse:

        record = session.query(self.model).filter_by(id=id).first()
        if record:
            session.delete(record)
            session.commit()
        session.close()

        return DeleteRecordResponse(
            message=f"{self.tag.capitalize()} with id {id} deleted successfuly"
        )


    def filter_by_params(self, session: Session , queryCmd: Literal["all" , "first"] = "all" , filter_methods : List[QueryFilter] = [] , **kwargs):
        
        try:
            query = session.query(self.model)

            for filter_method in filter_methods:
                query = filter_method(query=query , **kwargs)
        except Exception as e:
            raise HTTPException(status_code=500 , detail={
                "message": f"Error: server failed in adding the filter methods; {self.tag} model;",
                "error": f"{e}" 
                }
                )

        try:
            for key , value in kwargs.items():
            
                try:
                    getattr(self.model, key)
                except:
                    continue

                if value is None: 
                    continue

                query = query.filter(getattr(self.model, key) == value)
        except Exception as e:
            raise HTTPException(status_code=500 , detail={
                "message": f"Error: server failed in adding field filter; {self.tag} model;",
                "error": f"{e}" 
                }
                )

        if queryCmd == "all":
            try:
                records = query.all()
            except Exception as e:
                raise HTTPException(status_code=500 , detail={
                "message": f"Error: server failed fetching all records; {self.tag} model;",
                "error": f"{e}" 
                }
                )
        else:
            try:
                records = query.first()
            except Exception as e:
                raise HTTPException(status_code=500 , detail={
                "message": f"Error: server failed fetching a single record; {self.tag} model;",
                "error": f"{e}" 
                }
                )

        return records



class CRUDBaseJunctionTable(CRUDBase):

    pass