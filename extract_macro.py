import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()
http = urllib3.PoolManager()
url = input('Ingresar URL de dndtools.net or d20srd.org: \n')
r = http.request('GET', url)
soup = BeautifulSoup(r.data.decode("utf-8"), features="lxml")
macro = '&{template:DnD35StdRoll} {{spellflag=true}} {{name=@{character_name} }} {{subtags=casts ['

if "dndtools" in url: 

    content = soup.body.find('div', attrs={'id' : 'content'})
    notes_html = content.find('div', attrs={'class' : 'nice-textile'})
    notes = '{{notes= ' + notes_html.get_text() + '}}'
    notes_html.decompose()
    split_content = str(content).split("<br/>")

    # Title and url
    title_url = BeautifulSoup(split_content[0], features="lxml")
    spell_url = title_url.find('div', attrs={'id' : 'inaccurate'}).a
    macro += title_url.h2.get_text() + "](" 
    macro += spell_url.attrs["href"].split("//")[1] + ")}}"

    # School
    school = BeautifulSoup(split_content[2], features="lxml")
    macro += '{{School:=' + school.get_text().replace("\n", " ") + '}}'

    # Parameters
    for split in split_content[3:-2]:
        split_html = BeautifulSoup(split, features="lxml")
        macro += '{{' + split_html.body.get_text().replace("\n", " ").replace(":",":=") + "}}"

    # Notes
    macro += notes

elif "d20srd" in url:
    name = soup.body.h1
    macro += name.get_text() + '](' + url + ")}}"
    name.decompose()

    # School
    school = soup.body.h4
    macro += '{{School:=' + school.get_text() + '}}'
    school.decompose()

    # Parameters
    table = soup.find('table', attrs={'class' :'statBlock' })
    for row in table.find_all('tr'):
        macro += '{{' + row.get_text().replace(":",":=").replace("\n", " ") + "}}"
    table.decompose()

    # Notes
    soup.find('div', attrs={'id' : 'header'}).decompose()
    soup.find('div', attrs={'class' : 'footer'}).decompose()
    for script_tag in soup.find_all('script'):
        script_tag.decompose()
    tables = soup.find_all('table')
    for table_tag in tables:
        table_tag.decompose()
    
    macro += '{{notes= ' + soup.body.get_text().replace("\n", " ") + '}}'

with open('macro.txt', 'w') as f:
    f.write(macro)