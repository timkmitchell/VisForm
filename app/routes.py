from flask import Flask, render_template, request, flash
from forms import ContactForm

from flask_mail import Mail, Message

#new instance on the Flask class
app = Flask(__name__)   

#CSRF prevention-checks for matching token
#If it matches the handling and validation continues
app.secret_key = '$3@$ging5gj%24'

mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'tmitchell822@gmail.com'
app.config["MAIL_PASSWORD"] = 'jvndpiuweapjjufo'
mail.init_app(app)

#maps URL'/' to the "home" function
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/visform', methods = ['GET', "POST"])
def visform():
    form = ContactForm()

    if request.method == "POST":
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('visform.html', form=form)
        else:
            msg = Message(form.subject.data, sender='contact@example.com', recipients=['tmitchell822@gmail.com'])
            msg.body = """ 
        From: %s <%s> 
        %s 
        """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('visform.html', success=True)
    elif request.method =='GET':
        return render_template('visform.html', form=form)
  
if __name__ == '__main__':
  app.run(debug=True)