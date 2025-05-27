import asyncio
from google.adk.sessions import VertexAiSessionService
from vertexai import agent_engines

project_id = "hackathon-overlords"
location = "us-central1"
resource_id = "projects/499014060451/locations/us-central1/reasoningEngines/2764691201717174272"


def create_session():
    session_service = VertexAiSessionService(project_id, location)
    session = asyncio.run(session_service.create_session(
            app_name=resource_id,
            user_id="traveler0115"
        )
    )
    return session


def get_agent():
    return agent_engines.get(resource_id)


def send_message(agent, session_id: str, message: str) -> None:
    
    for event in agent.stream_query(
        user_id="traveler0115",
        session_id=session_id,
        message=message,
    ):
        for part in event.get("content",{}).get("parts",[]):
            p = part.get("text")
            if p:
                print(p)


def main() -> None:
    session = create_session()
    message = "Find me an apartment in Paris in June 5th for 3 days"
    send_message(session.id, message)



if __name__ == "__main__":
    main()
