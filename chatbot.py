print("====== WeLcOmE tO mY ChAtBoAt=====")
print(" Type 'Bye' to exit")

def chatbot_reply(message):
        if message in ["hello", "hii", "hey"]:
                return("Bot: Hii!")

        elif message == "how are you":
            return("Bot: I am fine, Thanks!")

        elif message == "your name":
            return("Bot: My name is Python Bot")

        elif message == "thank you":
            return("Bot: You're welcome!")

        else:
            return("Bot: Sorry, I dont understand")

while True:

        message = input("You: ").lower().strip()

        if message == "bye":
            print("Bot: Goodbye!")
            break
        reply = chatbot_reply(message)
        print(reply)

        