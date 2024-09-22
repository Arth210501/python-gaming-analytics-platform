from celery import Celery

celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)


@celery.task
def process_game_data(data):
    # Placeholder for game data processing
    return f"Processed data: {data}"
