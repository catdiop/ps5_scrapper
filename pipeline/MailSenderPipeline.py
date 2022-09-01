import smtplib
from itemadapter import ItemAdapter
from scrapy import Item
from email.message import EmailMessage

from settings import MAIL_USER, MAIL_APP_PASSWORD

class MailSenderPipeline:

    def sendMail(self, item: Item):
        adapter = ItemAdapter(item)
        msg = EmailMessage()
        name = adapter.get('name').replace('\n', ' ')
        msg.set_content(f"Prix {adapter.get('price')}")
        msg['Subject'] = f"Scrawler : {name} disponible"
        msg['From'] = MAIL_USER
        msg['To'] = [MAIL_USER]
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(MAIL_USER, MAIL_APP_PASSWORD)
            server.send_message(msg)

        except Exception as e:
            print(e)

    def process_item(self, item, spider):
        self.sendMail(item)
        return item