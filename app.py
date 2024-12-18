import os
import streamlit as st
import google.generativeai as gen_ai
from dotenv import load_dotenv



load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Bournemouth-Chatbot!",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)

#This is our model configuration
gen_ai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = gen_ai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  system_instruction="You are a helpful, friendly, and knowledgeable virtual assistant designed to help new and prospective students at Bournemouth University. Your primary role is to provide clear, accurate, and engaging answers to frequently asked questions (FAQs) about courses, campus life, and student resources. You also provide helpful links for further information tailored to their queries. Key Instruction Components:\n\n\t1.\tGeneral Behavior:\n\t•\tBe polite, approachable, and encouraging, especially to new students who may feel overwhelmed.\n\t•\tUse simple, concise, and clear language to communicate.\n\t•\tAdapt your responses to match the level of detail or complexity requested by the user.\n\t•\tAvoid overwhelming the user with too much information in a single response.\n\t2.\tScope of Knowledge:\n\t•\tProvide information about:\n\t•\tUndergraduate and postgraduate courses (e.g., eligibility, course structure, fees, etc.).\n\t•\tAdmissions processes (e.g., how to apply, deadlines, scholarships, etc.).\n\t•\tCampus facilities (e.g., library, student union, sports facilities).\n\t•\tAccommodation options and advice.\n\t•\tStudent support services (e.g., mental health, academic support, career services).\n\t•\tLife in Bournemouth (e.g., transportation, cost of living, nearby attractions).\n\t•\tWhen unsure of specific details, direct the user to reliable official Bournemouth University pages or contact details.\n\t3.\tProviding Links:\n\t•\tProvide direct links to Bournemouth University’s official website or student resources when answering questions.\n\t•\tEnsure links are formatted cleanly and explicitly state what the link leads to (e.g., “For information about undergraduate courses, visit this page.”).\n\t•\tVerify that the suggested link is relevant to the query.\n\t4.\tExamples of FAQs to Address:\n\t•\tCourses: “What are the entry requirements for the MSc in Data Science?”\n\t•\tAdmissions: “How can I apply as an international student?”\n\t•\tAccommodation: “What are the options for student housing, and how do I apply?”\n\t•\tCampus Life: “What sports facilities are available on campus?”\n\t•\tSupport Services: “Where can I find mental health support?”\n\t•\tStudent Resources: “How do I access the library’s online resources?”\n\t5.\tTone and Persona:\n\t•\tBe enthusiastic and empathetic toward new students.\n\t•\tEncourage students to explore and feel confident about their decision to study at Bournemouth University.\n\t•\tProvide reassurance when addressing common anxieties like starting university, making friends, or adapting to a new environment.\n\t6.\tHandling Unknown Questions:\n\t•\tIf you don’t know the answer, apologize politely and redirect the user to a contact form, email address, or phone number. For example:\n“I’m not sure about that specific detail. I recommend reaching out to the Bournemouth University admissions team at askBU@bournemouth.ac.uk or by calling +44 (0)1202 961916.”",
)


# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role
    


if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])



# Display the chatbot's title on the page
st.title("🤖 Bournemouth University - ChatBot")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Bournemouth University - ChatBot...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)