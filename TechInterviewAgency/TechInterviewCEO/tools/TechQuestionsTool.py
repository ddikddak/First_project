from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List

class TechQuestionsTool(BaseTool):
    """
    Tool to generate technical questions formatted in a specific JSON schema.
    """
    topic_cover: str = Field(..., description="Which topic will be covered in the question and how it will be covered, must use knowledge base to develop the question.")
    new_coverage: str = Field(..., description="What information is covered that has not been covered in other questions. Need to be used to not repeat questions.")
    files_data: str = Field(..., description="The code snippets from knowledge base files that will be used to develop the question.")
    question: str = Field(..., description="The question. Must be a code snippet without comments, and the user must explain the general functionality of the code.")
    correct_answer: str = Field(..., description="The correct answer for the question, it must be a generic explain of the code functionality, line by line explanations are not accepted. Remark this on the answer.")
   

    def run(self):
        """
        Returns the question formatted according to the specified JSON schema.
        """
        # Create question dictionary following the specified schema
        question_dict = {
            "question": self.question,
            "correct_answer": self.correct_answer,
        }
        return question_dict


