from bs4 import BeautifulSoup
import html
import os
import json

test_file = open('message_1.html', 'r', encoding='utf-8').read()
sellers = ['Quỳnh Aeri']

def filter_msg(message):
    if("@" in message):
        return ""
    if("Đã bày tỏ cảm xúc" in message):
        return ""
    if("www" in message or "http" in message or "https" in message):
        return ""
    if("Giờ đây, các bạn có thể gọi và nhắn tin cho nhau" in message):
        return ""
    return message

def get_message_content(message):
    msg = message.find('div', class_='_2ph_ _a6-p')
    if msg is None:
        return ''
    div = msg.findAll('div')
    try:
        return html.unescape(filter_msg(div[2].text))
    except:
        return html.unescape(filter_msg(msg.text))

def get_sender(message):
    sender = message.find('div', class_='_2ph_ _a6-h _a6-i')
    if sender is None:
        return ''
    return sender.text

def get_messages(html):
    soup = BeautifulSoup(html, 'html.parser')
    messages_div = soup.find_all('div', class_='_3-95 _a6-g')[::-1]
    messages = []
    current_seller_message = ''
    current_buyer_message = ''
    current_sender = ''
    for message in messages_div:
        sender = get_sender(message)
        if (current_sender == ''):
            current_sender = sender
        if sender in sellers:
            current_seller_message += get_message_content(message) + "\n"            
        else:
            current_buyer_message += get_message_content(message) + "\n"
        if (current_sender != sender):
            messages.append((current_buyer_message, current_seller_message))
            current_buyer_message = ''
            current_seller_message = ''
            current_sender = sender
    return messages

path = os.walk('quynh')
html_files = []
for root, dirs, files in path:
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))
data = []
for file in html_files:
    html_file = open(file, 'r', encoding='utf-8').read()
    print(file)
    messages = get_messages(html_file)
    for message in messages:
        if(len(message[0]) > 1 and len(message[1]) > 1):
            data.append({'prompt': message[0], 'completion': message[1]})
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)