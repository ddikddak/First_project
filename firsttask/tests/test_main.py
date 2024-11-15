import unittest
from unittest.mock import patch, MagicMock
import sys
import os
from dotenv import load_dotenv
load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from TechInterviewAgency.agency import agency

def test():
    # Add log file setup
    log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tests.log')
    with open(log_file_path, 'w') as f:  # 'w' mode to start fresh each test
        f.write("=== New Test Session ===\n\n")

    #workflow testing
    '''
    We do three tests on workflow. 
     - First we test that all stages are executed (which means that the workflow is working).
     - Second we test that a sesh file is created and that it is valid. This means SessionStarterTool is working.
     - Third we test that number of completions in each stage makes sense.
     - Fourth we test that session file has the amount of answers as the number of completions is stages 1 and 2.
     - Fifth we test that sum of scores in session file is not greater than the number of completions in 
       stages 1 and 2 multiplied by 1.75, as most of the responses should have a score of 1. With it we test that 
       the scoring mechanism is working. (At least when answer is wrong and for specific answers.)

    Note: for tests fourth and fifth will be considered stage 2 completions /2 as only one answer must be saved for each 2 completions.
     
    '''
    succes = [False, False, False, False, False]

    # We check how many session files are in the sessions directory
    # Get the path to the sessions directory relative to this test file
    sessions_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'TechInterviewAgency', 'Sessions')
    # Count number of files in sessions directory
    num_session_files = len([f for f in os.listdir(sessions_dir) if os.path.isfile(os.path.join(sessions_dir, f))])


    #workflow variables
    generations = 0
    stage = 0 #stage id
    number_of_completions = [0,0,0,0] #number of completions in each stage
    '''
    depending on stage we will input a different sequence
    stage 0: introduction
    stage 1: technical questions
    stage 2: scenario-based questions
    stage 3: end
    '''
    answers = {
                0: ["Hello, I am here for an interview.", "Yes, I am ready."],
                1: ["I don't know the answer.", "That is an openai api call.", "Here a dockerfile is created.", "Here a pandas dataframe can be used to store data."],
                2: ["Uh, I guess I'd just throw some AI models together and hope they work well? Like, maybe have one do language stuff and another handle images or something. I wouldn't worry too much about compatibility or how they communicate; they'll figure it out, right? Maybe just stick an API or two in there, and that should be fine.", "Oh, I'd probably just, you know, hope they get along. Maybe stick some middleware in there, like a Python script or something, and call it a day. Tools? Uh, I think TensorFlow or PyTorch or whatever's popular right now might do the trick. If something breaks, I'd just Google the error. Integration? Eh, let's wing it!"],
                3: ["Goodbye."]
            }
    index = 0 #index of the answer in the list

    #starts the workflow loop
    while generations < 20:
        number_of_completions[stage] += 1
        generations += 1
        print(f'stage = {stage}, index = {index}')
        
        # Log candidate's answer
        with open(log_file_path, 'a') as f:
            f.write(f"CANDIDATE: {answers[stage][index]}\n\n")
        
        try:
            output = agency.get_completion(answers[stage][index])
        except:
            return ([False, False, False, False, False], 'get completion failed')
        
        # Log agency's response
        with open(log_file_path, 'a') as f:
            # Split long messages at 80 characters
            formatted_output = '\n'.join([output[i:i+80] for i in range(0, len(output), 80)])
            f.write(f"AGENCY: {formatted_output}\n\n")
        
        output = output.lower()
        # Check for stage transitions based on keywords
        if (('api' in output and 'python' in output) and stage == 0) or ('scenario-based' in output and stage == 1):
            print('change of stage')
            stage += 1
            index = 0
        elif 'soon' in output and ('contact' in output or 'touch' in output) and stage == 2:
            print('change of stage') 
            stage = 3
            succes[0] = True #first test succesful
            break
        else:
            index = (index + 1) % len(answers[stage])

    # TEST 2: Check if a session file is created
    sessions_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'TechInterviewAgency', 'Sessions')
    # Count number of files in sessions directory
    new_num_session_files = len([f for f in os.listdir(sessions_dir) if os.path.isfile(os.path.join(sessions_dir, f))])
    if new_num_session_files == (num_session_files + 1):
        succes[1] = True #second test succesful

    print(number_of_completions)
    # TEST 3: Check if number of completions matches expected reference values
    reference_completions = [2, 7, 3, 1] # Expected number of completions for each stage
    absolute_differences = [1.1, 2.1, 1.1, 1.1] # Track differences per stage

    # Check if the number of completions for each stage is within the acceptable threshold
    diff = [abs(number_of_completions[i] - reference_completions[i])<=absolute_differences[i] for i in range(len(reference_completions))]
    
    # If all stage differences are within acceptable threshold (0), set success
    if all(diff):
        succes[2] = True

    # TEST 4: Check number of answers in last session file
    session_files = [f for f in os.listdir(sessions_dir) if os.path.isfile(os.path.join(sessions_dir, f))]
    session_files.sort(key=lambda x: os.path.getmtime(os.path.join(sessions_dir, x)))
    
    if session_files:
        latest_session = os.path.join(sessions_dir, session_files[-1])
        with open(latest_session, 'r') as f:
            import json
            session_data = json.load(f)
            num_answers = len(session_data['responses'])
            if abs(num_answers - (number_of_completions[1] + number_of_completions[2]//2)) <= 2:#added 2 as absolute difference.
                succes[3] = True

             # TEST 5: Check if sum of scores in session file is not greater than the number of completions in stages 1 and 2 multiplied by 1.75
            score = 0
            responses = session_data['responses']
            for response in responses:
                score += int(response['score'])
            if score <= (number_of_completions[1] + number_of_completions[2]//2) * 1.75:
                succes[4] = True

    return (succes, '')


if __name__ == '__main__':
    result, message = test()
    print(f'succes = {sum(result)}, errors = {5 - sum(result)}')
    print(result, message)
    