from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List



class ScenarioQuestionsTool(BaseTool):
    """
    Tool to generate scenario-based questions formatted in a specific JSON schema.
    """
    topic_cover: str = Field(..., description="How candidate problem solving will be assessed.")
    new_coverage: str = Field(..., description="What information is covered that has not been covered in other questions. Need to be used to not repeat questions.")
    files_data: str = Field(..., description="The data from knowledge base files that will be used to develop the question.")
    question: str = Field(..., description="Question must be open-ended, based on knowledge base files, and must test problem solving skills. Examples care given a code snippet improve it, or for a specific agency scenario, which tools would you use or which agents.")
    discussion_questions: List[str] = Field(..., description="List of questions to discuss the solution with the candidate. They aim to understand how the candidate thinks and solve problems.")
   

    def run(self):
        """
        Returns the question formatted according to the specified JSON schema.
        """
        # Create question dictionary following the specified schema
        question_dict = {
            "question": self.question,
            "discussion_questions": self.discussion_questions,
        }
        return question_dict


