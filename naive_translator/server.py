import logging

import tornado.ioloop
import tornado.web

from . import translator
from .config import DEFAULT_PORT


# noinspection PyAbstractClass
class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        html = """
        <h1>Welcome!<h1>
        <ul>
            <li><a href='/dicts' target='_blank'>/dicts</a></li>
            <li><a href='/translate?dict=&text=' target='_blank'>/translate?dict=&text=</a></li>
        </ul>
        """
        return self.finish(html)


# noinspection PyAbstractClass
class TranslateHandler(tornado.web.RequestHandler):
    def get(self):
        origin = self.get_argument('text')
        use = self.get_argument('dict', None)
        return self.translate(origin, use)

    def post(self):
        origin = self.request.body.decode('utf8')
        use = self.get_argument('dict', None)
        return self.translate(origin, use)

    def translate(self, origin, use=None):
        use = use or translator.use
        translation = translator(origin)
        logging.info(f'{origin} => {translation}')
        return self.finish({'dict': use, 'translation': translation})


# noinspection PyAbstractClass
class ListDictsHandler(tornado.web.RequestHandler):
    def get(self):
        self.finish({'dicts': translator.all_uses})


def make_app():
    return tornado.web.Application([
        (r'/', HomeHandler),
        (r'/translate', TranslateHandler),
        (r'/dicts', ListDictsHandler),
    ])


def start_server(port: int = DEFAULT_PORT):
    app = make_app()
    app.listen(port)
    print(f'Start server on port: {port}')
    tornado.ioloop.IOLoop.current().start()
