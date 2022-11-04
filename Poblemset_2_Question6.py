from html.parser import HTMLParser

# Inherit from Html parser
class HeadingParser(HTMLParser):
    # Define the headings
    headers = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']

    # Handle the functions
    def handle_starttag(self, tag, attrs):
        if tag in self.headers:
            print(tag)

    def handle_endtag(self, tag):
        if tag in self.headers:
            print(tag)

    def handle_data(self, data):
        print(data)

# TEST HERE
parser = HeadingParser()
infile = open('w3c.html')
content = infile.read()
infile.close()
hp = HeadingParser()
hp.feed(content)

