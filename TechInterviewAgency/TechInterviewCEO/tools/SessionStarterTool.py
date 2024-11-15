from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List
from datetime import datetime
import os
import json



class SessionStarterTool(BaseTool):
    """
    Tool create a new session instance for a candidate.
    """
    
    def run(self):
        """
        Creates a json file with session id.
        """
        session_id = f"sesh_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        session_data = {
            "session_id": session_id,
            "responses": []
        }
        sessions_dir = os.path.join(os.path.dirname(__file__), '../../Sessions')
        session_file_path = os.path.join(sessions_dir, f"{session_id}.json")
        # Create Sessions directory if it doesn't exist
        os.makedirs(sessions_dir, exist_ok=True)
        with open(session_file_path, "w") as file:
            json.dump(session_data, file, indent=4)
        
        return f"Session instance created with id: {session_id}"