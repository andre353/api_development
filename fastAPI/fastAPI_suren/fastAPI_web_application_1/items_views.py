from typing import Annotated

from fastapi import APIRouter, Path

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/")
def list_items():
    return [
        "Item1",
        "Item2",
    ]


# 1) order is important
@router.get("/latest/")
def get_latest_item():
    return {"items": {"id": "0", "name": "latest"}}


# 2) order is important
@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item": {
            "id": item_id,
        }
    }
