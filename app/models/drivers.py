from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    car_id = Column(Integer, ForeignKey("car.id"))

    cars = relationship("Car", back_populates="driver")
