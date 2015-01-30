import ProcessURL, ScrapeGoogle
import os
import datetime

def run(): 
    ''' This function calls ScrapeGoogle and ProcessURL functions
    to get the list of URL's from news.google.com and get the visible text
    from all news articles and places referenced by news.google.com
    '''
    
    # Scrape google new for links to new articles
    g = ScrapeGoogle.Retriever()
    g.scrapeGoogleNews()

    # Getting list of sights from ScrapeGoogle
    dict1 = g.getSitesDict()

    # instantiate time, it will be used for building filenames
    time1 = datetime.datetime.today()

    # Printing the number of sites retrieved
    print "The number of URL's is", dict1.__len__()

    # Construct filename for log file containing URL's for the day "-log.txt"
    filename = "../news_data/" + time1.strftime("%Y-%m-%d")
    filename = filename + "-log.txt"

    # Check if log file exists, if so, delete it
    if os.path.isfile(filename):
        os.remove(filename)

    # Get news, parse them and print the number of words in final dictionary
    count = 0
    for i in dict1:
        u = ProcessURL.URLProcessor()
        u.ProcessURL(dict1[i].strip())
        count = count + 1

        # Write log entry
        g = open(filename, "a")
        g.write(str(count) + "\t" + time1.strftime("%Y-%m-%d") + "\t" + str(u.getNumberOfWords()) + "\t" + dict1[i] + "\n")
        g.close()
    
        # Print the same entry to the console
        print count, "  ", u.getNumberOfWords(), " ", i

    # Getting unique word
    worddict = u.getWordsDict()

    # Build filename for data file to hold actual data ".txt"
    filename = "../news_data/" + time1.strftime("%Y-%m-%d") + ".txt"

    # Populate the data file
    f = open(filename, "w")
    for k in worddict:
        count = worddict[k]
        word = k
        today = time1.strftime("%Y-%m-%d")
        var = str(word) + ", " + str(count) + ", " + str(today)
        f.write(var + "\n")
    f.close()

    # print total number of words processed
    print
    print worddict.__len__()
    print "Done"

if __name__ == "__main__":
    run()
