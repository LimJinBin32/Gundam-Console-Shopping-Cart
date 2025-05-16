cart = []  #store the items
qty = []   #store the quantity
prices = [] #store the price
yes_no = ['y', 'n']
cat1 = {1: 'GUNDAM RAISER', 2: 'Gundam SEED Astray', 3: 'Wing Gundam', 4: 'Freedom Gundam'}
cat2 = {1: 'RG GoldyMarg', 2: 'RG Gao Gai Gar', 3: 'God Gundam', 4: 'Wing Gundam'}
cat3 = {1: 'Eclipse Gundam', 2: 'Full Saber', 3: 'Unicorn Gundam', 4: 'Gundam Dynamics'}
cat4 = {1: 'Messiah Ranka Lee', 2: 'Ganesa', 3: 'Arcanadea Lumitea', 4: 'Tsubasa Kazanari'}
cat5 = {1: 'Little Ryan', 2: 'Elephant Racer', 3: 'Zoids Stylaser', 4: 'Cannon Bull'}

price = {
    1: {'GUNDAM RAISER': 315.0, 'Gundam SEED Astray': 320.0, 'Wing Gundam': 350.0, 'Freedom Gundam': 410.0},
    2: {'RG GoldyMarg': 52.0, 'RG Gao Gai Gar': 78.0, 'God Gundam': 58.0, 'Wing Gundam': 38.0},
    3: {'Eclipse Gundam': 195.0, 'Full Saber': 72.0, 'Unicorn Gundam': 52.0, 'Gundam Dynamics': 56.0},
    4: {'Messiah Ranka Lee': 95.0, 'Ganesa': 20.0, 'Arcanadea Lumitea': 75.0, 'Tsubasa Kazanari': 90.0},
    5: {'Little Ryan': 30.0, 'Elephant Racer': 17.0, 'Zoids Stylaser': 148.0, 'Cannon Bull': 35.0}
}

discounts = {
    1: 0.15,
    2: 0.10,
    3: 0.05,
    4: 0
}

def menu():
    print(f"{'No':<10} {'category':<20}{'item':<20}{'price':>15}")
    print('------------------------------------------------------------------')
    print(f"{'1':<10} {'':<20}{'GUNDAM RAISER':<21}{'$315.0':>15}")
    print(f"{'2':<10} {'Perfect Grade':<20}{'Gundam SEED Astray':<21}{'$320.0':>15}")
    print(f"{'3':<10} {'':<20}{'Wing Gundam':<21}{'$350.0':>15}")
    print(f"{'4':<10} {'':<20}{'Freedom Gundam':<21}{'$410.0':>15}")
    print('------------------------------------------------------------------')
    print(f"{'1':<10} {'':<20}{'RG GoldyMarg':<20}{'$52.0':>15}")
    print(f"{'2':<10} {'Real Grade':<20}{'RG Gao Gai Gar':<20}{'$78.0':>15}")
    print(f"{'3':<10} {'':<20}{'God Gundam':<20}{'$58.0':>15}")
    print(f"{'4':<10} {'':<20}{'Wing Gundam':<20}{'$38.0':>15}")
    print('------------------------------------------------------------------')
    print(f"{'1':<10} {'':<20}{'Eclipse Gundam':<21}{'$195.0':>15}")
    print(f"{'2':<10} {'Master Grade':<20}{'Full Saber':<20}{'$72.0':>15}")
    print(f"{'3':<10} {'':<20}{'Unicorn Gundam':<20}{'$52.0':>15}")
    print(f"{'4':<10} {'':<20}{'Gundam Dynamics':<20}{'$56.0':>15}")
    print('------------------------------------------------------------------')
    print(f"{'1':<10} {'':<20}{'Messiah Ranka Lee':<20}{'$95.0':>15}")
    print(f"{'2':<10} {'Mecha Girl':<20}{'Ganesa':<20}{'$20.0':>15}")
    print(f"{'3':<10} {'':<20}{'Arcanadea Lumitea':<20}{'$75.0':>15}")
    print(f"{'4':<10} {'':<20}{'Tsubasa Kazanari':<20}{'$90.0':>15}")
    print('------------------------------------------------------------------')
    print(f"{'1':<10} {'':<20}{'Little Ryan':<20}{'$30.0':>15}")
    print(f"{'2':<10} {'Motorized':<20}{'Elephant Racer':<20}{'$17.0':>15}")
    print(f"{'3':<10} {'':<20}{'Zoids Stylaser':<21}{'$148.0':>15}")
    print(f"{'4':<10} {'':<20}{'Cannon Bull':<20}{'$35.0':>15}")
    choices()

def choices():
    print(f'{"choice":^18}')
    print('------------------')
    print(f"1)  {'Perfect Grade'}")
    print(f"2)  {'Real Grade'}")
    print(f"3)  {'Master Grade'}")
    print(f"4)  {'Mecha Girl'}")
    print(f"5)  {'Motorized'}")
    global choice
    choice = valid_input('\nwhat category do you want (1-5): ', 1, 5)
    print('--------------------------------')
    if choice == 1:
        global cat
        cat = cat1
        print(f'{"Perfect Grade":^33}')
        print('--------------------------------')
        print(f"{'No':<5} {'item':^15}{'price':>10}")
        print(f"{'1':<5} {'GUNDAM RAISER':<20}{'$315.0':>5}")
        print(f"{'2':<5} {'Gundam SEED Astray':<20}{'$320.0':>5}")
        print(f"{'3':<5} {'Wing Gundam':<20}{'$350.0':>5}")
        print(f"{'4':<5} {'Freedom Gundam':<20}{'$410.0':>5}")
    elif choice == 2:
        cat = cat2
        print(f"{'Real Grade':^31}")
        print('--------------------------------')
        print(f"{'No':<5} {'item':^15}{'price':>10}")
        print(f"{'1':<5} {'RG GoldyMarg':<20}{'$52.0':>5}")
        print(f"{'2':<5} {'RG Gao Gai Gar':<20}{'$78.0':>5}")
        print(f"{'3':<5} {'God Gundam':<20}{'$58.0':>5}")
        print(f"{'4':<5} {'Wing Gundam':<20}{'$38.0':>5}")
    elif choice == 3:
        cat = cat3
        print(f"{'Master Grade':^32}")
        print('--------------------------------')
        print(f"{'No':<5} {'item':^15}{'price':>10}")
        print(f"{'1':<5} {'Eclipse Gundam':<20}{'$195.0':>5}")
        print(f"{'2':<5} {'Full Saber':<20}{'$72.0':>5}")
        print(f"{'3':<5} {'Unicorn Gundam':<20}{'$52.0':>5}")
        print(f"{'4':<5} {'Gundam Dynamics':<20}{'$56.0':>5}")
    elif choice == 4:
        cat = cat4
        print(f"{'Mecha Girl':^32}")
        print('--------------------------------')
        print(f"{'No':<5} {'item':^20}{'price':>5}")
        print(f"{'1':<5} {'Messiah Ranka Lee':<20}{'$95.0':>5}")
        print(f"{'2':<5} {'Ganesa':<20}{'$20.0':>5}")
        print(f"{'3':<5} {'Arcanadea Lumitea':<20}{'$75.0':>5}")
        print(f"{'4':<5} {'Tsubasa Kazanari':<20}{'$90.0':>5}")
    elif choice == 5:
        cat = cat5
        print(f"{'Motorized':^32}")
        print('--------------------------------')
        print(f"{'No':<5} {'item':^20}{'price':>5}")
        print(f"{'1':<5} {'Little Ryan':<20}{'$30.0':>5}")
        print(f"{'2':<5} {'Elephant Racer':<20}{'$17.0':>5}")
        print(f"{'3':<5} {'Zoids Stylaser':<20}{'$148.0':>5}")
        print(f"{'4':<5} {'Cannon Bull':<20}{'$35.0':>5}")
    start_shopping()

def start_shopping():
    item = valid_input('\nwhich item do you want (1-4): ', 1, 4)
    item_name = cat[item]
    print(f'You have chosen {item_name}!')
    num_of_items = valid_input('How many do you want: ', 1, 999)
    price_item = price[choice][item_name]
    cart.append(item_name)
    qty.append(num_of_items)
    prices.append(price_item)
    show_cart()
    shopping_action()

def valid_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

def show_cart():
    print(f"\n{'CART':^48}")
    print('-------------------------------------------------')
    print(f'{"No"} {"item":<19}{"qty":<4}{"unit price":^14}{"Total":^8}')
    print('-------------------------------------------------')
    for i in range(len(cart)):
        print(f'{i + 1}) {cart[i]:<20}{qty[i]:<5}{"$"}{prices[i]:<12}{"$"}{prices[i] * qty[i]:^7.2f}')

def continue_shopping():
    while True:
        repeat = input('\ndo you want to continue shopping (y/n): ').lower()
        if repeat in yes_no:
            break
        else:
            print('invalid input, please try again')
            continue
    if repeat == 'y':
        shopping_action()
    elif repeat == 'n':
        checkout()

def shopping_action():   # user action
    print(f"\n{'No':<3}| {'choice':<8}")
    print('----------------')
    print(f"{'1':<3}| {'add items'}")
    print(f"{'2':<3}| {'remove items'}")
    print(f"{'3':<3}| {'change item quantity'}")
    print(f"{'4':<3}| {'view cart'}")
    print(f"{'5':<3}| {'checkout'}")
    while True:
        more_items = valid_input("\nDo you want to add more items, remove items, change quantities, view cart, or proceed to checkout (1-5): ", 1, 5)
        if more_items == 1:  # add items
            print('')
            menu()
            break
        elif more_items == 2:  # remove items
            remove_item()
            break
        elif more_items == 3:  # change item quantity
            change_item_quantity()
            break
        elif more_items == 4:
            show_cart()
            continue_shopping()
            break
        elif more_items == 5:  # end transection
            checkout()
            break

def remove_item():
    while True:
        show_cart()
        item_to_remove = valid_input(f'\nwhich item do you want to remove (1-{len(cart)}) or (0 to cancel): ', 0, len(cart))
        if item_to_remove == 0:
            print('\nremove canceled. Nothing was changed')
            continue_shopping()
        else:
            print(f"\n{qty[item_to_remove - 1]} {cart[item_to_remove - 1]} has been removed")
            del cart[item_to_remove - 1]
            del qty[item_to_remove - 1]
            del prices[item_to_remove - 1]
            show_cart()
            while True:
                repeat_remove = input('\nDo you want to remove anymore items? (y/n): ').lower()
                if repeat_remove in yes_no:
                    break
                else:
                    print('invalid input, please try again')
                    continue
            if repeat_remove == 'y':
                if len(cart) > 0:
                    continue
                else:
                    print('\nthere are no more items left in cart')
                    print('')
                    menu()
            else:
                continue_shopping()

def change_item_quantity():
    while True:
        show_cart()
        item_to_change = valid_input(f'\nwhich item do you want to change (1-{len(cart)}) or (0 to cancel): ', 0, len(cart))
        if item_to_change == 0:
            print('\nchange quantity canceled. Nothing was changed')
            continue_shopping()
        else:
            new_qty = valid_input('enter the new quantity: ', 1, 999)
            qty[item_to_change - 1] = new_qty
            show_cart()
            while True:
                repeat_change = input('\nDo you want to change anymore items? (y/n): ').lower()
                if repeat_change in yes_no:
                    break
                else:
                    print('invalid input, please try again')
                    continue
            if repeat_change == 'y':
                continue
            else:
                continue_shopping()

def calculate_discount(membership_type, total):
    return total * discounts[membership_type]

def calculate_gst(total):
    return total * 0.08

def print_bill(total, discount, gst):
    show_cart()
    print(f"\n{'--- BILL STATEMENT ---':^38}")
    print(f"\nTotal before discount and GST: ${total:.2f}")
    print(f"Discount: {'$':>22}{discount:.2f}")
    print(f"GST: {'$':>27}{gst:.2f}")
    print(f"Final payable amount: {'$':>10}{total - discount + gst:.2f}\n")

def checkout():
    total = sum(qty[i] * prices[i] for i in range(len(cart)))
    show_cart()
    print(f"\n{'No':<3}| {'choice':<8}")
    print('----------------')
    print(f"{'1':<3}| {'Gold'}")
    print(f"{'2':<3}| {'Silver'}")
    print(f"{'3':<3}| {'Bronze'}")
    print(f"{'4':<3}| {'None'}")
    membership_type = valid_input("\nEnter your membership type (1-4): ", 1, 4)
    discount = calculate_discount(membership_type, total)
    gst = calculate_gst(total - discount)
    print_bill(total, discount, gst)
    print('Thank you for shopping with us! ')
    exit()

while True:
    menu()