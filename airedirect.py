import requests
import json
import difflib


def ask_ai(query, api_key, model, urls_disc):
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "nexusclubs.in",
                "X-Title": "Nexus Clubs",
            },
            data=json.dumps({
                "model": model,
                "messages": [
                    {
                        "role": "user",
                        "content": f"Based on this query: '{query}', which page should I redirect to? Here are the available pages and their descriptions: {urls_disc}. Just return the exact page name from the dictionary keys."
                    }
                ],
            })
        )
        
        if response.status_code == 200:
            result = response.json()['choices'][0]['message']['content'].strip().lower()
            # Check if the result matches any of our known pages
            if result in urls_disc:
                return result
            return 'not_found'
        else:
            error_msg = response.json().get('error', {}).get('message', 'Unknown error')
            print(f"Error: {error_msg}")
            return 'not_found'
            
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return 'not_found'

def ask_py(query, urls_disc):
    descriptions = list(urls_disc.values())
    match = difflib.get_close_matches(query, descriptions, n=1, cutoff=0.3)
    
    if match:
        for key, desc in urls_disc.items():
            if desc == match[0]:
                return key
    return "not_found"

# Example usage
# query = "how to reset my password"
# result = ask_py(query, urls_disc)
# print(result)
