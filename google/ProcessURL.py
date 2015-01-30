import html2text
import urllib
import re


class URLProcessor(object):
    
    words = {}
    size = 0
    
    def ProcessURL(self, url):
        
        # Setting up html2text
        h = html2text.HTML2Text()
        h.ignore_links = True
        
        # Reading the url
        html = urllib.urlopen(url).read()
        
        # Parsing text with html2text
        try:
            result = h.handle(html.decode('unicode-escape'))
        except Exception, err:
            print "Error parsing", url
            print err
            return None

            
        # Removing urls from text
        result = re.sub(r'http?:\/\/.*[\r\n]*', '', result)
        result = re.sub(r'https?:\/\/.*[\r\n]*', '', result)
        
        # Extracting unique words
        result = result.split()
        for i in result:
            # Assure getting alpha words only
            if re.match(r'[a-zA-Z]', i):
                # if not alpha, substitute non-alpha with space
                i = re.sub('[^a-zA-Z]', ' ', i)
                # Check if after splitting there only one token
                # more then one - discard
                if len(i.split()) == 1:
                    i = i.lower().strip()
                    # Testing if the word is in the dictionary: if not, add a list
                    # containing word, and count
                    if self.words.has_key(i):
                        self.words[i] = self.words[i] + 1
                    else:
                        self.words[i] = 1

    
    def getWordsDict(self):
        """ Returns the dictionary of words """
        return self.words
    
    def getNumberOfWords(self):
        """ Returns the number of words in the dictionary """
        return self.words.__len__()


if __name__ == "__main__":
    c = URLProcessor()
    c.ProcessURL('http://mashable.com/2015/01/23/will-ferrell-cheerleader-stunt/')
    dct = c.getWordsDict()
    for i in dct:
        print i, dct[i]