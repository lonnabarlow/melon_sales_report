SALESPERSON_INDEX = 0
INTERNET_INDEX = 1
DORKY_LINE_LENGTH = 80
MELONS_BY_TYPE_PATH = "orders-by-type.txt"  # made the df we are working with a constant
SALES_BY_TYPE_PATH = "orders-with-sales.txt" # made the df we are working with a constant

print("*" * DORKY_LINE_LENGTH)
melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}
melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 } # moved melon_prices up top keeping lists together for readability.
total_revenue = 0

def load_melon_type(file_path):                    #made this a function with a new name that is more semantic. 
    file = open(file_path)                         # changed the variables to show what is being called in the function.
    for line in file:                              #for each loop the line will split at the | where the melons will be 
        data = line.split("|")                     # counted and incramented and moved into the melon                  
        melon_type = data[1]                       #tallies array. then close the file after all itterations. 
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count
    file.close()



def print_revenues():                               #made this a function and new variables. This function loops over
    for melon_type in melon_tallies:                #the list and the tallie array to total up the price of the melon *
        price = melon_prices[melon_type]            # the amount in the melon type list. 
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        # print("We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue))
        print(f"We sold {melon_tallies[melon_type]} {melon_type} melons at {price:.2f} each for a total of {revenue:.2f}")

load_melon_type(MELONS_BY_TYPE_PATH)
print_revenues()


print("******************************************")
#this function is going to loop through the new file and determine if the onlie sales or in person sales were greater. Using the index to determine if it was an online sale as well as adding the totals, in the end it determines that the online sales were not as great as the salesperson revenue totals. Here variables were changes and the s_file_path was made in to a constant and moved to the top of the page. 


def get_total(s_file_path):
    all_sales = open(s_file_path)
    sales = [0, 0]
    for line in all_sales:
        data1 = line.split("|")
        if data1[1] == "0":
            sales[0] += float(data1[3])
        else:
            sales[1] += float(data1[3])
    print(f"Salespeople generated ${sales[1]:.2f} in revenue.")
    print(f"Internet sales generated ${sales[0]:.2f} in revenue.")
    if sales[1] > sales[0]:
        print("Guess there's some value to those salespeople after all.")
    else:
        print("Time to fire the sales team! Online sales rule all!")

get_total(SALES_BY_TYPE_PATH)

print("******************************************")
