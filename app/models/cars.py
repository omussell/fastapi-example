from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    driver_id = Column(Integer, ForeignKey("driver.id"))
    trip_id = Column(Integer, ForeignKey("trip.id"))

    driver = relationship("Driver", back_populates="cars")
    trip = relationship("Trip", back_populates="cars")
