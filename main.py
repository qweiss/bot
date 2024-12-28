from highrise import BaseBot, SessionMetadata

class MyBot(BaseBot): 
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot started")
        coordinates = {
        'x': 12,
        'y': 0.5,
        'z': 7,
