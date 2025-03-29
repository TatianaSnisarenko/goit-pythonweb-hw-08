from functools import wraps
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status


def handle_db_exceptions(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except IntegrityError as e:
            if "duplicate key value" in str(e.orig):
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="A contact with this email already exists.",
                )
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"e.detail: {getattr(e, 'detail', "Database integrity error.")}",
            )

    return wrapper
