
import mechanicalsoup
from requests import Session
from sys import version_info
from requests.adapters import HTTPAdapter
from urllib3.util.ssl_ import create_urllib3_context

CIPHERS = (
    ':@SECLEVEL=2:ECDH+AESGCM:ECDH+CHACHA20:ECDH+AES:DHE+AES:!aNULL:!eNULL:!aDSS:!SHA1:!AESCCM'
)

class DESAdapter(HTTPAdapter):
    """
    A TransportAdapter that re-enables 3DES support in Requests to avoid Cloudflare filtering based on SSL profiling
    Adapted from the research provided by Nick Ostendorf (@nickostendorf) in https://github.com/j-andrews7/kenpompy/issues/33
    """

    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=CIPHERS)
        kwargs['ssl_context'] = context
        return super(DESAdapter, self).init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=CIPHERS)
        kwargs['ssl_context'] = context
        return super(DESAdapter, self).proxy_manager_for(*args, **kwargs)

def environment_requires_DES_adapter():
    return version_info.major == 3 and version_info.minor < 11
	

def login(email, password):
    session = Session()
	
    if environment_requires_DES_adapter():
        session.mount('https://kenpom.com/', DESAdapter())

    browser = mechanicalsoup.StatefulBrowser(session)
    browser.set_user_agent('Mozilla/5.0')
    browser.open('https://kenpom.com/index.php')

    if 'Cloudflare' in browser.page.title.string:
        raise Exception(
            'Opening kenpom.com failed - request was intercepted by Cloudflare protection')

    # Response page actually throws an error but further navigation works and will show you as logged in.
    browser.get_current_page()
    browser.select_form('form[action="handlers/login_handler.php"]')
    browser['email'] = email
    browser['password'] = password

    response = browser.submit_selected()

    if response.status_code != 200 or 'PHPSESSID=' not in response.headers['set-cookie']:
        raise Exception(
            'Logging in to kenpom.com failed - check that the site is available and your credentials are correct.')
    
    if 'subscription expired' in str(browser.get('https://kenpom.com/index.php').content):
        raise Exception(
            'Logging in to kenpom.com failed - account subscription is expired')

    return browser
