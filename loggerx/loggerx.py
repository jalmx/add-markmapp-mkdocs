import logging

class LogX:

    def __init__(self, name="", debug=True):
        self.name = name
        self.debug = debug
        logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)


    def i(self, message):
        logging.info(message)
        print("Info:",message)

    def e(self, message,error=None):
        logging.error(f'{message}, Track: {error}')
        print("Error:", message, "Track:",error)


    def w(self, message):
        logging.warning(message)
        print("Warning:", message)

    def d(self, message):
        logging.debug(message)
        print("Debug:",message)


