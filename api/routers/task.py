from fastapi import APIRouter

import api.schemas.task as task_schema

router = APIRouter()


@router.get("/task", response_model=list[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="첫번쨰 Todo 작업")]


@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=1, **task_body.dict())
    # dict 인스턴스 앞에 **를 붙여 키워드 인수로 확장 TaskCreateResponse 클래스 생성자에 dict의 key/value를 전달한다
    #  **task_body.dick()는 (id=1, title=task_body.title, done=task_body.done)라고 작성하는 것과 동일하다.


@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=task_id, **task_body.dict())


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    return
