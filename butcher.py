
from ctypes.wintypes import HACCEL
from datetime import date, datetime
from sqlite3 import Date


class Shop:
    def __init__(self, company_name,item):
      self.company_name=company_name
      self.item=item
      self.intial_kgs=0
    def stock_kg(self,kgs):
        self.kgs=kgs
        if kgs<=0:
            return "you have entered an evalid number"
        else:
            self.intial_kgs+=kgs
        return f"Hello you have {self.intial_kgs} kgs" 
    def sold_stock(self,kg):
        self.kgs=kg
        if kg >self.intial_kgs:
            date=datetime.now()
            print(f"we have less kilograms today {date.strftime('%d/%-H/%m/')}")

        else:
        
            self.intial_kgs-=kg
            return f"your remaining kgs are {self.intial_kgs} "    

        
        


    

