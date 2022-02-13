from requests_html import HTMLSession
import datetime


def date_validation(date_text):
    """Checks if given date is valid.
      in JS, method toISOString() return str with date format %Y-%m-%dT%H:%M:%S.%f%z, so we expecting
      from the response date to be in the same format.
    :param date_text: str date for test.
    """
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%dT%H:%M:%S.%f%z')
    except ValueError:
        raise ValueError("Incorrect data format, should be %Y-%m-%dT%H:%M:%SZ")


def nginx_container_health_check(url="http://localhost:30004/index.html"):
    """Test Nginx container.

    :param url: optional for change the default URL.
    :return:
    """
    # create an HTML Session object, the regular request module cant evaluate js in web pages.
    session = HTMLSession()
    # here we connecting to our nginx webpage :)
    resp = session.get(url)

    assert resp.status_code == 200, "Bad status code, it should be 200 !"
    # Here we run our JS in the index.html
    resp.html.render()
    # here we extract the date from body tag :)
    page_date = resp.html.find('body')[0].element.text.strip()

    date_validation(page_date)


