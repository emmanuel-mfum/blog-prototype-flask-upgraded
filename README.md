# blog-prototype-flask-upgraded
Prototype for a personal blog written using Python and the Flask framework but now with added features

We have built upon the "blog-prototype-flask" project listed in the repositories and added Boostrap via Flask-Bootstrap and added a feature that sends emails
to the own of the site via the smtplib package. The email content comes from what the user writes in the contact page. The contatc page has a form and the data 
sent from the form is extracted with the request module. The said data is then going to be used create an email.

If the email is successfully sent, the email is redirected to the contact page ('contact.html') and a success message is displayed.
