def main():

    original_price = int(input('Enter the regular price: '))
    rate = int(input('Enter the discount rate: '))

    # regular = 100
    # rate = 20
    """
    ########################################
    Code Your Program here
    ########################################
    """

    discount_amount = rate     # complete this statement to calcualte the discount amount
    final_price = {original_price} - {discount_amount%100}         # complete this statement to calculate the final price

    print(f'Regular Price: ${original_price}')
    print(f'Discount Amount: ${discount_amount}')
    print(f'Final Price: ${original_price - discount_amount}')

   ##################################################
   # Do not delete the return statement
   ##################################################
    return original_price, discount_amount, final_price


if __name__ == '__main__':
    main()
