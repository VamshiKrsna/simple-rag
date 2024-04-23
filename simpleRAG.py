import streamlit as st
import google.generativeai as genai
import PyPDF2

# Function that extracts text from the pdf.
def text_extractor(pdf_path):
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def main():

    pdf_path = "attention_is_all_you_need.pdf"

    # Loading Model :
    model_name = "gemini-1.5-pro-latest"
    genai.configure(api_key="YOUR_GEMINI_API_KEY")

    # Streamlit UI
    st.title("RAG System for 'Attention Is ALL You NEED' Paper")
    question = st.text_input("Ask your question")

    if st.button("Generate Answers"):
        if question:
            text = text_extractor(pdf_path)

            context = text + "\n\n" + question

            ai = genai.GenerativeModel(model_name=model_name)

            response = ai.generate_content(context)

            st.subheader("Question:")
            st.write(question)
            st.subheader("Answer:")
            st.write(response.text)
        else:
            st.warning("Please enter your question.")

if __name__ == "__main__":
    main()
