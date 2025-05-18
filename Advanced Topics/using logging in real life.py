import logging
from getpass import getpass # getpass is used to hide the password 
# while typing same as input() but input() will show the password
# --------------------------------------------------

# Configure logging
logging.basicConfig(
    filename="python/learning/Advanced Topics/login_attempts.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s -%(name)s - %(funcName)s() - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger("login_system") # Get a logger with the name "login_system"
# --------------------------------------------------

def validate_password(): 
    """
    Attempts to validate a user's password. The user is given a maximum of 4
    attempts to enter the correct password. If the user enters the correct
    password, the function logs a success message and returns True. If the user
    enters an incorrect password, the function logs a warning message and prints
    an error message. If the user exceeds the maximum number of attempts, the
    function logs an error message and returns False. If the user interrupts the
    process with Ctrl+C, the function logs a warning message and returns False.
    """
    correct_password = "secret123" # This is the correct password
    max_attempts = 4 # Maximum number of attempts
    attempts = 0 # Number of attempts made

    while attempts < max_attempts: # Loop until the maximum number of attempts is reached
        try:
            # getpass hides the password while typing same as input() but input() 
            # will show the password
            password = getpass("Enter your password: ") 
            attempts += 1
            
            if password == correct_password:
                logger.info("Login successful") # Log a success message
                print("Welcome! Login successful.") 
                return True # Exit the loop and function
            else:
                remaining = max_attempts - attempts # Remaining attempts
                logger.warning(f"Failed login attempt {attempts}/{max_attempts}")
                if remaining > 0: # If there are remaining attempts
                    print(f"Incorrect password. {remaining} attempts remaining.") 
                
        except KeyboardInterrupt: # Handle Ctrl+C interruption by the user
            logger.warning("Login process interrupted by user")
            print("\nLogin process cancelled.")
            return False 

    logger.error("Account locked - Maximum login attempts exceeded") # Log an error message 
    # after exceeding the maximum number of attempts
    print("Maximum login attempts exceeded. Account is locked.") 
    return False # Exit the loop and function

if __name__ == "__main__": # Main function to run the script
    # This block will only run if the script is executed directly
    print("Login System") # Print the title
    print("-" * 20) # Print a separator
    validate_password() # Call the validate_password function