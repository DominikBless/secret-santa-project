"""
Secret Santa Assignment Program

This script allows users to enter a list of participants for a Secret Santa gift exchange. 
Participants can have specified partners (who they cannot be assigned to), and there's 
also functionality for pre-determining some of the gift assignments. The program ensures 
that each participant is assigned another participant to whom they can give a gift, 
adhering to the rules of not being assigned to themselves or their partners.
"""

import random
import os
import sys

def is_assignment_possible(participants):
    """
    Check if a valid Secret Santa assignment is possible.
    A valid assignment is possible if there's at least one participant who
    can be assigned a Secret Santa without breaking the rules.

    Args:
    participants (dict): Dictionary of participants and their partners.

    Returns:
    bool: True if an assignment is possible, False otherwise.
    """
    for santa in participants:
        possible_recipients = [name for name in participants if name != santa and name != participants[santa]]
        if not possible_recipients:
            return False
    return True


def input_participants():
    """
    Input and validate participant names and their partners, along with pre-determined assignments.

    Returns:
    tuple: A tuple containing two dictionaries, one for participants and their partners, 
           and the other for pre-determined assignments.
    """
    participants = {}
    displayed_pairs = set()  # Set to keep track of displayed pairs
    pre_assigned = {}  # Dictionary to store pre-determined assignments
    in_pre_assignment = False  # Flag to track if we are in pre-assignment mode

    while True:
        print("\nEnter the names of participants. Type 'done' when finished.")
        participants.clear()
        displayed_pairs.clear()

        while True:
            name = input("Enter participant's name: ").strip()
            if not name:
                print("Please enter a valid name.")
                continue
            if name == '1':
                if in_pre_assignment:
                    # Exit pre-assignment mode if '1' is entered again
                    in_pre_assignment = False
                    break
                else:
                    # Enter pre-assignment mode 
                    in_pre_assignment = True
                    print("Enter pre-determined assignments (format: Giver > Receiver). Type '1' to finish.")
                    while True:
                        assignment = input().strip()
                        if assignment == '1':
                            break
                        if '>' in assignment:
                            try:
                                giver, receiver = assignment.split('>')
                                pre_assigned[giver.strip()] = receiver.strip()
                            except ValueError:
                                print("Invalid format for assignment. Please use 'Giver > Receiver'.")
                        os.system('cls' if os.name == 'nt' else 'clear')
                    continue

            if name.lower() == 'done':
                break
            partner = input(f"Enter {name}'s partner's name (or 'none' if no partner): ").strip()
            partner = None if partner.lower() == 'none' else partner
            if partner == name:
                print("A participant cannot be their own partner. Please re-enter.")
                continue
            participants[name] = partner
            if partner and partner not in participants:
                participants[partner] = name  # Add partner as a participant as well
            
        print("\nParticipants and their partners:")
        for participant, partner in participants.items():
            if partner and (participant, partner) not in displayed_pairs and (partner, participant) not in displayed_pairs:
                print(f"{participant} - {partner}")
                displayed_pairs.add((participant, partner))  # Mark this pair as displayed
            elif not partner:
                print(f"{participant} - None")

        confirm = input("\nIs the above information correct? (yes/no): ").strip().lower()
        if confirm == 'yes':
            break

    return participants, pre_assigned

def assign_secret_santa(participants, pre_assigned):
    """
    Assign each participant a Secret Santa, considering pre-determined assignments.

    Args:
    participants (dict): Dictionary of participants and their partners.
    pre_assigned (dict): Dictionary of pre-determined Santa assignments.

    Returns:
    dict: A dictionary of assigned Santas or None if an assignment is not possible.
    """
    all_names = list(participants.keys())
    valid_assignments = {name: [n for n in all_names if n != name and n != participants[name]] for name in all_names}

    assignments = pre_assigned.copy()  # Start with pre-assigned participants
    all_names = [name for name in all_names if name not in pre_assigned]  # Exclude pre-assigned givers

    while all_names:
        santa = random.choice(all_names)
        possible_recipients = valid_assignments[santa]

        # Exclude already assigned giftees
        possible_recipients = [recipient for recipient in possible_recipients if recipient not in assignments.values()]
        
        if not possible_recipients:
            return None  # Restart the process if stuck

        giftee = random.choice(possible_recipients)
        assignments[santa] = giftee
        all_names.remove(santa)

        # Remove giftee from other's possible recipients
        for name in valid_assignments:
            if giftee in valid_assignments[name]:
                valid_assignments[name].remove(giftee)

    return assignments

def reveal_assignments(assignment):
    """
    Reveal the Secret Santa assignments to participants in a 'secret' way.

    Args:
    assignment (dict): Dictionary containing the Secret Santa assignments.
    """
    print("\nDo you want to see the assignments? (yes/no): ")
    if input().strip().lower() != 'yes':
        print("Exiting program.")
        sys.exit()

    for santa in assignment:
        input(f"\n{santa}: (Press Enter to reveal)")
        print(f"-> {assignment[santa]}")
        input("Press Enter to continue...")

        # Clear the console screen to hide the previous assignment
        os.system('cls' if os.name == 'nt' else 'clear')

def get_yes_or_no_input(prompt):
    """
    Get a yes or no input from the user.

    Args:
    prompt (str): The prompt to display to the user.

    Returns:
    bool: True if the user inputs 'yes' or 'y', False otherwise.
    """
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Invalid response. Please answer with 'yes', 'no', 'y', or 'n'.")

def check_assignments_again(assignment):
    """
    Allow participants to check their Secret Santa assignments again.

    Args:
    assignment (dict): Dictionary containing the Secret Santa assignments.
    """
    while True:
        if not get_yes_or_no_input("Does anyone need to see their assignment again? (yes/no): "):
            print("Exiting program.")
            break

        santa = input("Enter your name to see your Secret Santa assignment: ").strip()
        if santa in assignment:
            print(f"Your Secret Santa assignment is: {assignment[santa]}")
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Name not found. Please try again.")
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')


# Main Program
participants, pre_assigned = input_participants()

while not is_assignment_possible(participants):
    print("\nAssignment is not possible with the current set of participants.")
    choice = input("Do you want to re-enter participant information? (yes/no): ").strip().lower()
    if choice != 'yes':
        print("Exiting program.")
        exit(0)
    participants = input_participants()

assignment = None
while not assignment:
    assignment = assign_secret_santa(participants, pre_assigned)

reveal_assignments(assignment)
check_assignments_again(assignment)