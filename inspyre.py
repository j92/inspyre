import requests
import json
import config
import smtplib

class Inspyre:
    QUOTE_API = "http://api.theysaidso.com/qod.json?category="

    def run(self):
        self.send_mail(self.get_quote())

    def get_quote(self):
        response = requests.get(self.build_api_url())
        return json.loads(response.content)

    def send_mail(self, daily_quote):
        msg = "\r\n".join([
            "From: " + config.sender_password,
            "To: " + config.recipient_mail,
            "Subject: " + daily_quote["contents"]["quotes"][0]["title"],
            daily_quote["contents"]["quotes"][0]["quote"],
            "- by Inspyre"
        ])

        s = smtplib.SMTP(config.smtp_server)
        s.ehlo()
        s.starttls()
        s.login(config.sender_mail, config.sender_password)
        s.sendmail(config.sender_mail, config.recipient_mail, msg)
        s.quit()

        return print("All done for the day")

    def build_api_url(self):
        return self.QUOTE_API + config.category


if __name__ == '__main__':
    Inspyre().run()
