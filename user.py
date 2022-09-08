import admin2 as ad
class user:
      login_info={}
      def __init__(self,email,name,phone_no,address,password):
          self.email=email
          self.name=name
          self.phone_no=phone_no
          self.address=address
          self.password=password
          user.login_info[self.email]={'Email':self.email,'Full_Name':self.name,'Phone_no':self.phone_no,
                                    'Address':self.address,
                                    'Password':self.password,
                                               }
          self.order_history={}
        
      def place_new_order(self):
          print("What you want to order here in at the Restaurent ")
          ad.show_menu_item()
          choice_user = int(input("If you want to order then select 1.YES  2.NO"))
          if choice_user == 1:
              n=int(input("How many Item do You Want to Order "))
              total_bill=0
              total_discount=0
              for i in range(n):
                  itemid = int(input("Enter the Item id here: "))
                  quan = int(input("Enter the quantity of the item: "))
                  total_bill = total_bill + ad.menu_list[itemid]['Price'] * quan
                  total_discount += ad.menu_list[itemid]['Discount']
                  ad.menu_list[itemid]['Stock'] = ad.menu_list[itemid]['Stock']-quan
                  self.order_history[itemid] = {
                      "Name": ad.menu_list[itemid]["Name"],
                      "Price": ad.menu_list[itemid]["Price"],
                      "Quantity": quan
                  }
              again_ask = input("Confirmed ?? 1 Otherwise 0 ")
              if again_ask == '1':
                  print(f"Total Discount Allowed is {total_discount} ")
                  print(f"After Deduced Discount It costs is {total_bill-total_discount} INR in total")
                  print("You're order is successfully placed...")

              elif again_ask=="0":
                  print("Your Order has Cancelled Now...")
                  self.order_history.clear()

              else :
                  print("Invalid Input !!!!!")

          elif choice_user == 2:
              print("You Selected 2 option So we Cancelled This....")

          else:
              print(" Invalid no    !!! ")


      def order_history_see(self):
          print(self.order_history)


      def update_profile(self):
          print("Update Profile Here <-------")
          email=input("Enter Your Mail-id ")
          if email in user.login_info.keys():
              print("Email Matched !!!!1")
              del user.login_info[email]


              new_email=input("Enter new  Email ")
              new_name = input("Enter new  Name ")
              new_phone_no = int(input("Enter new  Phone No "))
              new_Address = input("Enter new  Address ")
              new_password = input("Enter new  Password ")

              user.login_info[new_email] = {'Email':new_email,
                                             'Full_Name': new_name,
                                            'Phone_no': new_phone_no,
                                            'Address': new_Address,
                                            'Password': new_password,
                                                    }
              print("Profile Updated Successfully --------")
          else :
              print("Email not Registered <--- Please Try Again  ")

      def login(cls, email, password):
            
          if  email in cls.login_info.keys():
              if cls.login_info.get(email)['Password']==password:
                  print(f"logged in  *******  Successfully  ********** {cls.login_info.get(email)['Full_Name']}")
                  return True
              else:
                 print("SORRY! These are the Wrong Credentials")
                 return False
          else:
              print(f"{email} Not Registered Yet.. First Register then Come Again !!!!! ")
              return False
    
