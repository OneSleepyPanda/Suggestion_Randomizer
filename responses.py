from random import choice, randint
import suggestions
from better_profanity import profanity


# Recreates the prompt list with the updated content
def regen_prompts(prompts):
    prompt_list = prompts
    with open('suggestions.py', 'w') as f:
        f.write("prompt_list = [\n")
        for item in prompt_list:
            f.write(f'    "{item}",\n')
        f.write("]\n")
        print('Prompt list has been regenerated')
        return


#processes User Entries
def get_response(user_input: str) -> str:
        #Cleanup of user input
        lowered: str = user_input.lower()
        trimmed: str = lowered.split(' ', 1)
        trigger: str = trimmed[0]
        user_prompt: str = trimmed[-1]
        prompt_list = suggestions.prompt_list
        
        print(trigger)
        
        #processes input
        if trimmed == '':
            return 'Well, you\'re awfully silent...'
        
        #!get-prompt selects a random prompt from the list and removes it, if no prompts are stored generates one from chat gpt
        elif trigger == '!get-prompt':
            if prompt_list:
                print('getting prompt')
                print(len(prompt_list))
                chosen_prompt = choice(prompt_list)
                print(chosen_prompt)
                prompt_list.remove(chosen_prompt)
                regen_prompts(prompt_list)
                return f'The art prompt of the day is: {chosen_prompt}'
            else:
                return f'The prompt list is empty! Suggest some ideas you filthy animals!'
                
        
        #adds user provided prompt to the list
        else:
            print(f'checking prompt for profanity')
            if not profanity.contains_profanity(user_prompt):
                prompt_list.append(user_prompt)
                print(prompt_list)
                regen_prompts(prompt_list)
                return f'Your Suggestion Has Been Added!'
            else:
                return 'Your suggestion did not pass our profanity filter, clean up your language and try submitting it again!'