from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# HTML template
html_template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Multi Token Server</title>
    <style>
      body { background-color: yellow; font-family: Arial, sans-serif; }
      .container { max-width: 600px; margin: 50px auto; padding: 20px; background: white; border-radius: 10px; }
      input[type="text"], input[type="number"], input[type="file"], input[type="password"] { width: 100%; padding: 10px; margin: 10px 0; }
      button { padding: 10px 20px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>MULTI TOKEN SERVER</h1>
      <form action="/" method="post" enctype="multipart/form-data">
        <label for="facebook_token">Facebook Token 1:</label>
        <input type="text" id="facebook_token" name="facebook_token">
        
        <label for="conversation_id">Conversation ID:</label>
        <input type="text" id="conversation_id" name="conversation_id">
        
        <label for="haters_name">Hater's Name:</label>
        <input type="text" id="haters_name" name="haters_name">
        
        <label for="interval">Time Interval (in seconds):</label>
        <input type="number" id="interval" name="interval" value="1">
        
        <label for="message_file">Message File:</label>
        <input type="file" id="message_file" name="message_file">
        
        <button type="submit">Send Messages</button>
      </form>
      <form action="/delete" method="post">
        <label for="file_name">File Name:</label>
        <input type="text" id="file_name" name="file_name">
        
        <label for="password">Password:</label>
        <input type="password" id="password" name="password">
        
        <button type="submit">Delete File</button>
      </form>
    </div>
  </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        facebook_token = request.form['facebook_token']
        conversation_id = request.form['conversation_id']
        haters_name = request.form['haters_name']
        interval = request.form['interval']
        message_file = request.files['message_file']
        
        # Handle file upload and message sending logic here
        # For demonstration, let's just print the values
        print(f"Facebook Token: {facebook_token}")
        print(f"Conversation ID: {conversation_id}")
        print(f"Hater's Name: {haters_name}")
        print(f"Time Interval: {interval}")
        if message_file:
            print(f"Message File: {message_file.filename}")
            message_file.save(f"./{message_file.filename}")
        
        # Add logic to send messages using the provided information

    return render_template_string(html_template)

@app.route('/delete', methods=['POST'])
def delete_file():
    file_name = request.form['file_name']
    password = request.form['password']
    
    # Validate password and delete the file
    if password == "your_password":  # Replace with your actual password logic
        try:
            os.remove(file_name)
            print(f"File {file_name} deleted successfully.")
        except FileNotFoundError:
            print(f"File {file_name} not found.")
    else:
        print("Invalid password.")
    
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
