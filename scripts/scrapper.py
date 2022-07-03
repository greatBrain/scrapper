import twint as tw
from datetime import datetime
from datetime import date
import os

class Scrapper:
      def __init__(self):          

          self.KEYWORDS = [ 
          'Banco Popular', 
          'AFP Popular', 
          'Grupo Popular', 
          'AFI Popular', 
          'Inversiones Popular',          
          ]          
      
      def _get_key(self):
          for key in self.KEYWORDS:
              yield key              

      def search(self):
          all_keywords = list(self._get_key())

          for keyw in range(len(all_keywords)):
              config = tw.Config()

              #Total tweets to scrape
              config.Limit = 300           
              config.Store_CSV = True
              config.Output = os.path.join("../reports/menciones_{}_.csv".format(datetime.today().strftime('%d-%m-%Y')))
              config.Search = all_keywords[keyw]
              tw.run.Search(config)
          
      def filter_data(self):
          pass


if __name__ == "__main__":
   scrp = Scrapper()
   scrp.search()





'''def scrap():
    config = tw.Config()
    config.Limit = 500 #Total tweets to scrape
    config.Store_CSV = True
    config.Output = "menciones.csv"
    config.Search = 'Banco Popular'
    tw.run.Search(config)



if __name__ == "__main__":
   scrap()'''