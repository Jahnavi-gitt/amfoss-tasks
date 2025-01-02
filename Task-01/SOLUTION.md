# **Command Line Operations Used**

1. **`pwd`**  
   Used to display the path of the current directory.

2. **`cd Amfoss`**  
   Used to change directory (since it was the first time it navigated to the directory named `AmFoss`).

3. **`mkdir Task-01`**  
   Command used to create a new directory.

4. **`ls`**  
   To list all the subdirectories inside `AmFoss`.

5. **`cd Task-01`**  
   Used to navigate to the subdirectory `Task-01`.

6. **`git clone https://github.com/KshitijThareja/TheCommandLineCup.git`**  
   Used to clone the repository.

7. **`mkdir codes`**  
   Creates a new subdirectory inside `Task-01`.

8. **`mkdir Part_1.txt`, `mkdir Part_2.txt`, `mkdir Part_3.txt`, `mkdir Part_4.txt`**  
   Created 4 different text files which were to store the 4 different secret codes respectively.  
   [Completed parts 1 and 2 by decoding the clue and getting the secret codes from the required codes in the spellbook]

9. **`cd TheCommandLineCup`**  
   Used to navigate into the directory which is present in the `Task-01` directory since `TheCommandLineCup` repository was cloned into it.

10. **`cd spellbook`**  
   Used to navigate into the subfolder `spellbook`.

11. **`git branch`**  
   Used to see the branch the user is currently in.

12. **`git checkout origin/defenseAgainstTheDarkArts Riddikulus.py`**  
   Used to copy the appropriate spell from a different branch `defenseAgainstTheDarkArts` into `spellbook` of the `main` branch.

13. **`git commit -m "Added Riddikulus.py from defenseAgainstTheDarkArts branch."`**  
   Used to commit the changes.  
   [The required spell file was added to the main branch and part 3 was successfully completed as we got the required secret code.]

14. **`git checkout origin/thegraveyard Priori Incantatem.py`**  
   Used to copy the appropriate spell from a different branch `thegraveyard` into `spellbook` of the `main` branch.  
   [The required spell file was added to the main branch and part 4 was successfully completed as we got the required secret code.]

15. **`git clone https://github.com/TheHuntsman4/TheFinalSpell.git`**  
   Used to clone the repository to the system.  
   Below is a screenshot of the message in the text file (which was present in `TheFinalSpell` directory).  
   ![alt text](image-1.png)

---

# **Git Terminal Commands Which Are Used to Push Work into amfoss-tasks GitHub Repository**

1. **`git add .`**  
   Adds all changes for the next commit.

2. **`git commit -m "message"`**  
   Commits the changes with a descriptive message.

3. **`git push origin main`**  
   Pushes the committed changes to the `main` branch of the remote repository.
