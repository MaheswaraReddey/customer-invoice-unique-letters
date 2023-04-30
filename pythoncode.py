print("Amount for Introduction to Python Programming Book               :Rs.499")
b1=int(input("Enter number of books for Introduction to Python Programming Book:"))
print("Amount for Python Libraries Cookbook                             :Rs.855")
b2=int(input("Enter number of books for Python Libraries Cookbook              :"))
print("Amount for Data Science in Python Book                           :Rs.645")
b3=int(input("Enter number of books for Data Science in Python Book            :"))
n1=499*b1
n2=855*b2
n3=645*b3
GST=(n1+n2+n3)*(12/100)
print("Total Amount for the books                                       :Rs.",(n1+n2+n3))
print("Additional GST tax on all the books is	                         :Rs.",round(GST))
print("Delivery charges are                                             :Rs.250")
print("Total Invoice Amount with GST&delivery charge is                 :Rs.",round(n1+n2+n3+GST+250))







