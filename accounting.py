SALESPERSON_INDEX = 0
INTERNET_INDEX = 1
DORKY_LINE_LENGTH = 80
MELONS_BY_TYPE_PATH = "orders-by-type.txt"
SALES_BY_TYPE_PATH = "orders-with-sales.txt"

print("*" * DORKY_LINE_LENGTH)
melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}
melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
total_revenue = 0

def load_melon_type(file_path):
    file = open(file_path)
    for line in file:
        data = line.split("|")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count
    file.close()



def print_revenues():
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        # print("We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue))
        print(f"We sold {melon_tallies[melon_type]} {melon_type} melons at {price:.2f} each for a total of {revenue:.2f}")

load_melon_type(MELONS_BY_TYPE_PATH)
print_revenues()


print("******************************************")


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
