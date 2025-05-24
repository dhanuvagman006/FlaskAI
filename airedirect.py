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