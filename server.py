from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# 1
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# 2
@app.route('/dojo')
def dojo():
    return 'Dojo!'

# 3
@app.route('/say/<string:word>')
def say(word):
    return f"{word}"

# 4
@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return f"{word * num} "


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

