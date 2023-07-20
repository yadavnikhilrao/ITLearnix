from flask import Flask, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'itlearnix@gmail.com'
app.config['MAIL_PASSWORD'] = 'veyqttrtaoahxsga'
app.config['MAIL_DEFAULT_SENDER'] = 'itlearnix@gmail.com'

# Configure the OAuth instances
mail = Mail(app)

# Flask route for the homepage
@app.route("/", methods=["GET",'POST'])
def home():
    return render_template("index.html")


# Courses
@app.route("/courses_1", methods=["GET",'POST'])
def course_1():
    return render_template("courses_1.html")

@app.route("/courses_2", methods=["GET",'POST'])
def course_2():
    return render_template("courses_2.html")




# Courses List
@app.route("/Business-Analytics-for-Beginners", methods=["GET", "POST"])
def course1():
    return render_template("Business Analytics for Biginners.html")

@app.route("/C-Programming-Basic-to-Advance", methods=["GET", "POST"])
def course2():
    return render_template("C Programming - Basic to Advance.html")

@app.route("/Computer-Vision-with-TensorFlow", methods=["GET", "POST"])
def course3():
    return render_template("Computer Vision with TensorFlow.html")

@app.route("/Data-Analysis-with-Python", methods=["GET", "POST"])
def course4():
    return render_template("Data Analysis with Python.html")

@app.route("/Data-Visualization-with-Advanced-Excel", methods=["GET", "POST"])
def course5():
    return render_template("Data Visualization with Advanced Excel.html")

@app.route("/Neural-Network-and-Deep-Learning-for-Beginners", methods=["GET", "POST"])
def course6():
    return render_template("Neural Network and Deep Learning for Beginners.html")

@app.route("/Full-Stack-Data-Science", methods=["GET", "POST"])
def course7():
    return render_template("Full Stack Data Science.html")

@app.route("/HTML-CSS-and-Javascript-for-Web", methods=["GET", "POST"])
def course8():
    return render_template("HTML, CSS, and Javascript for Web.html")

@app.route("/Java-Full-Stack-Development", methods=["GET", "POST"])
def course9():
    return render_template("Java Full Stack Development.html")

@app.route("/Java-Programming-Basic-to-Advance", methods=["GET", "POST"])
def course10():
    return render_template("Java Programming - Basic to Advance.html")

@app.route("/Machine-Learning-with-Python", methods=["GET", "POST"])
def course11():
    return render_template("Machine Learning with Python.html")

@app.route("/Power-BI-for-Business-Intelligence", methods=["GET", "POST"])
def course12():
    return render_template("Power BI for Business Intelligence.html")

@app.route("/Python-Basic-to-Advance", methods=["GET", "POST"])
def course13():
    return render_template("Python - Basic to Advance.html")

@app.route("/Python-Full-Stack-Development", methods=["GET", "POST"])
def course14():
    return render_template("Python Full Stack Development.html")

@app.route("/The-Complete-MySQL-Developer-Course", methods=["GET", "POST"])
def course15():
    return render_template("The Complete MySQL Developer Course.html")

@app.route("/DSA-in-Java", methods=["GET", "POST"])
def course16():
    return render_template("DSA in Java.html")



# Mentors
@app.route("/mentors", methods=["GET",'POST'])
def mentors():
    return render_template("mentors.html")

@app.route("/mentors-2", methods=["GET",'POST'])
def mentors_2():
    return render_template("mentors_2.html")


# Mentors List
@app.route("/mentor-nikhil", methods=["GET",'POST'])
def mentor1():
    return render_template("mentor-nikhil.html")

@app.route("/mentor-prakriti", methods=["GET",'POST'])
def mentor2():
    return render_template("mentor-prakriti.html")

@app.route("/mentor-nishant", methods=["GET",'POST'])
def mentor3():
    return render_template("mentor-nishant.html")

@app.route("/mentor-tripti", methods=["GET",'POST'])
def mentor4():
    return render_template("mentor-tripti.html")

@app.route("/mentor-ujjawal", methods=["GET",'POST'])
def mentor5():
    return render_template("mentor-ujjawal.html")

@app.route("/mentor-aman", methods=["GET",'POST'])
def mentor6():
    return render_template("mentor-aman.html")

@app.route("/mentor-vikas", methods=["GET",'POST'])
def mentor7():
    return render_template("mentor-vikas.html")


# Blogs
@app.route("/blogs", methods=["GET",'POST'])
def blogs():
    return render_template("coming-soon.html")


# contact
@app.route("/contact", methods=["GET",'POST'])
def contact():
    return render_template("contact.html")

@app.route('/register', methods=["GET",'POST'])
def register():
    return render_template("register.html")



@app.route('/register-succesful', methods=['POST'])
def register_succesful():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        course = request.form.get('course')
        email = request.form.get('email')
        phone = request.form.get('phone')

        # Create the email message for team member
        team_subject = 'New User Registration'
        team_body = f"Name: {user_name}\nCourse: {course}\nEmail: {email}\nPhone: {phone}"
        team_recipients = ['yadavnikhilrao@gmail.com']

        # Send email to team member
        team_msg = Message(subject=team_subject, body=team_body, recipients=team_recipients)
        mail.send(team_msg)

        # Create the email message for user
        user_subject = 'Course Enrollment Confirmation'
        user_body = f'''Dear {user_name},\n\nThank you for enrolling in the course: {course}. We are excited to have you as a student!\n\nAt ITLearnix, we strive to provide high-quality educational resources and support to help you succeed in your learning journey.
        Our team of experienced instructors is dedicated to delivering comprehensive course content and ensuring a valuable learning experience.\n\nIf you have any questions or need assistance during the course, feel free to reach out to our support team at itlearnix@gmail.com.
        We are here to help!\n\nOnce again, welcome to ITLearnix, and we look forward to seeing you thrive in your chosen course.\n\nBest regards,\nTeam ITLearnix'''

        user_recipients = [email]

        # Send email to user
        user_msg = Message(subject=user_subject, body=user_body, recipients=user_recipients)
        mail.send(user_msg)

        # Set the values for msg and line
        msg = 'Registration successful'
        line = 'Thank you for registering!'

        return render_template('notify.html', msg=msg, line=line)


@app.route('/subscribe', methods=['POST'])
def subscribe():
    if request.method == 'POST':
        email = request.form.get('email')

        # Create the email message for team member
        team_subject = 'New User Subscription'
        team_body = f"Email: {email}"
        team_recipients = ['yadavnikhilrao@gmail.com']

        # Send email to team member
        team_msg = Message(subject=team_subject, body=team_body, recipients=team_recipients)
        mail.send(team_msg)

        # Create the email message for user
        user_subject = 'Thanks for subscribing'
        user_body = f'''Dear Subscriber,\n\nThank you for subscribing to our newsletter. We are excited to have you on board!\n\nAt ITLearnix, we strive to provide valuable content and updates related to our courses and educational resources.\n\nIf you have any questions or need assistance, feel free to reach out to our support team at itlearnix@gmail.com. We are here to help!\n\nOnce again, thank you for subscribing, and we look forward to sharing valuable information with you.\n\nBest regards,\nTeam ITLearnix'''

        user_recipients = [email]

        # Send email to user
        user_msg = Message(subject=user_subject, body=user_body, recipients=user_recipients)
        mail.send(user_msg)

        # Set the values for msg and line
        msg = 'Subscription Successful'
        line = 'Thank you for subscribing to our newsletter!'

        return render_template('notify.html', msg=msg, line=line)


@app.route('/contact-form', methods=['POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Create the email message for team member
        team_subject = 'New Contact Form Submission'
        team_body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
        team_recipients = ['yadavnikhilrao@gmail.com']

        # Send email to team member
        team_msg = Message(subject=team_subject, body=team_body, recipients=team_recipients)
        mail.send(team_msg)

        # Set the values for msg and line
        msg = 'Message Sent'
        line = 'Thank you for contacting us! We will get back to you soon.'

        return render_template('notify.html', msg=msg, line=line)


if __name__ == '__main__':
    app.run()
