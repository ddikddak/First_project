from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List


class EvaluationTool(BaseTool):
    """
    Tool to evaluate the candidate's performance in the interview.
    """
    problem_solving: List[str] = Field(..., description="List of good and bad points of candidate's problem solving skills shown during the interview. Check info of problem solving criteria in knowledge base file.")
    problem_solving_level: str = Field(..., description="Level of problem solving skills shown by the candidate. Information of the levels in knowledge base file.")
    DSA: List[str] = Field(..., description="List of good and bad points of candidate's Data Structures and Algorithms knowledge shown during the interview. Check info of DSA criteria in knowledge base file.")
    DSA_level: str = Field(..., description="Level of Data Structures and Algorithms knowledge shown by the candidate. Information of the levels in knowledge base file.")
    project: List[str] = Field(..., description="List of good and bad points of candidate's project skills shown during the interview. Check info of project criteria in knowledge base file.")
    project_level: str = Field(..., description="Level of project skills shown by the candidate. Information of the levels in knowledge base file.")
    communication: List[str] = Field(..., description="List of good and bad points of candidate's communication skills shown during the interview. Check info of communication criteria in knowledge base file.")
    communication_level: str = Field(..., description="Level of communication skills shown by the candidate. Information of the levels in knowledge base file.")

    def run(self):
        """
        Returns the evaluation formatted according to the specified JSON schema.
        """
        evaluation_dict = {
            "problem_solving": self.problem_solving,
            "problem_solving_level": self.problem_solving_level,
            "DSA": self.DSA,
            "DSA_level": self.DSA_level,
            "project": self.project,
            "project_level": self.project_level,
            "communication": self.communication,
            "communication_level": self.communication_level,
        }
        return evaluation_dict

