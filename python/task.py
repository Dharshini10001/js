# fruits=[]
# price=[]
# total=0
# apple=200
# orange=180
# grapes=120
# palm=80
# melon=50
# watermelon=40
# one_kg=180
# half_kg=150
# quater=120
# enter=input("if you want to buy fruits text yes other print no!")
# for i in (enter==yes):
#     fruit=int(input("Enter the fruits:"))
#     fruits.append(fruit)
# else:
#     print("if you want exit press 1:")
# i=0
# while i < fruits.length:
#     total=fruits[]+1
# print(total)

fruits = []
price = []
total = 0

# Prices for fruits
fruit_prices = {
    "apple": 200,
    "orange": 180,
    "grapes": 120,
    "palm": 80,
    "melon": 50,
    "watermelon": 40
}

enter = input("If you want to buy fruits, type 'yes'. Otherwise, type 'no': ").lower()

if enter == "yes":
    while True:
        fruit = input("Enter the fruit you want to buy (type 'exit' to finish): ").lower()
        
        if fruit == "exit":
            break
        
        
        if fruit in fruit_prices:
            quantity = float(input("Enter the quantity in kgs: "))
            fruits.append(fruit)
            price.append(fruit_prices[fruit] * quantity)
        else:
            print(f"{fruit} is not available. Please choose from the available fruits.")
else:
    print("You chose not to buy any fruits.")

# Calculate total
for i in range(len(price)):
    total += price[i]

print(f"The total cost of the fruits is: {total}")
