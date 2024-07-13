from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.your-email-provider.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        recipient = request.form['recipient']
        description = request.form['description']
        model = request.form['model']
        item = request.form['item']
        location = request.form['location']
        date = request.form['date']
        sender_phone = request.form['sender_phone']
        sender_email = request.form['sender_email']
        name = request.form['name']
        semester = request.form['semester']
        section = request.form['section']

        # Creating the email body
        email_body = f"""
        Dear students,

        I have lost my {description} {model} {item} in {location} on {date}. 

        If found please contact me at {sender_phone} or {sender_email}.

        {name}
        {semester} Sem
        ‘{section}’ Section
        """

        msg = Message("Lost Item Notification", sender=app.config['MAIL_USERNAME'], recipients=[recipient])
        msg.body = email_body

        try:
            mail.send(msg)
            flash('Email sent successfully!')
        except Exception as e:
            flash(f'Failed to send email: {str(e)}')

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
