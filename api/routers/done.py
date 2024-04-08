from fastapi import APIRouter

router = APIRouter()


@router.put("/task/{task_id}/done", response_model=None)
async def mark_task_as_done(task_id: int):
    return


@router.delete("/task/{task_id}/done", response_model=None)
async def unmark_task_as_done(task_id: int):
    pass
