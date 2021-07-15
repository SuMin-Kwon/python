from class01 import Stock

li =  [["item", "open", "high", "low", "close"],
            ["A01", 100, 110, 70, 100],
            ["B01", 200, 210, 180, 190],
            ["A11", 300, 310, 300, 310]]
            
stock = Stock(li)

stock.print_close()
stock.print_close_grater( 150 ) 
print( stock.get_open_item( 'B01')  )
print( stock.get_diff_item( 'B01')  )
