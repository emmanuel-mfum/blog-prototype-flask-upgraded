from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)

EMAIL = "*************"
PASSWORD = "***********"


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/0067e63917ca7a5034d9"
    response = requests.get(url=blog_url)  # GET request
    blog_data = response.json()  # transform the data we get into JSON
    return render_template('index.html', posts=blog_data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone']
        message = request.form['message']
        success = True
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # secure connection with TLS
            connection.login(user=EMAIL, password=PASSWORD)  # login into the email address of the sender
            connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                                msg=f"Subject: New Message !\n\n Name:{name}\n Email:{email}\n Phone:{phone_number}\n"
                                    f"Message:{message}")  # sends email

        return render_template('contact.html', status=success)  # sends a boolean variable for display success message
    else:
        return render_template('contact.html')


@app.route('/post/<post_id>')
def get_post(post_id):
    blog_url = "https://api.npoint.io/0067e63917ca7a5034d9"
    response = requests.get(url=blog_url)
    blog_data = response.json()
    return render_template('post.html', posts=blog_data, num=int(post_id))


if __name__ == "__main__":
    app.run(debug=True)
