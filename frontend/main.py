from browser import document, html
import browser

def hello(ev):
    browser.alert('Hello cloud-django-brython!')

print('WELCOME CLOUD-DJANGO-BRYTHON')
# Insert Header into document body
document <= html.H1("WELCOME CLOUD-DJANGO-BRYTHON", Id="main")

hello_button = html.BUTTON("hello")
hello_button.bind("click", hello)

document <= hello_button
