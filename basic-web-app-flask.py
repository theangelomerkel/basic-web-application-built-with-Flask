from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my website!'

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # handle the form submission
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # send an email or save the message to a database
        return 'Thank you for your message, {}! We will get back to you soon.'.format(name)
    else:
        # display the contact form
        return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
