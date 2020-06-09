from fastapi import APIRouter, BackgroundTasks
from time import sleep

router = APIRouter()

# can be async def or normal def function
def write_notification(email: str, message=""):
    # lets pretend this is sending an email...
    sleep(5)
    # print in the uvicorn log
    print(f"notification for {email}: {message}")


@router.post("/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}
