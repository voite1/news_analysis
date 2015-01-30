import requests
import bs4

class Retriever(object):
    urlcount = 0
    sites = {}
    
    def scrapeGoogleNews(self):
        """ To get a list of news URL's from google """
        
        # Google news URL to use
        gUrl="http://news.google.com/"
        
        # Getting google news page
        response = requests.get(gUrl) 
        
        # Putting page into beautifulsoap
        soup = bs4.BeautifulSoup(response.content)

        for a in soup.find_all('a', id=True):
            # extracting 'href' attribute values from Tag a
            temp = a['href']
            
            # Removing google sites
            if "google" not in temp:
                temp = temp.strip()
                if not self.sites.has_key(temp):
                    self.sites[temp] = temp

        # Updating self.urelcount to list found urls
        self.urlcount = self.sites.__len__()

    def getNumberOfSites(self):
        """ Returns the number of URL's """
        return self.urlcount
    
    def getSitesDict(self):
        """ Returns dictionary containing sites as keys and values """
        return self.sites



if __name__ == "__main__":
    '''Test Class'''
    c = Retriever()
    c.scrapeGoogleNews()
    print(c.getSitesDict())
