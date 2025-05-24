import requests
import json

    
def ask_ai(query,api_key,model,urls_disc):
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "nexusclubs.in", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "Nexus Clubs", # Optional. Site title for rankings on openrouter.ai.
  },
  data=json.dumps({
    "model": model,
    "messages": [
      {
        "role": "user",
        "content": query+f"The following is the description of the pages and just return the page name: {urls_disc}"
      }
    ],
    
  })
)
    return response.json()['choices'][0]['message']['content']


def ask_py(query, urls_disc):
    descriptions = list(urls_disc.values())
    match = difflib.get_close_matches(query, descriptions, n=1, cutoff=0.3)
    
    if match:
        for key, desc in urls_disc.items():
            if desc == match[0]:
                return key
    return "not_found"

# Example usage
query = "how to reset my password"
result = ask_py(query, urls_disc)
print(result)
