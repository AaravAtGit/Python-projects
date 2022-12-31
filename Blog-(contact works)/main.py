from flask import Flask, render_template,request
import requests
import smtplib

gmail = "mail"
email_password = "pass"

posts = requests.get("https://api.npoint.io/eb8c008084279504fc66").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(gmail, email_password)
        connection.sendmail(gmail,"another mail", email_message)

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        details = request.form
        send_email(details["name"],details["email"],details["phone"],details["message"])
        return "<h1>Message sent</h1>"
    else:
        return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
