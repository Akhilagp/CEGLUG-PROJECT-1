import csv
import shutil
from collections import defaultdict
header=['It_name','It_qty','It_price']
class Supermarket():
  pdt_id=0
  pdt_name=' '
  pdt_qty=0
  pdt_price=0.00
  
  
  def prod_add(self,pdt_name,pdt_qty,pdt_price):
    with open('data.csv','a') as file:
      write=csv.DictWriter(file,fieldnames=header)
      write.writerow({'It_name':pdt_name,'It_qty':pdt_qty,'It_price':pdt_price})
    print('done')


      
  def prod_display(self):
    with open('data.csv','r')as file:
      read=csv.reader(file)
      for row in read:
        print(row)
 
  def prod_search(self,name_srch):
		count=0
		with open("data.csv","r") as file:
			reader=csv.DictReader(file,fieldnames=header)
			for row in reader:
				if row["It_name"]==name_srch:
					count=1
					break
			if count==1:
				print("found")
				
			else:
			  ch=input('Product not found\n1. to search another pdt\n2. to exit')
			  if(ch==1):
			    name_srch=raw_input("Enter another Product")
			    self.prod_search(name_srch)
			  elif(ch==2):
				  return
				
  def prod_update(self,name_update,quantity_update):
    
		
		with open("data.csv","r") as file,open('tmp.csv','w') as tmp_file:
			reader=csv.DictReader(file,fieldnames=header)
			writer=csv.DictWriter(tmp_file,fieldnames=header)
			for row in reader:
				if name_update==row["It_name"]:
					writer.writerow({'It_name':row["It_name"],'It_qty':quantity_update,'It_price':row["It_price"]})
				else:
					writer.writerow({'It_name':row["It_name"],'It_qty':row["It_qty"],'It_price':row["It_price"]})
		shutil.move('tmp.csv',"data.csv")
		print("Quantity updated!!")
	
	
  def prod_del(self,name_del):
  	flag=0
  	with open("data.csv","r") as file,open('tmp.csv','w') as tmp_file:
			reader=csv.DictReader(file,fieldnames=header)
			writer=csv.DictWriter(tmp_file,fieldnames=header)
			for row in reader:
				if(name_del!=row["It_name"]):
				  writer.writerow({'It_name':row["It_name"],'It_qty':row["It_qty"],'It_price':row["It_price"]})
				elif(name_del==row["It_name"]):
				  flag=1
				  
			if flag is 0:
			  print("product doesnt exist")
			else:
			  shutil.move('tmp.csv',"data.csv")
			  
  def bill_calc(self):
	  bill_amt=0.00
	  ch='y'
	  while(ch.lower()!='n'):
	    flag=0
	    self.prod_display()
	    bill_pdt=raw_input("enter product's name")
	    with open("data.csv",'r')as file:
	      reader_=csv.DictReader(file,fieldnames=header)
	      for row in reader_:
	        if(row["It_name"]==bill_pdt):
	          flag=1
	          bill_qty=raw_input("Enter qty of the product you want to buy")
	          bill_qty=int(bill_qty)
	          if(bill_qty<=int(row["It_qty"])):
	            bill_amt=bill_amt+(bill_qty*float(row["It_price"]))
	            new_qty=int(row["It_qty"]) - bill_qty
	            self.prod_update(row["It_name"],new_qty)
	          elif(bill_qty>int(row["It_qty"])):
	            print("sorry!!product out of stock")
	      if(flag==0):
	        print("product doesnt exist")
	    print("\n")
	    print(bill_amt)
	    
	    ch=raw_input("enter 'y' to continue and 'n' to exit")
	      
	    
	
sprmrkt=Supermarket()
print("Welcome!Have a great Shopping Experience!!")
enter='a'
while(enter!='e'):
  ch=raw_input("\n1.User\n2.Staff\n")
  if(int(ch)==1):
    ch_u=raw_input("\n1.Search\n2.Pay\n")
    if(int(ch_u)==1):
      n=raw_input('name to search')
      sprmrkt.prod_search(n)
    elif(int(ch_u)==2):
      sprmrkt.bill_calc()
    else:
      print("wrong choice\n")
      continue;
  elif(int(ch)==2):
    ch_s=raw_input("\n1.Add products\n2.Update products\n3.Delete products\n4.Display")
    if(int(ch_s)==1):
      name_=raw_input('enter pdt name')
      qty_=raw_input('enter quantity')
      price_=raw_input('enter price')
      sprmrkt.prod_add(name_,int(qty_),float(price_))
    elif(int(ch_s)==2):
      update_name=raw_input('name to update')
      update_qty=raw_input("enter new qty")
      sprmrkt.prod_update(update_name,int(update_qty))
      sprmrkt.prod_display()
    elif(int(ch_s)==3):
      del_name=raw_input('name to delete')
      sprmrkt.prod_del(del_name)
      sprmrkt.prod_display()
    elif(int(ch_s)==4):
      sprmrkt.prod_display()
    else:
      print("wrong choice")
      continue;
      
  enter=raw_input('\n enter e to exit or any character to continue:')

