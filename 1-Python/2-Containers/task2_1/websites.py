
import webbrowser
favourite_websites={
    "Google":'https://www.google.com',
    "GetHub":'https://github.com',
    "Facebook":'https://www.facebook.com',
}

def open_websit_on_firfox(url):
    firefox_path='C:/Program Files/Mozilla Firefox/firefox.exe'
    webbrowser.register('firefox',None,webbrowser.BackgroundBrowser(firefox_path))
    webbrowser.get('firefox').open(url)











