from uuid import UUID
from app.utils.exceptions import IdNotFoundException, NameNotFoundException
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi_pagination import Params
from app import crud
from app.api import deps
from app.models.product_model import Product
from app.models.user_model import User
from app.schemas.common_schema import IOrderEnum
from app.schemas.product_schema import (
    IProductCreate,
    IProductRead,
    IProductUpdate,
)
from app.schemas.response_schema import (
    IDeleteResponseBase,
    IGetResponseBase,
    IGetResponsePaginated,
    IPostResponseBase,
    IPutResponseBase,
    create_response,
)
from app.schemas.role_schema import IRoleEnum
from app.core.authz import is_authorized

router = APIRouter()

@router.get("")
async def get_product_list(
    params: Params = Depends()
) -> IGetResponsePaginated[IProductRead]:
    """
    Gets a paginated list of heroes
    """
    heroes = await crud.hero.get_multi_paginated(params=params)
    return create_response(data=heroes)