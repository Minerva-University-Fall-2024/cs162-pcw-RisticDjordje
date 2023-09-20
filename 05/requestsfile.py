import requests

# Base URL for httpbin
BASE_URL = "https://httpbin.org/"

# Function to perform HTTP Basic Authentication
def basic_auth(username, password):
    auth = requests.auth.HTTPBasicAuth(username, password)
    url = f"{BASE_URL}basic-auth/{username}/{password}"
    response = requests.get(url, auth=auth)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

# Function to download an image
def download_image():
    response = requests.get(f"{BASE_URL}image/jpeg")
    print(f"Image Status Code: {response.status_code}")
    with open("downloaded_image.jpg", "wb") as file:
        file.write(response.content)
    print("Image downloaded successfully")

# Function to generate a UUID
def generate_uuid():
    url = f"{BASE_URL}uuid"
    response = requests.get(url)
    print(f"UUID Status Code: {response.status_code}")
    print(f"UUID: {response.text}")

# Function to get a JSON response
def json_response():
    url = f"{BASE_URL}json"
    response = requests.get(url)
    print(f"JSON Status Code: {response.status_code}")
    print(f"JSON Response: {response.text}")

# Function to get dog breeds in JSON format from a public API
def get_dog_breeds():
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)
    print(f"Dog Breeds Status Code: {response.status_code}")
    print(f"Dog Breeds: {response.text}")

# Base URL for The Cat API
CAT_BASE_URL = "https://api.thecatapi.com/v1/"

# Function to get random cat images
def get_random_cat_image():
    url = f"{CAT_BASE_URL}images/search"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"Cat Image Data: {response.text}")

# Function to get a list of cat breeds
def get_cat_breeds():
    url = f"{CAT_BASE_URL}breeds"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}") 
    print(f"Cat Breeds Data: {response.text}")

# Main program
if __name__ == "__main__":
    basic_auth("djordje", "ristic")
    download_image()
    generate_uuid()
    json_response()
    get_dog_breeds()
    get_random_cat_image()
    get_cat_breeds()
