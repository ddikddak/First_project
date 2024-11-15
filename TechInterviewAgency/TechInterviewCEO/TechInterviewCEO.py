from agency_swarm.agents import Agent
from agency_swarm.tools.oai import FileSearch
from .tools.TechQuestionsTool import TechQuestionsTool
from .tools.ResponseSaverTool import ResponseSaverTool
from .tools.SessionStarterTool import SessionStarterTool
from .tools.ScenarioQuestionsTool import ScenarioQuestionsTool



class TechInterviewCEO(Agent):
    def __init__(self):
        super().__init__(
            name="TechInterviewCEO",
            description="The TechInterviewCEO is responsible for guiding the interview process within the TechInterviewAgency.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[FileSearch, TechQuestionsTool, ResponseSaverTool, SessionStarterTool, ScenarioQuestionsTool],
            #tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
            parallel_tool_calls=True,
        )
        
    def response_validator(self, message):
        return message
