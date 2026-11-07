class KnowledgeBaseChatbot:
    def __init__(self):
        self.knowledge_base = {
            "python": "Python is a versatile programming language used for web dev, data science, and AI.",
            "machine learning": "Machine learning focuses on building applications that learn from data and improve accuracy.",
            "internship": "An internship is a professional learning experience that offers meaningful practical work related to a student's field of study."
        }

    def get_response(self, query):
        query = query.lower()
        for key, value in self.knowledge_base.items():
            if key in query:
                return value
        return "I am sorry, I couldn't find information regarding this query in my knowledge base."

if __name__ == "__main__":
    bot = KnowledgeBaseChatbot()
    print("--- Knowledge Base Chatbot Initialized ---")
    
    test_query = "What is machine learning?"
    print(f"User Query: {test_query}")
    print("Bot Response:", bot.get_response(test_query))
