import requests

def get_words_from_jotform():

    # api_key = Jotform API key
    # form_id = Your ID form
    api_key = 'ca3565b29686950eda90056b751fd38f'
    form_id = '241556017423047'

    url = f"https://eu-api.jotform.com/form/{form_id}/submissions?apiKey={api_key}"

    response = requests.get(url)
    data = response.json()

    # Safely get the content list, default to empty list if not found
    submissions = data.get('content',[])
    word_list = []
    
    for submission in submissions:
        answers = submission.get('answers', {})
        name_answer = answers.get('17', {}).get('answer', 'No name provided')
        if name_answer:
                word_list.append(name_answer)
        
    
    return word_list        


