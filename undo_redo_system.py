# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None

    def print_stack(self):
        current = self.top
        if not current:
            print("Stack is empty.")
            return
        while current:
            print(current.data)
            current = current.next

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        return data

def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            # Push the action onto the undo stack and clear the redo stack


            print(f"Action performed: {action}")
        elif choice == "2":
            # Pop an action from the undo stack and push it onto the redo stack
            pass # delete this line
            

        elif choice == "3":
            # Pop an action from the redo stack and push it onto the undo stack
            pass # delete this line


        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            
            

        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            
            
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()