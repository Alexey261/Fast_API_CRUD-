from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.backend.db import Base
from app.models import user
from sqlalchemy.schema import CreateTable

class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)
    user = relationship(argument='User', back_populates='tasks')

# print(CreateTable(Task.__table__))