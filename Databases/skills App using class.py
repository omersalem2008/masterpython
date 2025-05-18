#docstring
"""
this code is a simple command line application that allows the user to manage their skills
the user can add a new skill, delete a skill, and update the progress of a skill
the user can also view all their skills
the user can also quit the application all that by using class and sqlite3
"""


# Input Big Message
import sqlite3

input_message = """
What Do You Want To Do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option:
"""
#create and connect to database using sqlite3   


class Skills:
    def __init__(self):
        # Connect to or create SQLite database
        """
        Connect to or create SQLite database and create skills table if it doesn't exist
        """
        self.conn = sqlite3.connect("skills.db")
        self.cur = self.conn.cursor() # Create a cursor object to execute
        #SQL commands
        
        # Create skills table if it doesn't exist
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS skills (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                progress INTEGER DEFAULT 0
            )
        """)
        self.conn.commit()
    
    def add_skill(self, name, progress=0):
        try:
            # Insert a new row into skills table with name and progress values
            self.cur.execute("INSERT INTO skills (name, progress) VALUES (?, ?)", (name, progress))
            self.conn.commit()  # Save changes to database
            print(f"Skill {name} added successfully")
        except sqlite3.Error as e:
            print(f"Error adding skill: {e}")
    
    def show_skills(self):
        # Select all columns (*) and rows from skills table
        self.cur.execute("SELECT * FROM skills")
        skills = self.cur.fetchall()  # Fetch all rows from the result
        if skills:
            print("\nYour Skills:")
            # Display each skill's ID, name, and progress
            for skill in skills:
                print(f"ID: {skill[0]}, Name: {skill[1]}, Progress: {skill[2]}%")
        else:
            print("You have no skills yet")
    
    def delete_skill(self, identifier):
        try:
            # Check if the input is a number (ID) or text (name)
            if str(identifier).isdigit():
                # Delete row where id matches
                self.cur.execute("DELETE FROM skills WHERE id = ?", (identifier,))
            else:
                # Delete row where name matches
                self.cur.execute("DELETE FROM skills WHERE name = ?", (identifier,))
            
            if self.cur.rowcount > 0:  # Check if any row was affected
                self.conn.commit()  # Save changes to database
                print(f"Skill deleted successfully")
            else:
                print(f"No skill found with identifier: {identifier}")
        except sqlite3.Error as e:
            print(f"Error deleting skill: {e}")
    
    def update_skill(self, identifier, progress):
        try:
            # Check if the input is a number (ID) or text (name)
            if str(identifier).isdigit():
                # Update progress where id matches
                self.cur.execute("UPDATE skills SET progress = ? WHERE id = ?", (progress, identifier))
            else:
                # Update progress where name matches
                self.cur.execute("UPDATE skills SET progress = ? WHERE name = ?", (progress, identifier))
            
            if self.cur.rowcount > 0:  # Check if any row was affected
                self.conn.commit()  # Save changes to database
                print(f"Skill progress updated successfully")
            else:
                print(f"No skill found with identifier: {identifier}")
        except sqlite3.Error as e:
            print(f"Error updating skill: {e}")
    
    def __del__(self):
        # Close database connection when object is destroyed
        self.conn.close()

# Main program loop
def main():
    app = Skills()
    while True:
        choice = input(input_message).strip().lower()
        
        if choice == "s":
            app.show_skills()
        
        elif choice == "a":
            name = input("Enter skill name: ").strip()
            progress = int(input("Enter skill progress (0-100): ").strip())
            app.add_skill(name, progress)
        
        elif choice == "d":
            try:
                identifier = input("Enter skill ID or name to delete: ").strip()
                app.delete_skill(identifier)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "u":
            try:
                identifier = input("Enter skill ID or name to update: ").strip()
                progress = int(input("Enter new progress (0-100): ").strip())
                if progress < 0 or progress > 100:
                    print("Progress must be between 0 and 100")
                    continue
                app.update_skill(identifier, progress)
            except ValueError:
                print("Invalid progress value. Please enter a number between 0-100")
        
        elif choice == "q":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()

