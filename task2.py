def main():
    # 1. INITIALIZATION: Setting the State
    # 'total' must be initialized OUTSIDE the loop so it isn't discarded on every iteration.
    total = 0.0

    print("--- DecodeLabs Expense Tracker ---")
    print("Enter your expenses one by one.")
    print("Type 'quit' to terminate the process and view your final audit.\n")

    # 2. THE CONTINUOUS AUDIT LOOP
    while True:
        # INPUT: Raw Data Feed
        user_input = input("Enter expense amount ($): ").strip()

        # THE KILL SWITCH: Sentinel Value
        if user_input.lower() == 'quit':
            break

        # 3. PROCESS & DIGITAL POKA-YOKE (Error-Proofing)
        try:
            # Transformation Mechanism: String to Float
            expense = float(user_input)
            
            # THE ACCUMULATOR PATTERN: State(new) = State(old) + Input
            total += expense
            print(f">>> Deposited: ${expense:.2f} | Running Total: ${total:.2f}")

        except ValueError:
            # Digital Barrier: Catching invalid strings safely
            print("Invalid Data! Please enter a numerical value.")

    # 4. OUTPUT: Final Display
    print("\n--- FINAL OUTPUT STREAM ---")
    print(f"FINAL TOTAL: ${total:.2f}")
    print("Session Terminated.")

# The Gatekeeper
if __name__ == "__main__":
    main()