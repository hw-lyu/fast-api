from fastapi import APIRouter

router = APIRouter()


@router.get("/task")
async def list_tasks():
    pass  # pass는 아무것도 하지 않는 문장


@router.post("/tasks")
async def create_task():
    pass


@router.put("/tasks")
async def update_task():
    pass


@router.delete("/tasks")
async def delete_task():
    pass
