import cohere

# 🔐 Step 1: Add your Cohere API key
co = cohere.Client("QEvOTk66ut2G0bpxp0sQwEVGhoA6hrpIdBJYPdxO")  # Replace with your actual key

# 🤖 Step 2: Function to generate the bio
def generate_bio(name, field, interests, goal):
    chat_history = []

    user_prompt = f"""Write a 3-line professional student bio.
Name: {name}
Field of Study: {field}
Interests: {interests}
Career Goal: {goal}
Keep it clear, confident, and friendly."""

    response = co.chat(
        message=user_prompt,
        chat_history=chat_history,
        temperature=0.7
    )

    return response.text.strip()

# 👤 Step 3: Collect user inputs
print("📄 Welcome to the AI Bio Generator!\n")
name = input("Enter your name: ")
field = input("Enter your field of study: ")
interests = input("Enter your interests (comma separated): ")
goal = input("Enter your career goal: ")

# 📝 Step 4: Generate and print the bio
bio = generate_bio(name, field, interests, goal)
print("\n✨ Your AI-Generated Bio:\n")
print(bio)

# 💾 Optional: Save to file
with open("your_bio.txt", "w") as file:
    file.write(bio)

print("\n✅ Bio saved to 'your_bio.txt'")
