import string
import secrets

def main():
    print("--- Enterprise Random Password Generator ---")
    
    while True:
        # Phase 1: Environmental Requirements and Validation
        user_input = input("\nEnter target password length (or 'quit' to exit): ").strip()
        
        if user_input.lower() == 'quit':
            print("Session Terminated.")
            break
            
        try:
            length = int(user_input)
            if length <= 0:
                print("Invalid Data! Length must be greater than 0.")
                continue
                
            # Phase 2: Building the backend transformation engine
            # Standardizing character classification
            char_pool = string.ascii_letters + string.digits
            
            # Utilizing cryptographically secure randomness and O(N) memory allocation
            password_list = [secrets.choice(char_pool) for _ in range(length)]
            secure_password = "".join(password_list)
            
            # Phase 3: Output
            print(f">>> Generated Credential: {secure_password}")
            
        except ValueError:
            print("Invalid Data! Please enter a numerical integer.")

if __name__ == "__main__":
    main()