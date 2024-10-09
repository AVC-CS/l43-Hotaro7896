def main():
    
    total = 0
    count = 0
    while count < 5:
        try:
            num = int(input(f"Enter integer {count + 1}: "))
            total += num
            count += 1
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue 
    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
