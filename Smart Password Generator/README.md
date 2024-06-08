## Smart Password Generator 
This code provides a functional GUI-based smart password generator that combines user input with randomness to create a password. 
### Explanation of Key Components
**Imports and Library Setup:**
- tkinter, customtkinter: Libraries for creating the GUI.
- random, string: Libraries for generating the password.<br/>
**Function gen:**
- Collects user input for first name, last name, birth date, and year.
- Creates a password using random selections from the input data and a predefined list of special characters.
- Displays the generated password.<br/>
**UI Setup:**
- Main window (app) is configured with size and title.
- Three frames (frame1, frame2, frame3) organize input fields and the result label.
- Labels and entry fields gather user data.
- A button triggers the gen function.
- The generated password is displayed in a label within frame3.<br/>
**Error Handling:**
- The try-except block in gen handles potential errors, such as empty input fields or incorrect input formats.
