# ScriptGPT

## Description

The Python script is engineered to synthesize video titles, scripts, and conduct research utilizing a
singular user-provided prompt. It harnesses the Streamlit framework to render a web interface, and leverages
the Langchain framework for manipulation of LLMs. The script integrates the Wikipedia API for research capabilities
and employs OpenAI's LLM for semantic text generations.

Upon receiving a prompt from the user, the script adeptly processes it,
 engaging OpenAI's LLM to dynamically generate content. 
 Simultaneously, it utilizes the Wikipedia API for rigorous research, 
 subsequently amalgamating the output into a meticulously structured format. 
 A notable feature of this script is its  memory management system,
which archives previous user prompts, thereby enhancing contextual relevance and continuity in content generation.

## Features
- **Language Model Integration**: Utilizes OpenAI's language models for advanced text processing.
- **Wikipedia API Wrapper**: Integrates a Wikipedia API for accessing and incorporating Wikipedia data.
- **Memory management**: Allows users to review past prompts.

## Installation
1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Get OpenAI API key:
   ```bash
   export OPENAI_API_KEY='your_api_key_here'
   ```

## Usage
- Run the application:
  ```bash
  streamlit run app.py
  ```
- Enter the text you wish to process in the provided input field.

## Dependencies
- Listed in `requirements.txt`.
