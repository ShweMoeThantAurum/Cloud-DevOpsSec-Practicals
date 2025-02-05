class StudentUnion:
    price_for_caps = 5
    price_for_shirts = 10
    price_for_hoodies = 20

    @staticmethod
    def calculate_total_cost(quantity_of_caps, quantity_of_shirts, quantity_of_hoodies):
        """Calculate the total cost based on the numbers of caps, shirts and hoodies bought."""
        total_cost = ((StudentUnion.price_for_caps * quantity_of_caps) +
                      (StudentUnion.price_for_shirts * quantity_of_shirts) +
                      (StudentUnion.price_for_hoodies * quantity_of_hoodies))
        return total_cost
