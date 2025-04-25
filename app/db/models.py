import uuid
from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    Enum,
    Float,
    String, 
    ForeignKey,
    DateTime,
    Table,
    UniqueConstraint,
    )
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector

from app.db.base import Base


class BaseTable():

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime , default=datetime.now , nullable=False)
    updated_at = Column(DateTime , default=datetime.now , nullable=False)
    deleted = Column(Boolean , default=False , nullable=False)

class UserImage(BaseTable , Base):

    __tablename__ = 'user_image' 

    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id') , nullable=False)
    image_id = Column(UUID(as_uuid=True), ForeignKey('image.id'), nullable=False)

class Image(BaseTable , Base):

    __tablename__ = 'image'

    object_key = Column(String , nullable=False)
    bucket_name = Column(String , nullable=False)
    is_cover = Column(Boolean , nullable=True)

    # Scoring system
    highlight_score = Column(Float , default=0.0 , nullable=True)
    
    __table_args__ = (
        UniqueConstraint("object_key" , name="uq_image_object_key"),
    )

    users = relationship("User", secondary='user_image', back_populates="images" , lazy='joined')
    events = relationship("Event", secondary='event_image', back_populates="images" , lazy='joined')


class User(BaseTable , Base):

    __tablename__ = 'user'

    full_name = Column(String(100) , nullable=True)
    phone_number = Column(String(20) , nullable=True)
    face_identification_info = Column(Vector(128))

    images = relationship("Image", secondary='user_image', back_populates="users" , lazy='joined')
    events = relationship("Event", secondary="user_event", back_populates="users" , lazy='joined' , overlaps="events,users")

class Event(BaseTable , Base):

    __tablename__ = 'event'

    name = Column(String(100), nullable=False)
    client_id = Column(UUID(as_uuid=True), ForeignKey('client.id') , nullable=False)
    sub_title = Column(String , nullable=True)
    description = Column(String , nullable=True)
    location = Column(String , nullable=True)
    
    __table_args__ = (
        UniqueConstraint("name", "client_id", name="uq_event_name_client"),
    )

    images = relationship("Image", secondary='event_image', back_populates="events" , lazy='joined')
    users = relationship("User", secondary="user_event", back_populates="events" , lazy='joined' , overlaps="events,users")


class UserEvent(BaseTable, Base):

    __tablename__ = 'user_event'

    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id') , nullable=False)
    event_id = Column(UUID(as_uuid=True), ForeignKey('event.id'), nullable=False)


    user = relationship("User", backref="user_event_associations" , overlaps="events,users")
    event = relationship("Event", backref="user_event_associations" , overlaps="events,users")

    __table_args__ = (UniqueConstraint("user_id", "event_id", name="uq_user_event"),)

class EventImage(BaseTable , Base):

    __tablename__ = 'event_image'

    event_id = Column(UUID(as_uuid=True), ForeignKey('event.id') , nullable=False)
    image_id = Column(UUID(as_uuid=True), ForeignKey('image.id'), nullable=False)


class Client(BaseTable , Base):

    __tablename__ = 'client'

    username = Column(String , nullable=False)
    auth_provider_id = Column(UUID(as_uuid=True) , nullable=False, unique=True)

    events = relationship("Event" , lazy='joined')


