from imbox import Imbox

with Imbox('imap.bezlimit.ru',
           username='qa',
           password='Bezlimit2022',
           ssl=True,
           ssl_context=None,
           starttls=False) as imbox:
    unread_inbox_messages = imbox.messages(unread=True)
    print(unread_inbox_messages)
