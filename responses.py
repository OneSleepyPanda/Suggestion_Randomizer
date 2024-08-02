from random import choice, randint
import suggestions



def regen_prompts(prompts):
    prompt_list = prompts
    with open('suggestions.py', 'w') as f:
        f.write("prompt_list = [\n")
        for item in prompt_list:
            f.write(f'    "{item}",\n')
        f.write("]\n")
        print('Prompt list has been regenerated')
        return

def get_response(user_input: str) -> str:
        lowered: str = user_input.lower()
        trimmed: str = lowered.split(' ', 1)
        trigger: str = trimmed[0]
        user_prompt: str = trimmed[-1]
        prompt_list = suggestions.prompt_list
        
        print(trigger)
        if trimmed == '':
            return 'Well, you\'re awfully silent...'
        elif trigger == '!get-prompt':
            print('getting prompt')
            chosen_prompt = choice(prompt_list)
            print(chosen_prompt)
            prompt_list.remove(chosen_prompt)
            regen_prompts(prompt_list)
            return f'The art prompt of the day is: {chosen_prompt}'
        else:
            print(f'adding {user_prompt} to prompt list')
            prompt_list.append(user_prompt)
            print(prompt_list)
            regen_prompts(prompt_list)
            return f'Your Suggestion Has Been Added!'