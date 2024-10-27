import requests
import json

# Monday.com API setup
monday_api_token = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjQwNDkzNTI4OCwiYWFpIjoxMSwidWlkIjo2NTU0ODI2NSwiaWFkIjoiMjAyNC0wOS0wMlQxMTowMDoxNi42OTlaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MjUyMjg0NDIsInJnbiI6ImV1YzEifQ.QomC0V97whap4k1o7pWS4SGS1Ah1-xuGdI27KyU2-2M"
monday_headers = {
    'Authorization': monday_api_token,
    'Content-Type': 'application/json'
}

# Notion API setup

# -------- NOTION IS MORE CHILL, NO NEED TO TWEAK AS MANY PARAMETERS -----------------

notion_api_key = "secret_JDFy5P244tLfdfBNoedMPNTxIxx6A8veG6ro0zHwiVr"
notion_database_id = "9c0113de-0d6c-4876-9c8c-0564687ee797"  # Replace with your Notion database ID
headers = {
    "Authorization": f"Bearer {notion_api_key}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# ------ MAIN MONDAY PARAMETERS, TWEAK THESE FOR EACH NEW ACCOUNT ---------------

# Example usage to create a task in Monday.com
board_id = 1614669298  # Example board ID from the screenshot
group_id = "topics"  # Example group ID from the screenshot
item_name = "New Task Example"
status_label = "Working on it"  # Status label like 'Done', 'In Progress', etc.


# Function to fetch tasks from Monday.com
def fetch_monday_tasks():

     # Fetches tasks from monday.com
     #
     # args:
     #    none
     #
     # returns:
     #    returns the JSON data from the API response.

    query = """
    {
      boards (ids: 1614669298) {
        id
        name
        items_page (limit: 10) {
          items {
            id
            name
            column_values {
              id
              text
            }
          }
        }
      }
    }
    """
    response = requests.post('https://api.monday.com/v2/', json={'query': query}, headers=monday_headers)
    data = response.json()
    return data



# Function to fetch existing tasks from Notion
def fetch_existing_notion_tasks():

# Fetches existing notion taks
# args:
#     none
# returns:
#     If successful, the function returns a list of task names as strings (e.g., ["Task 1", "Task 2", "Task 3"]).
#     If the request fails, it returns an empty list [].


    url = f"https://api.notion.com/v1/databases/{notion_database_id}/query"
    
    response = requests.post(url, headers=headers, data=json.dumps({}))

# Check if the response was successful (status code 200 means OK)
    if response.status_code == 200:
        data = response.json()
        tasks = data.get('results', [])

        # This loops through the tasks and retrieves the 'Task name' from the 'properties' field.
        return [task['properties']['Task name']['title'][0]['plain_text'] for task in tasks if 'Task name' in task['properties']]
    else:
        # If the response was unsuccessful, an empty list is returned.
        print(f"Failed to fetch existing tasks from Notion. Status code: {response.status_code}")
        print(response.json())
        return []

# Function to fetch and return all users from Notion



def fetch_notion_users():


# Fetches the list of users from the Notion workspace using the Notion API.

# args:
#     none

# returns:
#     A list of dictionaries where each dictionary represents a user
#     with their 'name', 'email', and 'id'. If the request fails, an
#     empty list is returned.

    url = "https://api.notion.com/v1/users"
    
    response = requests.get(url, headers=headers)

# Check if the response was successful (status code 200 means OK)
    if response.status_code == 200:
        users = response.json().get('results', [])
        notion_users = []

        # Loop through each user in the list of users
        for user in users:
            # Create a dictionary for each user with their 'name', 'email', and 'id'
            # If any of these fields is missing, 'N/A' will be used as a fallback
            notion_user = {
                'name': user.get('name', 'N/A'),
                'email': user.get('person', {}).get('email', 'N/A'),
                'id': user.get('id', 'N/A')
            }

            # Adds the user information to the notion_users list, and returns the list.
            notion_users.append(notion_user)
        return notion_users
    else:
        print(f"Failed to fetch users from Notion. Status code: {response.status_code}")
        print(response.json())

        # Return an empty list in case response was unsuccessful.
        return []




# Function to fetch detailed user information from Monday.com
def fetch_monday_users():

# Fetches a list of users from the Monday.com workspace using the Monday API
# args:
#     none
# returns:
#     A list of users, where each user is a dictionary containing their 'id', 'name', and 'email'.
#     If the request fails, an empty list is returned.


# GraphQL query to fetch the users' id, name, and email from Monday.com
    query = """
    {
      users {
        id
        name
        email
      }
    }
    """
    response = requests.post('https://api.monday.com/v2/', json={'query': query}, headers=monday_headers)


# Check if the response was successful (status code 200 means OK)
    if response.status_code == 200:
        data = response.json()

        # Retrieve the 'users' list from the 'data' field in the response
        return data.get('data', {}).get('users', [])
    else:
        print(f"Failed to fetch users from Monday.com. Status code: {response.status_code}")
        print(response.json())
        # Returns an empty list if the response was unsuccessful
        return []

# Function to map Monday.com person to Notion person
def map_monday_to_notion_person(monday_person_name):
#     Maps a user from Monday.com to a corresponding user in Notion based on email or name.
#
#     Args:
#     monday_person_name(str), name of user from monday.com

#     Returns:
#     the matching Notion user as a dictionary if found, or None if no match is found.


    notion_users = fetch_notion_users()
    monday_users = fetch_monday_users()

    #Matching users based on their emails
    for monday_user in monday_users:
        # checking if the monday username provided exists in the monday users list.
        if monday_user['name'] == monday_person_name:
            monday_user_email = monday_user.get('email')
            for notion_user in notion_users:
                # matching emails of notion users with the email of the monday.com user provided
                if notion_user.get('email') == monday_user_email:
                    # returning the notion user if emails matched
                    return notion_user
    
    # match by same name if emails are not available or don't match
    for notion_user in notion_users:
        if notion_user.get('name', '').lower() == monday_person_name.lower():
            return notion_user

    # in case no user found in notion with the same name or email
    print(f"No matching user found for {monday_person_name}")
    return None



# Function to create a new task in Notion
def create_notion_task(task_name, status, assigned_to_id, date=None):


#  Creates a new task in a Notion database using the Notion API.
#
#     args:
#     - task_name (str): The name of the task to be created.
#     - status (str): The status of the task.
#     - assigned_to_id (str): The ID of the user to whom the task is assigned.
#     - date (str, optional): The date for the task. Defaults to None if not provided.
#
#     Returns:
#     - None: The function prints the response from the Notion API, indicating whether the task creation was successful or not.
#

    url = "https://api.notion.com/v1/pages"
    
    data = {
        "parent": { "database_id": notion_database_id },   # Specifies the database where the task will be created
        "properties": {
            "Task name": {
                "title": [
                    {
                        "text": {
                            "content": task_name
                        }
                    }
                ]
            },
            "Status": {
                "status": {
                    "name": status
                }
            }
        }
    }


# Optional date property if a date is provided
    if date:
        data["properties"]["Date"] = {
            "date": {
                "start": date
            }
        }

# Optional assignment property if a user ID is provided
    if assigned_to_id:
        data["properties"]["Assigned to"] = {
            "people": [
                {
                    "object": "user",
                    "id": assigned_to_id
                }
            ]
        }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))


# Check if the response was successful (status code 200 means OK)
    if response.status_code == 200:
        print("Page created successfully!")
        print(response.json())
    else:
        print(f"Failed to create page. Status code: {response.status_code}")
        print(response.json())   # Prints the JSON error response from the API



# Function to create a new task in Monday.com without assigning a person
def create_monday_task(board_id, group_id, item_name, status_label):

#    Creates a new task in Monday.com under a specified board and group, with a given status label.

    # args:
    #   board_id (int): The ID of the Monday.com board where the task should be created.
    #   group_id (str): The ID of the group within the board where the task will be placed.
    #   item_name (str): The name of the task to be created.
    #   status_label (str): The status label to be applied to the task.
    #
    # Returns:
    # - None, The function prints the result of the task creation process, indicating success or failure.
    #

    # Fetch existing tasks from Monday.com using fetch_monday_tasks function
    existing_tasks = fetch_monday_tasks()
    boards = existing_tasks.get('data', {}).get('boards', [])

    # Gathering names of all monday tasks, to avoid duplicates
    existing_task_names = []
    for board in boards:
        for item in board.get('items_page', {}).get('items', []):
            existing_task_names.append(item.get('name', 'Unnamed Task'))
    
    # Check if the task already exists
    if item_name in existing_task_names:
        print(f"Task '{item_name}' already exists in Monday.com. Skipping creation.")
        return

    # Construct the GraphQL mutation,
    # The mutation create_item is a predefined action within Monday.com's GraphQL API that tells the system to create a new task.
    query = """
    mutation {
      create_item (
        board_id: %s, 
        group_id: "%s", 
        item_name: "%s",
        create_labels_if_missing: true,
        column_values: "{\\"status__1\\":{\\"label\\":\\"%s\\"}}"
      ) {
        id
      }
    }
    """ % (board_id, group_id, item_name, status_label)

    # Send the request to create a new item in Monday.com
    response = requests.post('https://api.monday.com/v2/', json={'query': query}, headers=monday_headers)
    print(response.text)

# Check if the response was successful (status code 200 means OK)
    if response.status_code == 200:
        data = response.json()
        if 'errors' in data:
            print(f"Error creating item: {data['errors']}")
        else:
            print(f"Item created successfully! ID: {data['data']['create_item']['id']}")
    else:
        print(f"Failed to create item. Status code: {response.status_code}")
        print(response.json())



# Main function to recreate Monday.com tasks in Notion
def recreate_monday_tasks_in_notion():

#     Recreates tasks from Monday.com in Notion by fetching tasks from Monday.com and creating them in Notion
#     if they don't already exist.

#     Steps:
#     1. Fetches tasks from Monday.com.
#     2. Fetches existing tasks from Notion.
#     3. Loops through each task in Monday.com.
#     4. Extracts relevant task details such as task name, assigned person, and status.
#     5. Checks if the task already exists in Notion.
#     6. Maps the assigned person in Monday.com to a Notion user.
#     7. Creates the task in Notion if it doesn't already exist.
#
#     Returns:
#     - None: The function prints the progress and results of the task recreation process.

# Fetch tasks from monday.com and notion
    monday_tasks = fetch_monday_tasks()
    existing_notion_tasks = fetch_existing_notion_tasks()

#fetch boards from monday.com
    boards = monday_tasks.get('data', {}).get('boards', [])

    for board in boards:
        for item in board.get('items_page', {}).get('items', []):
            task_name = item.get('name', 'Unnamed Task')  # Get the task name or use 'Unnamed Task' as default
            person_name = None
            status = None

            # Extract relevant information
            for column_value in item.get('column_values', []):
                if column_value['id'] == 'person':  # Check for the person column
                    person_name = column_value.get('text')
                elif column_value['id'] == 'status__1':  # Check for the status column
                    status = column_value.get('text')

            # Check if task already exists in Notion
            if task_name in existing_notion_tasks:
                print(f"Task '{task_name}' already exists in Notion. Skipping creation.")
                continue

            # Map the person to a Notion user
            notion_person = map_monday_to_notion_person(person_name) if person_name else None
            assigned_to_id = notion_person['id'] if notion_person else None

            # Create task in Notion
            create_notion_task(task_name, status, assigned_to_id)

def recreate_notion_tasks_in_monday(board_id, group_id):

#     Recreates tasks from Notion in Monday.com by fetching tasks from Notion and creating them in Monday.com
#     if they don't already exist.

#     args:
#     - board_id: int or str, the ID of the Monday.com board where tasks will be created.
#     - group_id: str, the ID of the group within the Monday.com board where tasks will be created.

#     Steps:
#     1. Fetches existing tasks from Notion.
#     2. Fetches existing tasks from Monday.com to avoid duplicates.
#     3. Iterates through each task in Notion.
#     4. Checks if the task already exists in Monday.com.
#     5. Creates the task in Monday.com if it doesn't already exist.

#     Returns:
#     - None: The function prints the progress and results of the task recreation process.



    # Fetch existing tasks from Notion
    url = f"https://api.notion.com/v1/databases/{notion_database_id}/query"
    response = requests.post(url, headers=headers, data=json.dumps({}))

    # checking if the request was successful
    if response.status_code != 200:
        print(f"Failed to fetch existing tasks from Notion. Status code: {response.status_code}")
        print(response.json())
        return

    data = response.json()
    existing_notion_tasks = data.get('results', [])

    # Fetch existing tasks from Monday.com to avoid duplicates
    monday_tasks = fetch_monday_tasks()
    existing_monday_task_names = []
    boards = monday_tasks.get('data', {}).get('boards', [])

# Extract the names of existing tasks in Monday.com
    for board in boards:
        for item in board.get('items_page', {}).get('items', []):
            existing_monday_task_names.append(item.get('name', 'Unnamed Task'))

    # Iterate over existing Notion tasks to create them in Monday.com
    for task in existing_notion_tasks:
        task_name = task['properties']['Task name']['title'][0]['plain_text']
        notion_status = task['properties']['Status']['status']['name'] if 'Status' in task['properties'] else None

        # Check if task already exists in Monday.com
        if task_name in existing_monday_task_names:
            print(f"Task '{task_name}' already exists in Monday.com. Skipping creation.")
            continue

        # Use the Notion status directly as the Monday.com status label
        status_label = notion_status if notion_status else "Not started"  # Default to "Not started" if status is None

        # Create the task in Monday.com
        create_monday_task(board_id, group_id, task_name, status_label)



# Example usage
recreate_monday_tasks_in_notion()
recreate_notion_tasks_in_monday(board_id,group_id)

#create_monday_task(board_id, group_id, item_name, status_label)