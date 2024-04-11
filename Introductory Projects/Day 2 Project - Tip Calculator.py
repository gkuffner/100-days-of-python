
def main():
    print("Welcome to the Tip Calculator.")

    total_bill = float(input("What's the total bill? $"))
    tip = float(input("What's the tip percentage? "))
    num_people = int(input("How many people will split the bill? "))

    ind_bill = (total_bill * (1 + (tip/100)))/num_people

    print(f"Each person should pay: ${ind_bill:.2f}")

if __name__ == "__main__":
    main()
