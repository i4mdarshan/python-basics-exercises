# Exercise
# 1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total
#    area using python and print it
field_length = 92
field_width = 48.8
area = field_length * field_width
print("Area of the football field is " + str(area))

# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
#    and you gave shopkeeper 20 dollar.
#    Find out using python, how many dollars is the shopkeeper going to give you back?
packets = 9
per_packet_price = 1.49
amt_paid = 20
print("Amount returned : ", amt_paid - (packets * per_packet_price))


# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet
#    is its length. If tiles cost 500 rs per square feet, how much will be the total
#    cost to replace all tiles. Calculate and print the cost using python
#    Hint: Use power operator (**) to find area of a square
bathroom_length = 5.5
per_sq_ft = 500
area = bathroom_length ** 2
print("Total Area of bathroom: ",area)
print("Total cost: ",area * per_sq_ft)

# 4. Print binary representation of number 17
num = 17
def toBinary(num):
    if num >= 1:
        toBinary(num // 2)
    print(num % 2, end = '')
toBinary(num)