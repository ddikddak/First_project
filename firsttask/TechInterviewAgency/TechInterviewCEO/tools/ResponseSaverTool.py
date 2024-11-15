from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List
import json
import os


class ResponseSaverTool(BaseTool):
    """
    Tool to save a candidate's response and its evaluation score to a JSON file.
    Each session is identified by a unique timestamp-based session ID.
    """

    session_id: str = Field(..., description="Session ID of the candidate. Given by SessionStarterTool tool.")
    candidate_performance: str = Field(..., description="Considering the correct_answer, evaluate the candidate's answer. Make shure correct_answer guide is followed.")
    performance_crieteria: List[str] = Field(..., description="Different levels for each crieria considering candidate's crieria bases in knowledge base file.")
    question: str = Field(..., description="Question asked to the candidate.")
    response: str = Field(..., description="Response of the candidate.")
    score: int = Field(..., description="Score of the candidate's evaluation, based on candidate_performance and performance_criteria.")
    
    def run(self):
        """
        Saves the candidate's response and evaluation score in a JSON file identified by session ID.
        """
        # Generate a unique session ID based on the current timestamp
        # Check if session file exists
        session_file_path = os.path.join(os.path.dirname(__file__), '../../Sessions', f"{self.session_id}.json")
        if not os.path.exists(session_file_path):
            return f"Session file not found for session ID: {self.session_id}, make sure SessionStarterSool has been properly executed or the session id is the correct one."
        
        # Read existing session data
        with open(session_file_path, "r") as file:
            session_data = json.load(file)
        
        # Prepare response data to be saved
        response_data = {
            "question": self.question,
            "response": self.response,
            "score": self.score
        }

        #Add response data to session data
        session_data["responses"].append(response_data)
        
        # Write data to a JSON file
        with open(session_file_path, "w") as file:
            json.dump(session_data, file, indent=4)
        
        return 'Answer saved.'

