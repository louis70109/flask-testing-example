from models.stream import Stream

NAME = "Brown"

def stream_hello():
    stream = Stream(name='sally')
    text = stream.hello()
    return text

def stream_world():
    stream = Stream
    text = stream.world()
    return text


def item_tax(payload):
    return payload['value'] * payload['tax']


def something():
    return 'Hello'
