import requests

def send_simple_message(email,url):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxb8cd6ecc5fc74729b63bdca5bb2bd2c2.mailgun.org/messages",
        auth=("api", "key-3c04a8adfc7a31d67c54864fa5352213"),
        data={"from": "OpenML <postmaster@sandboxb8cd6ecc5fc74729b63bdca5bb2bd2c2.mailgun.org>",
              "to": "<%s>" % email,
              "subject": "Your ML model is ready",
              "text": "You can interact with your new ML model by clicking the following link:\n%s" % url})
