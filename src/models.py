from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class Users(db.Model):
    __tablename__="users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    lastname: Mapped[str]= mapped_column(String(50), nullable=False)

    profile: Mapped["Profiles"] = relationship(back_populates="user", uselist=False)
    
    
    favorites: Mapped[list["Favorites"]] = relationship(back_populates="user")

       
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "lastname": self.lastname,
            "profile": self.profile.serialize() if self.profile else None, #por que no es self.profile.serialize()
            "favorites": [favorite.serialize() for favorite in self.favorites]
        }

class Profiles(db.Model):
    __tablename__="profiles"
    id: Mapped[int]= mapped_column(primary_key=True)
    bio: Mapped[str]= mapped_column(String(2000), nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["Users"] = relationship(back_populates="profile")

    
    def serialize(self):
        return{
            "id": self.id,
            "bio": self.bio,
            "user": self.user, #aqui no estoy segura de que tengo que poner, si lleva serialize o no
            "favorites": [favorite.serialize() for favorite in self.favorites]
        }

class People(db.Model):
    __tablename__= "people"
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str]  = mapped_column(String(100), nullable=False)
    birth_year: Mapped[str] = mapped_column(String(50), nullable=False)
    gender: Mapped[str] = mapped_column(String(50), nullable=False)
    hair_color: Mapped[str] = mapped_column(String(50), nullable=False)
    height:Mapped[int] = mapped_column(nullable=False)
    films: Mapped[str]  = mapped_column(String(10000), nullable=False)
    vehicles: Mapped[str] = mapped_column(String(50), nullable=False)

    favorites: Mapped[list["Favorites"]] = relationship(back_populates="people")

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "vehicles": self.vehicles,
            "favorites": [favorite.serialize() for favorite in self.favorites]
        }

class Planets(db.Model):
    __tablename__= "planets"
    id: Mapped[int] = mapped_column(primary_key=True)
    climate: Mapped[str] = mapped_column(String(50), nullable=False)
    diameter: Mapped[int] = mapped_column(nullable=False)
    films: Mapped[str] = mapped_column(String(50000), nullable=False)
    gravity: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    population: Mapped[int] = mapped_column(nullable=False)

    favorites: Mapped[list["Favorites"]] = relationship(back_populates="planets")

    def serialize(self):
        return{
            "id": self.id,
            "climate": self.climate,
            "diameter": self.diameter,
            "films": self.films,
            "gravity": self.gravity,
            "name": self.name,
            "population": self.population, 
            "favorites": [favorite.serialize() for favorite in self.favorites]

        }
    
class Favorites(db.Model):
    __tablename__= "favorites"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    people_id: Mapped[int] = mapped_column(ForeignKey("people.id"), primary_key=True)
    planets_id: Mapped[int] = mapped_column(ForeignKey("planets.id"), primary_key=True)

    user: Mapped["Users"] = relationship(back_populates="favorites")
    people: Mapped["People"] = relationship(back_populates="favorites")
    planets: Mapped["Planets"] = relationship(back_populates="favorites")

