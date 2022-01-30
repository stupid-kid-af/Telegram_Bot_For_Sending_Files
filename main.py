from telegram_api import *

TOKEN = '5191602086:AAEmmBFBS5Gu0761lxZWyY_qCsthvcKtTUo'
CHAT_ID = '1987074996'

telegram(file = open('linux-image-5.16.4_5.16.4-1_amd64.deb', 'rb'), filetype = 'Document', token = TOKEN, chat_id = CHAT_ID)
telegram(file = open('linux-headers-5.16.4_5.16.4-1_amd64.deb', 'rb'), filetype = 'Document', token = TOKEN, chat_id = CHAT_ID)
telegram(file = open('linux-libc-dev_5.16.4-1_amd64.deb', 'rb'), filetype = 'Document', token = TOKEN, chat_id = CHAT_ID)
