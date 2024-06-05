

def main() -> None:
    
    print("Welcome to the Tip calculator!")
    
    total_bill = input("What is the total bill? $")
    
    tip_percentage = input("How much tip do you want to give? 10, 12 or 15? ")
    
    split = input("How many people to split the bill? ")
    
    total_bill_tip = ((float(total_bill) / 100 ) * int(tip_percentage)) + float(total_bill)
    
    bill_per_person = round(total_bill_tip/int(split),2)
    
    print(f"Each person should pay {bill_per_person}$")
    
    
    
    
    
    
    return None

if __name__ == "__main__":
    
    main()
    
