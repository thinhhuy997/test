from app.models.product_model import ProductBase
from app.utils.partial import optional
from uuid import UUID
from pydantic import field_validator

class IProductCreate(ProductBase):
    @field_validator('price')
    def check_price(cls, value):
        if value < 0:
            raise ValueError("invalid price")
        return value
    
# All these fields are optional
@optional()
class IProductUpdate(ProductBase):
    pass

class IProductRead(ProductBase):
    id: UUID

