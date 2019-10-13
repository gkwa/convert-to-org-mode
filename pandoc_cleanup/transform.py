import logging
import re
import urllib

import bs4

logger = logging.getLogger("my_script")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

url_rs = "https?:\/\/[0-9a-zA-Z$_+!*'()\.,/-]{4,2048}"


def html_example_to_text(s):
    txt = bs4.BeautifulSoup(s, "html.parser").get_text()
    r = re.sub(r"\s+", txt, "", re.DOTALL)
    if not r:
        return ""
    return f"#+BEGIN_HTML\n{txt}\n#+END_HTML"


def cleanup1(match):
    """ [[http://google.com][http://google.com]] -> http://google.com"""
    if match.group("url") == match.group("text"):
        return match.group("url")
    return match.group("markup")


def remove_attrs(soup, attrs):
    """ example: convert #1 to #2
    #1: <div class="status" id="postamble">
    #2: <div class="status">
    """
    for attribute in attrs:
        for tag in soup.find_all(attrs={attribute: True}):
            del tag[attribute]
    return soup


def add_header(soup, baseurl):
    """ add header including original url """
    segment = f"""
    <h1>{"github" if "github.com" in baseurl.lower() else "article"}: {soup.title.string}</h1>
      <h2 id='summary'>summary</h2>
      <p><a href="{baseurl}">{baseurl}</a></p>
      <h2 id='separator'>separator</h2>
    """
    segment = bs4.BeautifulSoup(segment, "html.parser")
    # add segment as first child of body
    soup.body.insert(1, segment)
    return soup


def abs_links(soup, baseurl):
    """ make links absolute """
    tags = {"a": "href", "img": "src", "link": "href", "script": "src"}
    for tag in tags:
        attr = tags[tag]
        for item in soup.findAll(tag, {attr: True}):
            try:
                r = urllib.parse.urljoin(baseurl, item[attr])
                item[attr] = r
            except Exception as ex:
                logger.exception(f"attr={attr}, item={str(item)}")
    return soup


def remove_header_links(soup):
    """ remove links in headers """
    for elm in soup.find_all(re.compile(r"h\d", re.I)):
        for link in elm.select(":any-link"):
            link.extract()
    return soup


def remove_more_links(soup):
    """ remove pesky <<cross-reference-elements>> output by pandoc """
    for anchor in soup.find_all("a"):
        if "href" not in anchor.attrs:
            anchor.extract()
    return soup


def customize(html, baseurl):
    soup = bs4.BeautifulSoup(html, "html.parser")
    soup = remove_attrs(soup, ["id"])
    soup = add_header(soup, baseurl)
    soup = abs_links(soup, baseurl)
    soup = remove_header_links(soup)
    soup = remove_more_links(soup)
    return str(soup)
