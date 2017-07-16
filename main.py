import csv
import shutil
from collections import defaultdict
header=['It_id','It_name','It_qty','It_price']
class Supermarket():
  pdt_id=0
  pdt_name=' '
  pdt_qty=0
  pdt_price=0.00
  
  
  def prod_add(self,pdt_id,pdt_name,pdt_qty,pdt_price):
    with open('data.csv','a') as file:
      write=csv.DictWriter(file,fieldnames=header)
      write.writerow({'It_id':pdt_id,'It_name':pdt_name,'It_qty':pdt_qty,'It_price':pdt_price})
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
				return 1
				
			else:
			  ch=input('Product not found\n1. to search another pdt\n2. to exit')
			  if(ch==1):
			    name_srch=raw_input("Enter another Product")
			    self.prod_search(name_srch)
			  elif(ch==2):
				  return
				
  def prod_update(self,name_update):
    
		quantity_update=input("Enter the new quantity")
		with open("data.csv","r") as file,open('tmp.csv','w') as tmp_file:
			reader=csv.DictReader(file,fieldnames=header)
			writer=csv.DictWriter(tmp_file,fieldnames=header)
			for row in reader:
				if name_update==row["It_name"]:
					writer.writerow({'It_id':row["It_id"],'It_name':row["It_name"],'It_qty':quantity_update,'It_price':row["It_price"]})
				elif(self.prod_search(name_update)!=1):
				  print("product doesnt exist")
				else:
					writer.writerow({'It_id':row["It_id"],'It_name':row["It_name"],'It_qty':row["It_qty"],'It_price':row["It_price"]})
		shutil.move('tmp.csv',"data.csv")
		print("Quantity updated!!")
	
	
  def prod_del(self,name_del):
  	flag=0
  	with open("data.csv","r") as file,open('tmp.csv','w') as tmp_file:
			reader=csv.DictReader(file,fieldnames=header)
			writer=csv.DictWriter(tmp_file,fieldnames=header)
			for row in reader:
				if(name_del!=row["It_name"]):
				  writer.writerow({'It_id':row["It_id"],'It_name':row["It_name"],'It_qty':row["It_qty"],'It_price':row["It_price"]})
				elif(name_del==row["It_name"]):
				  flag=1
				  
			if flag is 0:
			  print("product doesnt exist")
			else:
			  shutil.move('tmp.csv',"data.csv")
			  
  def bill_calc(self):
	  bill_amt=0.00
	  ch='Y'
	  while(ch.lower()!='n'):
	    self.prod_display()
	    bill_pdt=raw_input("enter product's name")
	    with open("data.csv",'r')as file:
	      reader_=csv.DictReader(file,fieldnames=header)
	      for row in reader_:
	        if(row["It_name"]==bill_pdt):
	          bill_qty=raw_input("Enter qty of the product you want to buy")
	          bill_qty=int(bill_qty)
	          if(bill_qty<=int(row["It_qty"])):
	            bill_amt=bill_amt+(bill_qty*float(row["It_price"]))
	            row["It_qty"]=int(row["It_qty"]) - bill_qty
	          elif(bill_qty>int(row["It_qty"])):
	            print("sorry!!product out of stock")
	      print("product doesnt exist")
	    print("\n")
	    print(bill_amt)
	    
	    ch=raw_input("enter 'y' to continue and 'n' to exit")
	      
	    
	
sprmrkt=Supermarket()
while(1):
  print("Welcome!Have a great Shopping Experience!!")
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
      exit(0)
  elif(int(ch)==2):
    ch_s=raw_input("\n1.Add products\n2.Update products\n3.Delete products")
    if(int(ch_s)==1):
      name_=raw_input('enter pdt name')
      id_=raw_input('enter pdt id')
      qty_=raw_input('enter quantity')
      price_=raw_input('enter price')
      sprmrkt.prod_add(int(id_),name_,int(qty_),float(price_))
    elif(int(ch_s)==2):
      update_name=raw_input('name to update')
      sprmrkt.prod_update(update_name)
      sprmrkt.prod_display()
    elif(int(ch_s)==3):
      del_name=raw_input('name to delete')
      sprmrkt.prod_del(del_name)
      sprmrkt.prod_display()
    else:
      print("wrong choice")
      exit(0)
