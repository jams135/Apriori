import sys
from itertools import combinations

def count(ll):
	c=[]
	for i in range(len(ll)):
		tmp=0
		for j in range(rows):
			if(set(ll[i]).issubset(set(transactions[j]))):
				tmp+=1		
		c.append(tmp)
	return c
def prune(list1,c1):
	list2=[]  	#list2 has to be declared here compulsarily 
	for i in range(len(list1)):
		if(c1[i]>=min_sup):
			list2.append(list1[i])
	return list2		

#min_sup=input("\nenter minimum support")
min_sup=3

transactions=[["Mango","Onion","Jar","KeyChain","Eggs","Chocolates"],["Nuts","Onion","Jar","KeyChain","Eggs","Chocolates"],["Mango","Apple","KeyChain","Eggs"],["Mango","Toothbrush","Corn","KeyChain","Chocolates"],["Corn","Onion","Onion","KeyChain","Knife","Eggs"]]

print "\n\n=======================Transactions=======================\n"
rows=len(transactions)
#cols=len(transactions[0]) cant use as each row has different length

for i in range(rows):
    for j in range(len(transactions[i])):
	print transactions[i][j],
    print "\n"


#creates an array list1 of every unique element in transactions
list1=[]
count1=[]
for i in range(rows):
    for j in range(len(transactions[i])):
	if(transactions[i][j] not in list1):
		list1.append(transactions[i][j])
		
print "\n\n\n1 frequent itemset(Unique items in list1)\n"
print list1

#count for each unique item in list1 is stored in list c1[]
c1=[]
for i in range(len(list1)):			#for loop for items of list1
	tmp=0					
	for j in range(rows):			#for loop for rows of transaction
		s=set(transactions[j])		#for unique elements
		s=list(s)
		tmp+=s.count(list1[i])	#use inbuilt .count func only with 1D list
	c1.append(tmp)



"""THIS WORKS as above
#count of each item in unique list1
c1=[]
for item in (list1):
	c1.append(sum(x.count(item) for x in transactions))

			
"""
print "\n\ncount for 1-itemset\n"
print "list1","    \t\t","c1\n"
for i in range(len(c1)):
	print list1[i],"    \t\t",c1[i]

"""
this WONT WORK
for item in (c1):
	if(item<3):
		print item
		c1.remove(item)
"""

print "\n\nPrune 1 frequent itemset"
#here we remove elements that dont satisfy min support by creating another list

list2=prune(list1,c1)

print "\nAfter pruning list1 we get list2"
print '\nlist2\n'
for item in (list2):
	print item

#2 FREQUENT ITEMSET

list3=[]
print "\n\n2 frequent itemset\n"
list3=list(combinations(list2,2))
print list3

"""
#convert set to lists
l3=[]
#convert set to lists
for item in list3:
	item=list(item)
	l3.append(item)
"""
#convert set to lists
list3 = map(list, list3)
	
c3=count(list3)

#even if it is already a set we can use subset only with set function	
print "\n\ncount for 2-itemset\n"	

print repr('list3').rjust(40),repr('c3').rjust(10);
for i in range(len(c3)):
	#print list3[i],"    \t\t",repr(c3[i]).rjust(3);
	print repr(list3[i]).rjust(40),repr(c3[i]).rjust(10);

print "\n\nPrune 2 frequent itemset"  
list4=prune(list3,c3)		#PRUNE

print "\nafter pruning list3 we get list4"
print "\nlist4\n"
for item in (list4):
	print item

#3 FREQUENT ITEMSET
#union of sets order changes, sets order changes

length=len(list4[0])-1
#print length

list5=[]  #works without declaration too
temp=[]
for i in range(len(list4)):
	
	for j in range(i+1,len(list4)):
		if (list4[i][0:length])==(list4[j][0:length]):
			list5.append(list4[i]+list4[j][length:])



c5=count(list5)		#COUNT

#print list5 and c5
print "\n\n3 frequent itemset with count\n"
print 'list5',"    \t\t\t\t\t",'c5\n'
for i in range(len(c5)):
	print list5[i],"    \t\t",c5[i]

#prune3 for list5
list6=prune(list5,c5)	#PRUNE

print "\n\nafter pruning list5 we get list6"
print "\nlist6\n"
for item in (list6):
	print item
			
##########association rules for 3frequent item set##############
print "\n\nAssociation rules\t\tconfidence"
for item in (list6):
	
	l1= item

	l2=item
	l2= list(combinations(item, 2))
	l2 = map(list, l2)
	#print l2
	

	ans=0.0

	
	for item1 in l1:
		ind=list1.index(item1)
		for item2 in l2:
			if item1 not in item2:
				ans=float(min_sup)/c1[ind]	
				print item1,'--->',item2," ",ans
				

	for item2 in l2:
		ind=list3.index(item2)
		for item1 in l1:
			if item1 not in item2:
				ans=float(min_sup)/c3[ind]	
				print item2,'--->',item1," ",ans
		


"""
Output:
jamila@ubuntu:~/apriori$ python ap3.py

enter minimum support3
=======================Transactions=======================

Mango Onion Jar KeyChain Eggs Chocolates 

Nuts Onion Jar KeyChain Eggs Chocolates 

Mango Apple KeyChain Eggs 

Mango Toothbrush Corn KeyChain Chocolates 

Corn Onion Onion KeyChain Knife Eggs 

Unique list1
['Mango', 'Onion', 'Jar', 'KeyChain', 'Eggs', 'Chocolates', 'Nuts', 'Apple', 'Toothbrush', 'Corn', 'Knife']

list1     		c1
Mango     		3
Onion     		3
Jar     		2
KeyChain     		5
Eggs     		4
Chocolates     		3
Nuts     		1
Apple     		1
Toothbrush     		1
Corn     		2
Knife     		1

Prune
After pruning list1 we get list2

list2
Mango
Onion
KeyChain
Eggs
Chocolates

2 frequent itemset
[('Mango', 'Onion'), ('Mango', 'KeyChain'), ('Mango', 'Eggs'), ('Mango', 'Chocolates'), ('Onion', 'KeyChain'), ('Onion', 'Eggs'), ('Onion', 'Chocolates'), ('KeyChain', 'Eggs'), ('KeyChain', 'Chocolates'), ('Eggs', 'Chocolates')]

count for 2-itemset
list3     		c3
['Mango', 'Onion']     		1
['Mango', 'KeyChain']     		3
['Mango', 'Eggs']     		2
['Mango', 'Chocolates']     		2
['Onion', 'KeyChain']     		3
['Onion', 'Eggs']     		3
['Onion', 'Chocolates']     		2
['KeyChain', 'Eggs']     		4
['KeyChain', 'Chocolates']     		3
['Eggs', 'Chocolates']     		2
Prune (2 frequent itemset)

after pruning list3 we get list4
['Mango', 'KeyChain']
['Onion', 'KeyChain']
['Onion', 'Eggs']
['KeyChain', 'Eggs']
['KeyChain', 'Chocolates']
list5     		c5
['Onion', 'KeyChain', 'Eggs']     		3
['KeyChain', 'Eggs', 'Chocolates']     		2

after pruning list5 we get list6
list6
['Onion', 'KeyChain', 'Eggs']

Association rules		confidence
Onion ---> ['KeyChain', 'Eggs']   1.0
KeyChain ---> ['Onion', 'Eggs']   0.6
Eggs ---> ['Onion', 'KeyChain']   0.75
['Onion', 'KeyChain'] ---> Eggs   1.0
['Onion', 'Eggs'] ---> KeyChain   1.0
['KeyChain', 'Eggs'] ---> Onion   0.75
jamila@ubuntu:~/apriori$ 
"""
