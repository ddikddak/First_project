from agency_swarm import Agency
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from TechInterviewAgency.TechInterviewCEO import TechInterviewCEO

ceo = TechInterviewCEO()

from dotenv import load_dotenv
load_dotenv()


agency = Agency([
    ceo,   
    ],
    shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
    max_prompt_tokens=25000,  # default tokens in conversation for all agents
    temperature=0.3,  # default temperature for all agents
    )


print("Starting agency...")
if __name__ == '__main__':
    print("Starting agency...")
    agency.demo_gradio()