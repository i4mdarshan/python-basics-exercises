stocks = open("E:\\Projects\\python-basics-exercises\\13_read_write_files\\stocks.csv", "r")
output = open("E:\\Projects\\python-basics-exercises\\13_read_write_files\\output.csv", "w")
output.write("Company_Name, PE_Ratio, PB_Ratio\n")
next(stocks)

for line in stocks:
    values = line.split(",")
    company_name = values[0]
    price = float(values[1])
    earnings_per_share = float(values[2])
    book_value = float(values[3])
    pe_ratio = round(price / earnings_per_share,2)
    pb_ratio = round(price / book_value,2)
    output.write(f"{company_name},{pe_ratio},{pb_ratio}\n")

