from fastapi import FastAPI
from typing import Dict

app = FastAPI()


@app.post("/events/")
async def receive_event(event: Dict):
    if event["event_type"] == "game_start":
        # Handle game start logic
        return {"message": "Game started", "player_id": event["player_id"]}

    elif event["event_type"] == "game_end":
        # Handle game end logic
        return {"message": "Game ended", "player_id": event["player_id"], "final_score": event.get("final_score", 0)}

    elif event["event_type"] == "player_score_update":
        # Handle player score update logic
        return {"message": "Player score updated", "player_id": event["player_id"], "new_score": event["score"]}

    else:
        return {"message": "Unknown event type"}
