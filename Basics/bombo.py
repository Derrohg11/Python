import matplotlib.pyplot as plt

def display_members():
    labels = ["Male Students", "Female Students"]
    students = [178, 112]

    plt.pie(students, labels=labels, autopct="%1.1f%%")
    plt.title("Club Membership")
    plt.show()

display_members()