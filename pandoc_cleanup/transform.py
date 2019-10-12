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


def transform(text):
    text = re.sub(
        r"""
            # get rid of extra spacing around brackets
            # [[url][ url ]] -> [[url][url]]
            \[
                \[\s*(.*?)\s*\]
                \[\s*(.*?)\s*\]
            \]
        """,
        lambda match: f"[[{match.group(1)}][{match.group(2)}]]",
        text,
        flags=re.VERBOSE,
    )

    text = re.sub(
        r"#\+BEGIN_HTML(.*?)#\+END_HTML",
        lambda match: html_example_to_text(
            match.group(1)
        ),  # call to_text for each match
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    text = re.sub(r":PROPERTIES:.*?:END:", "", text, flags=re.IGNORECASE | re.DOTALL)
    text = text.replace("\u00A0", " ")
    text = re.sub(r"(\\\\)[\r\n]", "\n", text)

    text = re.sub(
        r"""
            # remove [[]] and [[ ]]
            \[\[
                \s*
            \]\]
        """,
        "",
        text,
        flags=re.VERBOSE,
    )

    reg_url = re.compile(
        r"""
            # remove extra brackets around urls: Convert #1 to #2
            # 1: [[https://www.facebook.com/GeeksforGeeks-316764689022/timeline/][]]
            # 2: https://www.facebook.com/GeeksforGeeks-316764689022/timeline/
            \[\[                                              # pesky brackets
            (?P<url>                                          # start named group
                ({url_rs})                                    # valid url characters
                ?                                             # handle case: [[][]]
            )                                                 # end group
            \]\[                                              #
                (?://)*                                       # handle [[][//]]
            \]\]                                              # pesky brackets
        """.format(
            url_rs=url_rs
        ),
        flags=re.IGNORECASE | re.VERBOSE,
    )
    text = re.sub(reg_url, lambda match: f' {match.group("url")} ', text)

    reg_url = re.compile(
        r"""
            # [[][Products]] -> Products
            \[
                \[\]
                \[
                    ([^\]]+)
                \]
             \]
        """.format(
            url_rs=url_rs
        ),
        flags=re.VERBOSE,
    )
    text = re.sub(reg_url, lambda match: match.group(1), text)

    reg_url = re.compile(
        r"""
            \[\[
            (?P<url>
                ({url_rs}) | [^\]]*?
            )
            \]\[
            (?://)*
            \]\]
        """.format(
            url_rs=url_rs
        ),
        flags=re.IGNORECASE | re.VERBOSE,
    )
    text = re.sub(reg_url, lambda match: f' {match.group("url")} ', text)

    reg_url = re.compile(
        r"""(?P<markup>(
            \[
                \[(?P<url>([^\]]+))\]
                \[(?P<text>([^\]]+))\]
            \])
        )""",
        flags=re.IGNORECASE | re.VERBOSE,
    )
    text = re.sub(reg_url, lambda match: cleanup1(match), text)

    reg_whitespace = re.compile(
        r"""
            (?:\s+\n+)+
        """,
        flags=re.VERBOSE,
    )
    text = re.sub(reg_whitespace, "\n\n", text)

    ir = "|".join(
        ["footer", "header", "locationline", "logo", "pagebottom", "sidebar", "star"]
    )
    ir = f"<<{0}>>".format(ir)
    ir = re.compile(ir)
    text = re.sub(ir, "", text)

    text = re.sub("\n{3,}", "\n", text)

    return text


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
