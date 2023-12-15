from sqlmodel import Field, Relationship, SQLModel
from app.models.base_uuid_model import BaseUUIDModel
from uuid import UUID

class ProductBase(SQLModel):
    name: str = Field(index=True)
    price: float | None = Field(default=None)

class Product(BaseUUIDModel, ProductBase, table=True):
    created_by_id: UUID | None = Field(default=None, foreign_key="User.id")
    created_by: "User" = Relationship(  # noqa: F821
        sa_relationship_kwargs={
            "lazy": "joined",
            "primaryjoin": "Product.created_by_id==User.id",
        }
    )