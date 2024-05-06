

Text Summarization Application 📝


This project is a versatile text summarization tool that combines cutting-edge natural language processing techniques to generate concise summaries from textual content. With a user-friendly graphical interface built using Tkinter, the application caters to a variety of user needs, ranging from summarizing documents to extracting information from web pages.

🚀 Features
Abstractive Summarization: Uses the state-of-the-art T5 model to generate summaries that capture the essence of the text.
Extractive Summarization: Implements NLTK and spaCy to highlight the most significant sentences directly from the text.
Graphical User Interface: Provides a simple and intuitive interface for interacting with the application, designed with Tkinter.
File and Web Text Summarization: Enables users to load text from files or directly from URLs for summarization.
Text-to-Speech: Enhances accessibility by reading summaries aloud.
Comparison Tool: Allows users to compare the effectiveness of different summarization techniques.
Responsive Design: The layout is optimized for ease of use, with well-organized navigation and display areas.
🛠 Getting Started
Prerequisites
This application requires Python 3.7 or later. Download Python here. You will also need the following packages:

torch
transformers
tkinter
nltk
spaCy
BeautifulSoup
pyttsx3
pyaudio

🔧 Installation
Clone the repository and set up a virtual environment:


git clone https://github.com/Pratham1410/SummaMerge-Abstractive-Extractive-summerizer.git
cd SummaMerge-Abstractive-Extractive-summerizer
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required dependencies:
pip install -r requirements.txt

## Post-Installation

After installing the required packages, some additional resources need to be downloaded for the NLTK package. Run the following commands in your Python environment to download these resources:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

🖥️ Running the Application
Start the application with:
python SUMMERIZERAPP.py

📘 How to Use
Home Tab: Type or paste text into the input box to summarize.
File Tab: Open and summarize text files from your computer.
URL Tab: Enter a URL to fetch text from the web and summarize.
Comparer Tab: See how different summarization methods perform side-by-side.
🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check issues page. You can also take a look at the contributing guide.

📜 License
Distributed under the MIT License. See LICENSE for more information.
