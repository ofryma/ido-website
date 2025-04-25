from sqlalchemy.orm import sessionmaker
from app.db.base import engine
from app.db.models import UserImage


Session = sessionmaker(bind=engine)

class UserImageCrud():
    def create(self, obj_in: dict) -> UserImage:
        session = Session()
        user_image = UserImage(**obj_in)
        session.add(user_image)
        session.commit()
        session.close()
        return user_image

    def get(self, id) -> UserImage:
        session = Session()
        user_image = session.query(UserImage).filter_by(id=id).first()
        session.close()
        return user_image

    def update(self, id, obj: dict) -> UserImage:
        session = Session()
        user_image = session.query(UserImage).filter_by(id=id).first()
        if user_image:
            for key, value in obj.items():
                setattr(user_image, key, value)
            session.commit()
        session.close()
        return user_image

    def delete(self, id):
        session = Session()
        user_image = session.query(UserImage).filter_by(id=id).first()
        if user_image:
            session.delete(user_image)
            session.commit()
        session.close()
