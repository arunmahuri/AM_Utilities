import re


class utilities:
    def __init__(self, config):
        self.config = config
        self.word_count = {}

    def read_text(self, file_path):
        # read files to extract texts to be parsed
        pass

    def parse_string(self, data):
        """
        Function to read string data in data and parse it to extract words to calculate the count
        :param data:
        :return:
        """
        non_alpha = re.compile(self.config['parse_str'])
        data = non_alpha.sub('', data.lower())
        for word in data.split():
            self.word_count[word] = self.word_count.get(word, 0) + 1
        print(self.word_count)
