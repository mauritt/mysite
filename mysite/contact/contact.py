import os

from django.conf.urls import url
from django.shortcuts import render
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse




def index(request):
    return render(request, 'contact/index.html')

def send(request):
    emailInfo = {}
    emailInfo['frmEmailAddress'] = os.environ.get('EMAIL_HOST_USER')
    emailInfo['frmEmailPassword'] = os.environ.get('EMAIL_HOST_PASSWORD')
    emailInfo['frmEmailServer'] = os.environ.get('EMAIL_HOST')
    
    message = request.POST['message']
    fromWhom = request.POST['name']

    msg = MIMEText(message, 'plain')
    msg['Subject'] = 'Test from %s' % fromWhom
    msg['To'] = 'mauritt@gmail.com'
    frmEmail, frmEmailPassword, frmEmailServer = emailInfo['frmEmailAddress'], emailInfo['frmEmailPassword'],emailInfo['frmEmailServer'] 
    
    try:
        conn = SMTP_SSL(frmEmailServer)
        conn.login(frmEmail, frmEmailPassword)
        try:
            conn.sendmail(frmEmail, 'mauritt@gmail.com', msg.as_string())
        finally:
            conn.close()
    finally:
        return HttpResponseRedirect(reverse('contact:sent'))

def sent(request):
    return render(request, 'contact/sent.html')




urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^send$', send, name = 'send'),
    url(r'^sent$', sent, name= 'sent')
]
