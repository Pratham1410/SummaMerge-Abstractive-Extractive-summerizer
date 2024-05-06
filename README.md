

<h1 align="center">Text Summarization Application 📝</h1>

<p align="center">
  <img src="https://img.shields.io/badge/python-v3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License">
</p>

<p align="center">
This project is a versatile text summarization tool that combines cutting-edge natural language processing techniques to generate concise summaries from textual content. With a user-friendly graphical interface built using Tkinter, the application caters to a variety of user needs, ranging from summarizing documents to extracting information from web pages.
</p>

## 🚀 Features

- **Abstractive Summarization**: Uses the state-of-the-art T5 model to generate summaries that capture the essence of the text.
- **Extractive Summarization**: Implements NLTK and spaCy to highlight the most significant sentences directly from the text.
- **Graphical User Interface**: Provides a simple and intuitive interface for interacting with the application, designed with Tkinter.
- **File and Web Text Summarization**: Enables users to load text from files or directly from URLs for summarization.
- **Text-to-Speech**: Enhances accessibility by reading summaries aloud.
- **Comparison Tool**: Allows users to compare the effectiveness of different summarization techniques.
- **Responsive Design**: The layout is optimized for ease of use, with well-organized navigation and display areas.

## 🛠 Getting Started

### Prerequisites

This application requires Python 3.7 or later. Download Python [here](https://www.python.org/downloads/). You will also need the following packages:

- `torch`
- `transformers`
- `tkinter`
- `nltk`
- `spaCy`
- `BeautifulSoup`
- `pyttsx3`
- `pyaudio`

### 🔧 Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate
```
### Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 🖥️ Running the Application

Start the application with:

```bash
python SUMMERIZERAPP.py
```

### 📘 How to Use
- **Home Tab**: Type or paste text into the input box to summarize.
- **File Tab**: Open and summarize text files from your computer.
- **URL Tab**: Enter a URL to fetch text from the web and summarize.
- **Comparer Tab**: See how different summarization methods perform side-by-side.

