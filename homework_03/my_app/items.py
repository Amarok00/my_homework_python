from fastapi import APIRouter

router = APIRouter(tags=["items"])  # prefix='/items',


@router.get("/")
def get_items():
    return {"data": [{"id": 123, "name": "abc"}, {"id": 456, "name": "def"}]}


@router.get("/{item_id}")
def get_item(item_id: int):
    return {"data": {"id": item_id, "name": f"Item {item_id}"}}


@router.post("/")
def create_item(data: dict):
    return {"data": data}
