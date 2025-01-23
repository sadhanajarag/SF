class Jarag:
    def __init__(self):
        # Initialize an empty dictionary to store the elements of each phase
        self.elements = {}

    def input_elements(self):
        # List of phases in the modified Waterfall Model
        stages = [
            "Communication Phase (Project Initiation, Requirement Gathering)",
            "Planning Phase (Estimating, Scheduling, Tracking, Continuous Risk Assessment)",
            "Iterative Modeling Phase (Analysis, Design)",
            "Construction Phase (Code, Early Testing, Peer Validation)",
            "Deployment Phase (Delivery, Support, Feedback, TAM)"
        ]
        # Prompt user to enter key elements for each phase
        for stage in stages:
            self.elements[stage] = input(f"Enter key elements for {stage}: ")

    def display_elements(self):
        # Display the entered key elements for each phase
        print("\n Jarag's Model Elements:")
        for stage, elements in self.elements.items():
            print(f"{stage}: {elements}")

    def completion_check(self):
        # Ask user to confirm if all criteria are met before ending the program
        all_criteria_met = input("Confirm all criteria are met before end (yes/no): ")
        while all_criteria_met.lower() != "yes":
            # If the criteria are not met, re-evaluate processes and criteria
            print("Re-evaluate processes and criteria.")
            # Prompt user to enter key elements for each phase again
            self.input_elements()
            # Display the entered key elements for each phase again
            self.display_elements()
            # Ask user again if all criteria are met before ending the program
            all_criteria_met = input("Confirm all criteria are met before end (yes/no): ")
        # If the criteria are met, proceed to end the program
        print("All criteria are met. Proceed to end.")

if __name__ == "__main__":
    # Create an instance of the Jarag class
    model = Jarag()
    # Prompt user to input elements for each phase
    model.input_elements()
    # Display the entered elements
    model.display_elements()
    # Check if all criteria are met before ending the program
    model.completion_check()
