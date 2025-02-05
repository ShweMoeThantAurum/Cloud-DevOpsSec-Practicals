class WeightCalculator:
    @staticmethod
    def calculate_weight(age, height):
        """Calculate weight based on age and height."""
        recommended_weight = (height - 100 + age % 10) * 0.90
        return recommended_weight

