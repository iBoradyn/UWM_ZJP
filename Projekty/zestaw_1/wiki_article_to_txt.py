from html.parser import HTMLParser
import urllib.request

from bs4 import BeautifulSoup


class Parse(HTMLParser):
    def __init__(self):
        super().__init__()

        self.div_recording = 0
        self.p_recording = 0
        self.data = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != 'div' and tag != 'p':
            return

        if tag == 'div' and self.div_recording:
            self.div_recording += 1
            return
        if tag == 'p' and self.div_recording:
            self.p_recording += 1
            return

        for name, value in attrs:
            if name == 'id' and value == 'mw-content-text':
                break
        else:
            return

        self.div_recording = 1

    def handle_endtag(self, tag):
        if tag == 'div' and self.div_recording:
            self.div_recording -= 1
        if tag == 'p' and self.p_recording:
            self.p_recording -= 1

    def handle_data(self, data):
        if self.div_recording and self.p_recording:
            self.data.append(data)


# Import HTML from a URL
url = urllib.request.urlopen("https://pl.wikipedia.org/wiki/Specjalna:Losowa_strona")
html = url.read().decode()
url.close()

p = Parse()
p.feed(html)
with open('html_parser_wiki_article.txt', 'w') as file:
    file.write(' '.join(p.data))

soup = BeautifulSoup(html, 'html.parser')
div = soup.find(id='mw-content-text')
with open('beautifulsoup4_wiki_article.txt', 'w') as file:
    file.write(div.get_text())

