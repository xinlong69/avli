from typing import Any

from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
def read_items() -> Any:
    """
    Retrieve items.
    """
    return True


@router.get("/{id}")
def read_item() -> Any:
    """
    Get item by ID.
    """
    return True


@router.post("/")
def create_item() -> Any:
    """
    Create new item.
    """
    return True
