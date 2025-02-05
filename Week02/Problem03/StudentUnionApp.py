from StudentUnion import StudentUnion

number_of_caps = int(input("Enter the number of caps you bought: "))
number_of_shirts = int(input("Enter the number of shirts you bought: "))
number_of_hoodies = int(input("Enter the number of hoodies you bought: "))

print("Total cost:", StudentUnion.calculate_total_cost(number_of_caps, number_of_shirts, number_of_hoodies))