# Exception Handling
# Write a program that includes try-except blocks to handle exceptions gracefully.

# File Handling
# Read from and Write to a file using file handling operations.

try:
    # Reading from the file
    with open("tester.txt", "r") as file:
        content = file.read()
        print("File content:", content)

except FileNotFoundError:
    print("The file does not exist or cannot be found.")

except Exception as e:
    print("An error occurred:", e)

try:
    # Appending/Writing to the file
    with open("tester.txt", "a") as file:
        file.write("Test Write ")
        print("Data written successfully.")

except FileNotFoundError:
    print("The file does not exist or cannot be found.")


except Exception as e:
    print("An error occurred:", e)
