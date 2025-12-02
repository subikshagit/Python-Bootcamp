import os

# Step 1: Define placeholder
placeholder = "[name]"

# Step 2: Read all names from file
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()  # returns list like ['Angela\n', 'Jack\n']

# Step 3: Read the base letter template
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

# Step 4: Ensure output directory exists
output_folder = "./Output/ReadyToSend"
os.makedirs(output_folder, exist_ok=True)

# Step 5: Create a customized letter for each name
for name in names:
    stripped_name = name.strip()  # removes newline character
    new_letter = letter_content.replace(placeholder, stripped_name)

    # Create a personalized file name
    output_path = f"{output_folder}/letter_for_{stripped_name}.txt"

    # Write the new letter to file
    with open(output_path, mode="w") as completed_letter:
        completed_letter.write(new_letter)

    print(f"✅ Letter created for {stripped_name}: {output_path}")
