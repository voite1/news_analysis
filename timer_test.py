import time
from google import NewsProcessor as news
from yahoo import NASDAQProcessor as stock

def my_cron(interval=86400, days=30):
    ''' Setup timer to run data gathering routines 
    default is 24 hours. The interval is specified in seconds.
    usage: my_cron(interval, days) where interval is 
    24 hours expressed in seconds. days is the number of
    days to run '''
    
    # Day counter
    i=0
    
    # Run daily routine
    while (1):
        
        # Check for the number of days
        if (i == days): 
            break
        
        print "Run # {0}".format(i + 1)
        news.run()
        print "Processed news...."
        stock.run()
        print "Processed NASDAQ"
        # Default is 24 hours (86400 seconds)
        time.sleep(interval) 
    
        # Increment counter
        i = i + 1

if __name__ == "__main__":
    my_cron(300, 2)