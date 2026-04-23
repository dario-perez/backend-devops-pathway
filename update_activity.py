import os
import requests

def fetch_activity():
    username = "dario-perez"
    url = f"https://api.github.com/users/{username}/events/public"
    response = requests.get(url)
    if response.status_code != 200:
        return "⚠️ No se pudo obtener la actividad reciente."
    
    events = response.json()
    activity_lines = []
    
    # Procesar los últimos 5 eventos de commit
    count = 0
    for event in events:
        if event["type"] == "PushEvent" and count < 5:
            repo_name = event["repo"]["name"]
            # Obtener el mensaje del último commit en ese push
            commit_msg = event["payload"]["commits"][-1]["message"].split('\n')[0]
            repo_url = f"https://github.com/{repo_name}"
            
            line = f"- 🚀 **{repo_name}**: {commit_msg} ([view]({repo_url}))"
            activity_lines.append(line)
            count += 1
            
    return "\n".join(activity_lines) if activity_lines else "No hay actividad reciente."

def update_readme(new_activity):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    start_tag = ""
    end_tag = ""
    
    start_idx = content.find(start_tag) + len(start_tag)
    end_idx = content.find(end_tag)

    if start_idx == -1 or end_idx == -1:
        print("Error: No se encontraron los comentarios ancla en el README.")
        return

    new_content = content[:start_idx] + "\n" + new_activity + "\n" + content[end_idx:]
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    activity = fetch_activity()
    update_readme(activity)