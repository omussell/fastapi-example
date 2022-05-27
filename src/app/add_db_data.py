from typing import Optional

from sqlmodel import Session
from db.base import engine
from db.models import Plant


def create_plants():
    plant_1 = Plant(name="Hebe")
    plant_2 = Plant(name="Astilbe")
    plant_3 = Plant(name="Sedum")
    plant_4 = Plant(name="Helenium")
    plant_5 = Plant(name="Heather")

    session = Session(engine)

    session.add(plant_1)
    session.add(plant_2)
    session.add(plant_3)
    session.add(plant_4)
    session.add(plant_5)

    session.commit()

    session.close()


def main():
    create_plants()


if __name__ == "__main__":
    main()