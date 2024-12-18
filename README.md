This is a Streamlit-powered chatbot designed to assist new and prospective students at Bournemouth University. This chatbot answers frequently asked questions (FAQs) about courses, campus life, accommodation, and student resources. It also provides helpful links for further information tailored to user queries using Google’s Generative AI API (Gemini).

Features

	•	Interactive chatbot interface for real-time communication.
	•	Answers FAQs related to:
	•	Undergraduate and postgraduate courses (e.g., eligibility, course structure, fees).
	•	Admissions processes (e.g., how to apply, deadlines, scholarships).
	•	Campus life (e.g., facilities, sports, student support services).
	•	Accommodation options and advice.
	•	Life in Bournemouth (e.g., transportation, cost of living, attractions).
	•	Polished user experience with a conversational tone.
	•	Generates helpful links to official Bournemouth University resources.
	•	Scalable, easy-to-deploy Streamlit application.

Requirements

	•	Python 3.10 or later
	•	Virtual environment (recommended)
	•	Required Python libraries (specified in requirements.txt)

Setup Instructions

1. Clone the Repository

git clone <repository_url>
cd <repository_folder>

2. Create a Virtual Environment

python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

3. Install Dependencies

pip install -r requirements.txt

4. Add Your Google API Key

	1.	Create a .env file in the root directory.
	2.	Add your Google API key to the file:

GOOGLE_API_KEY=your_google_api_key

Run the App

Start the chatbot application with Streamlit:

streamlit run app.py

The app will launch in your default web browser at http://localhost:8501.

How It Works

	1.	Load the API Key: The app reads your Google API key from the .env file to connect with Google’s Generative AI service.
	2.	Configure the Chatbot: The chatbot uses a system instruction to establish its purpose and tone, ensuring relevant and friendly responses.
	3.	User Interaction: Users can ask questions in a chat interface, and the chatbot provides helpful answers along with relevant links.
	4.	Chat History: Conversations persist for the duration of the session.

File Structure

development folder/
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (API key)
├── README.md            # Project documentation
├── Subdirectory/        # (Optional) Additional resources
└── .venv/               # Virtual environment (not included in version control)

Customizing the Chatbot

	•	Modify the System Instruction: Edit the system_instruction in app.py to customize the chatbot’s behavior.
	•	Adjust the Model Configuration: Change parameters like temperature or max_output_tokens to tweak the chatbot’s creativity and response length.

FAQs

1. I’m seeing an import error for dotenv. What do I do?

Make sure the python-dotenv package is installed:

pip install python-dotenv

2. How do I get a Google API Key?

Follow Google’s guide to create and manage API keys.

3. Can I deploy this app online?

Yes! You can deploy the app using services like Streamlit Community Cloud, Heroku, or AWS. Make sure to add environment variables securely when deploying.

Contributing

Feel free to fork the repository and submit a pull request with new features, bug fixes, or optimizations. Contributions are welcome!

License

This project is licensed under the Apache License 2.0.
