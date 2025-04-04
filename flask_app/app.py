from flask import Flask, request, render_template_string # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    form_html = '''
    <form method="POST">
        Name: <input type="text" name="name"><br>
        Age: <input type="number" name="age"><br>
        <input type="submit" value="Submit">
    </form>
    '''
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        if not name or not age:
            return "Please enter both name and age."
        return f"Hello, {name}! You are {age} years old."
    return render_template_string(form_html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)