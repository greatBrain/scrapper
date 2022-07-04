import twint as tw
import datetime
import os

class Scrapper:
      def __init__(self):          

          self.KEYWORDS = [ 
          'BancoPopular',
          'BancoPopularDominicano', 
          'AFPPopular', 
          'GrupoPopular', 
          'AFIPopular', 
          'InversionesPopular',          
          ] 

          '''self.COUNTRIES = [
              "Dominican Republic", "Republica Dominicana"
          ]'''

          '''self.PROVINCES = [
              "Azua", "Baoruco", "Barahona", 
              "Dajabón", "Duarte", "El Seibo",
              "Elías Piña", "Espaillat", "Hato Mayor",
              "Hermanas Mirabal", "Independencia", "La Altagracia", 
              "La Romana", "La Vega", "María Trinidad Sanchez",
              "Monseñor Nouel", "Monte Cristi", "Monte Plata",
              "Pedernales", "Peravia", "Puerto Plata", "Samaná", 
              "San Cristobal", "san José de Ocoa", "San Juan", "San Pedro de Macorís", 
              "Sánchez Ramírez", "Santiago", "Santiago Rodríguez",
              "santo Domingo", "Valverde", "Distrito Nacional"
          ]'''

      def _get_date(self):
          range_date = datetime.datetime.now() - datetime.timedelta(days = 3)
          date = str(range_date).split()
          return date[0]

      
      def _get_key(self):
          for key in self.KEYWORDS:
              yield key              

      def search(self):
          all_keywords = list(self._get_key())
          
          for keyw in range(len(all_keywords)):
               config = tw.Config()

               #Total tweets to scrape
               config.Limit = 100    
               config.Since = self._get_date()    
               #config.Near =
               config.Store_CSV = True
               config.Output = os.path.join("../reports/menciones_{}_.csv".format(datetime.datetime.today().strftime('%d-%m-%Y')))
               config.Search = all_keywords[keyw]
               tw.run.Search(config)

         
      def get_total_mentions(self) -> int:
          pass


if __name__ == "__main__":
   scrp = Scrapper()
   print(scrp.search())
