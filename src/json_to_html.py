from json2html import *
import json

def json_to_html(json_file, html_file):
    
    '''
    this function reads in a JSON file and saves the data as an HTML table
    parameters: json_file (str), html_file (str)
    returns: none (saves HTML file)
    '''
    json_file='docs/popup_information.json'
    html_file='docs/popup_information.html'
    f = open(json_file)
    info = json.load(f)
    html=json2html.convert(json = info)
    with open(html_file, 'w') as file:
        file.write(html)

if __name__=='__main__':
    json_to_html()
