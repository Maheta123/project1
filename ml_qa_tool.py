import json

# Load Q&A data
def load_qa_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Search for the answer to a question
def search_answer(question, qa_data):
    for item in qa_data:
        if question.lower() in item['question'].lower():
            return item['answer']
    return "Sorry, I don't have an answer to that question."

# Main interaction loop
def main():
    qa_data = load_qa_data('ml_qa.json')  # updated filename

    print("Offline ML Q&A System")
    print("Type your question (or type 'exit' to quit):")
    while True:
        user_q = input(">> ").strip()
        if user_q.lower() == 'exit':
            break
        answer = search_answer(user_q, qa_data)
        print("\nAnswer:", answer)
        print("\n")

if __name__ == '__main__':
    main()
