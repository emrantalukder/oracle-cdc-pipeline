import requests

# Schema Registry URL
schema_registry_url = 'http://localhost:8081'  # Update with your Schema Registry URL

# Function to get a list of all subjects
def get_all_subjects(url):
    response = requests.get(f"{url}/subjects")
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch subjects")
        return []

# Function to delete a subject (schema)
def delete_subject(url, subject):
    response = requests.delete(f"{url}/subjects/{subject}")
    if response.status_code in [200, 204]:
        print(f"Deleted subject: {subject}")
    else:
        print(f"Failed to delete subject: {subject}")

# Main execution
if __name__ == "__main__":
    subjects = get_all_subjects(schema_registry_url)
    for subject in subjects:
        delete_subject(schema_registry_url, subject)
