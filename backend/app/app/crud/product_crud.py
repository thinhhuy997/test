from app.schemas.product_schema import IProductCreate, IProductUpdate
from datetime import datetime
from app.crud.base_crud import CRUDBase
from app.models.product_model import Product
from sqlmodel import select, func, and_, col
from sqlmodel.ext.asyncio.session import AsyncSession


class CRUDProduct(CRUDBase[Product, IProductCreate, IProductUpdate]):
    async def get_Producte_by_name(
        self, *, name: str, db_session: AsyncSession | None = None
    ) -> Product:
        db_session = db_session or super().get_db().session
        Producte = await db_session.execute(
            select(Product).where(col(Product.name).ilike(f"%{name}%"))
        )
        return Producte.scalars().all()

    async def get_count_of_Productes(
        self,
        *,
        start_time: datetime,
        end_time: datetime,
        db_session: AsyncSession | None = None,
    ) -> int:
        db_session = db_session or super().get_db().session
        subquery = (
            select(Product)
            .where(
                and_(
                    Product.created_at > start_time,
                    Product.created_at < end_time,
                )
            )
            .subquery()
        )
        query = select(func.count()).select_from(subquery)
        count = await db_session.execute(query)
        value = count.scalar_one_or_none()
        return value


Product = CRUDProduct(Product)
