# Question 1 - Develop an application that asks the user for her/his name, and then greets them with their name.
class Greeting:
    @staticmethod
    def do_greeting(username):
        """Greet the user."""
        return f"Hello, {username}."