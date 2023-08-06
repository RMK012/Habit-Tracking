Overview
The Swimming Habit Tracker is a Python tool that leverages the Pixela API to help users monitor and visualize their swimming habits. Users can track the number of pools they swam each day and visualize their progress over time.

Features
User Creation: Set up a new user profile on Pixela.
Graph Creation: Create a dedicated swimming graph to visualize swimming habits.
Swimming Data Logging: Log the number of pools swum on a specific day.
Data Update: Modify previously logged data.
Data Deletion: Remove specific data entries if needed.
Dependencies
requests: Required for making HTTP requests to the Pixela API.
Usage
Ensure you have the requests library installed.
Update the TOKEN, USERNAME, and GRAPH_ID variables with your desired values.
Run the script and input the number of pools you swam when prompted.
The script will then interact with the Pixela API and provide feedback on the operation's success.
Note
For security reasons, avoid hardcoding sensitive information like tokens directly in the script. Consider using environment variables or external configuration files.
