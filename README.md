# 🏊‍♂️ Swimming Habit Tracker

Track and visualize your swimming habits using the Pixela API. This Python script allows you to log the number of pools you swim each day and see your progress over time.

## 🌟 Features

- **User Profile**: Automatically set up a new user profile on Pixela.
- **Swimming Graph**: Generate a visual graph to represent your swimming sessions.
- **Log Sessions**: Input the number of pools swum on any given day.
- **Modify Data**: Easily update or delete previously logged swimming data.

## 📦 Dependencies

- Python's `requests` library: Used for API interactions.

## 🚀 Getting Started

1. **Setup**: Ensure you've installed the `requests` library. You can install it using pip:
   ```
   pip install requests
   ```
2. **Configuration**: Update the `TOKEN`, `USERNAME`, and `GRAPH_ID` variables in the script with your preferred values.
3. **Run**: Execute the script. When prompted, input the number of pools you swam that day.
4. **Feedback**: The script will communicate with the Pixela API and display the result of your operation.

## 🔒 Security Note

Avoid hardcoding sensitive data like tokens directly in the script. It's recommended to use environment variables or external configuration files for better security.
