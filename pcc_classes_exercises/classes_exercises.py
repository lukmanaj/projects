'''                     Classes Exercises: from the chapter in Eric Matthes' Python Crash Course,
                                    Part of Arewa Data Science Curriculum
''' 
'''
9-1. Restaurant: Make a class called Restaurant. The __init__() method for 
Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of 
information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
'''

class Restaurant:
    '''A simple attempt to model a Restaurant'''
    def __init__(self,restaurant_name,cuisine_type):
        '''Initialise restaurant name and cuisine type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''Print restaurant name and cuisine type'''
        print(f'{self.restaurant_name} offers the best {self.cuisine_type} meals')

    def open_restaurant(self):
        '''Indicate that restaurant is open'''
        print(f'{self.restaurant_name} is open for business')
    


a_restaurant = Restaurant('Sweeties','Italian')
print(a_restaurant.restaurant_name)
print(a_restaurant.cuisine_type)
print(a_restaurant.describe_restaurant())
print(a_restaurant.open_restaurant())





'''9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
different instances from the class, and call describe_restaurant() for each 
instance.'''
rest_one = Restaurant('Diamonds','Hausa')
rest_two = Restaurant('Freebies','Yoruba')
rest_three = Restaurant('Limine','Russian')
print(rest_one.describe_restaurant())
print(rest_two.describe_restaurant())
print(rest_three.describe_restaurant())





'''9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored 
in a user profile. Make a method called describe_user() that prints a summary 
of the user’s information. Make another method called greet_user() that prints 
a personalized greeting to the user.
Create several instances representing different users, and call both methods 
for each user.
'''
class User:
    '''Attempt to model a user profile'''
    def __init__(self,first_name,last_name,age,city,profession):
        '''initialize user first and last name and other info'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.profession = profession

    def describe_user(self):
        '''Print user profile'''
        print(f'{self.first_name} {self.last_name}, a {self.age} years old {self.profession} lives in {self.city}')

    def greet_user(self):
        '''Print a personalised greeting to specific user'''
        print(f'Good day {self.first_name} {self.last_name}, happy to see you with us')


user_one = User('Lukman','Aliyu',28,'Kaduna','Pharmacist')
user_two = User('Aminu','Jibrin',27,'Zaria','Engineer')
user_three = User('Hassana',"Aya",22,'Samaru','Student')

print(f'Greeting user one: {user_one.describe_user()}')
user_one.greet_user()

user_two.describe_user()
user_two.greet_user()

user_three.describe_user()
user_three.greet_user()


"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 162). 
Add an attribute called number_served with a default value of 0. Create an 
instance called restaurant from this class. Print the number of customers the 
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number 
of customers that have been served. Call this method with a new number and 
print the value again.
Add a method called increment_number_served() that lets you increment 
the number of customers who’ve been served. Call this method with any num￾ber you like that could represent how many customers were served in, say, a 
day of business."""
class Restaurant_v2:
    '''Another attempt to model a restaurant'''
    def __init__(self,restaurant_name,cuisine_type):
        '''Initialise restaurant name and cuisine type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''Print restaurant name and cuisine type'''
        print(f'{self.restaurant_name} offers the best {self.cuisine_type} meals and has served {self.number_served} customers so far')

    def open_restaurant(self):
        '''Indicate that restaurant is open'''
        print(f'{self.restaurant_name} is open for business')
    
    def set_number_served(self,num):
        '''Set the number of customers that have been served'''
        if num >= self.number_served:
            self.number_served = num
        else:
            print('We only move forward!!')

    def increment_number_served(self,add):
        '''Increase the number of customers served by an amount'''
        if add > 0:
            self.number_served += add
        else:
            print('Customers served can\'t be reduced')

restaurant = Restaurant_v2('Innies','Chinese')
restaurant.number_served   # 0
restaurant.number_served = 5
restaurant.describe_restaurant()  # 5 customers
restaurant.set_number_served(20)
restaurant.describe_restaurant()  # change reflected
restaurant.increment_number_served(5)
restaurant.describe_restaurant() # 5 added 



"""
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 162). Write a method called increment_login
_attempts() that increments the value of login_attempts by 1. Write another 
method called reset_login_attempts() that resets the value of login_attempts
to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented 
properly, and then call reset_login_attempts(). Print login_attempts again to 
make sure it was reset to 0.
"""
class User_v2:
    '''Attempt to model a user profile'''
    def __init__(self,first_name,last_name,age,city,profession):
        '''initialize user first and last name and other info'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.profession = profession
        self.login_attempts = 0


    def describe_user(self):
        '''Print user profile'''
        print(f'{self.first_name} {self.last_name}, a {self.age} years old {self.profession} lives in {self.city}')

    def greet_user(self):
        '''Print a personalised greeting to specific user'''
        print(f'Good day {self.first_name} {self.last_name}, happy to see you with us')
    
    def increment_login_attempts(self):
        '''Increase the number of login attempts by 1'''
        self.login_attempts += 1

    def reset_login_attempts(self):
        '''Reset the login_attempts back to zero'''
        self.login_attempts = 0

user_ex = User_v2('Sam','Wells',30,'Paris','Loafer')
for i in range(10):
    user_ex.increment_login_attempts()
print(user_ex.login_attempts) 
user_ex.reset_login_attempts()
print(user_ex.login_attempts)  # back to zero

'''
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write 
a class called IceCreamStand that inherits from the Restaurant class you wrote 
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of 
the class will work; just pick the one you like better. Add an attribute called 
flavors that stores a list of ice cream flavors. Write a method that displays 
these flavors. Create an instance of IceCreamStand, and call this method.'''

class IceCreamStand(Restaurant):
    '''An sttempt to model an icecream stand, a kind of restaurant'''
    def __init__(self, restaurant_name, cuisine_type):
        '''Initialise attributes of parent class(Restaurant) then those specific to an IceCreamStand'''
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry','vanilla']
    def display_flavors(self):
        '''Display the flavors available in the IceCreamStand'''
        print(f'\nWe have the follwing icecream flavors in stock')
        for item in self.flavors:
            print(f'-{item}')

rose = IceCreamStand('Biggies','French')
rose.display_flavors()

''''9-7. Admin: An administrator is a special kind of user. Write a class called 
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) 
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list 
of strings like "can add post", "can delete post", "can ban user", and so on. 
Write a method called show_privileges() that lists the administrator’s set of 
privileges. Create an instance of Admin, and call your method.'''




class Admin(User):
    '''An attempt to model an Admin, a special kind of User'''
    def __init__(self,first_name,last_name,age,city,profession):
        super().__init__(first_name,last_name,age,city,profession)
        self.privileges = ['can add post','can delete post','can ban user']
    def show_privileges(self):
        '''Display the privileges an admin possesses'''
        print(f'\n This admin has the following privileges')
        for item in self.privileges:
            print(f'-{item}')

his_admin = Admin('Lukman','Aliyu',28,'Kaduna','Pharmacist')
his_admin.show_privileges()

'''9-8. Privileges: Write a separate Privileges class. The class should have one 
attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
Move the show_privileges() method to this class. Make a Privileges instance 
as an attribute in the Admin class. Create a new instance of Admin and use your 
method to show its privileges.'''

class Privileges:
    '''An attempt to model the privileges an admin user profile has'''
    def __init__(self,privileges = ['can add post','can delete post','can ban user']):
        self.privileges = privileges
    def show_privileges(self):
        '''Display the privileges an admin possesses'''
        if self.privileges:
            print(f'\n This admin has the following privileges')
            for item in self.privileges:
                print(f'-{item}')
        else: 
            print(f'This user has no privileges')


class Admin_v2(User):
    '''An attempt to model an Admin, a special kind of User'''
    def __init__(self,first_name,last_name,age,city,profession):
        super().__init__(first_name,last_name,age,city,profession)
        self.privileges = Privileges()

admin_01 = Admin_v2('Lukman','Aliyu',20,'Kano','Analyst')
admin_01.privileges.show_privileges()  # worked

'''9-9. Battery Upgrade: Use the final version of electric_car.py from this section. 
Add a method to the Battery class called upgrade_battery(). This method 
should check the battery size and set the capacity to 100 if it isn’t already. 
Make an electric car with a default battery size, call get_range() once, and 
then call get_range() a second time after upgrading the battery. You should 
see an increase in the car’s range.
'''

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        '''Upgrade the battery if there's a need'''
        if self.battery_size == 75:
            self.battery_size = 100
            print('Battery has been upgraded to 100KWh')
        else:
            print('Battery already upgraded')


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\nChecking the range after upgrading battery:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


"""
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a mod￾ule. Make a separate file that imports Restaurant. Make a Restaurant instance, 
and call one of Restaurant’s methods to show that the import statement is working properly.
"""
# Solution in imported_restaurant.py



"""
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). 
Store the classes User, Privileges, and Admin in one module. Create a sepa￾rate file, make an Admin instance, and call show_privileges() to show that 
everything is working correctly.
"""
# Solution in imported_admin_ex.py

"""
9-12. Multiple Modules: Store the User class in one module, and store the 
Privileges and Admin classes in a separate module. In a separate file, create 
an Admin instance and call show_privileges() to show that everything is still 
