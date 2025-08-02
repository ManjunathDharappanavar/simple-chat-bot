# Simple AI Command-Line Chatbot

<div align="center">
  <img src="https://via.placeholder.com/200x120/2E86AB/FFFFFF?text=AI+CHATBOT" alt="Chatbot Logo" width="200"/>
  
  <p align="center">
    <strong>A lightweight Python-based command-line chatbot powered by OpenRouter API integration for conversational AI interactions</strong>
  </p>

  <p align="center">
    <a href="#features"><strong>Features</strong></a> •
    <a href="#installation"><strong>Installation</strong></a> •
    <a href="#usage"><strong>Usage</strong></a> •
    <a href="#configuration"><strong>Configuration</strong></a> •
    <a href="#contributing"><strong>Contributing</strong></a>
  </p>

  <p align="center">
    <img src="https://img.shields.io/github/license/ManjunathDharappanavar/simple-chat-bot" alt="License"/>
    <img src="https://img.shields.io/github/stars/ManjunathDharappanavar/simple-chat-bot" alt="Stars"/>
    <img src="https://img.shields.io/github/forks/ManjunathDharappanavar/simple-chat-bot" alt="Forks"/>
    <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version"/>
  </p>
</div>

---

## 📋 Table of Contents

<details>
<summary>Click to expand</summary>

- [About](#about)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Error Handling](#error-handling)
- [Security Considerations](#security-considerations)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

</details>

---

## 🚀 About

This command-line chatbot application provides direct access to advanced AI language models through the OpenRouter API platform. The application serves as a practical demonstration of API integration patterns while delivering functional conversational AI capabilities in a terminal environment.

The chatbot implementation emphasizes simplicity and reliability, utilizing the httpx library for robust HTTP communication and implementing comprehensive error handling to ensure stable operation across different network conditions. The application supports multiple AI models through OpenRouter's unified API interface, with GPT-3.5 Turbo configured as the default conversational engine.

### Project Architecture

The application follows a streamlined architecture pattern with direct API communication, stateless conversation handling, and minimal dependency requirements. This design approach ensures easy deployment, maintenance, and modification while providing reliable access to sophisticated AI language processing capabilities.

---

## ✨ Features

<table>
<tr>
<td width="50%">

### Core Functionality
- **AI-Powered Conversations**: Direct integration with OpenAI GPT-3.5 Turbo model
- **Real-time Communication**: Instant responses through OpenRouter API
- **Command-Line Interface**: Lightweight terminal-based interaction
- **Session Management**: Continuous conversation until user exit
- **Error Recovery**: Comprehensive exception handling for stable operation

</td>
<td width="50%">

### Technical Features
- **HTTP Client Integration**: Modern httpx library for reliable API communication
- **Model Flexibility**: Support for multiple AI models through configuration
- **Authentication Security**: API key-based authentication with proper headers
- **Response Processing**: JSON parsing with structured message extraction
- **Exit Control**: Clean session termination with user command

</td>
</tr>
</table>

---

## 📋 Prerequisites

### System Requirements

The application requires Python 3.7 or higher with pip package management capabilities. An active internet connection is necessary for API communication with OpenRouter services.

<div align="center">

| Component | Requirement | Purpose |
|-----------|-------------|---------|
| Python | 3.7+ | Runtime environment |
| pip | Latest version | Package management |
| Internet Connection | Required | API communication |
| OpenRouter API Key | Valid subscription | Service authentication |

</div>

### API Prerequisites

Users must obtain a valid OpenRouter API key through registration at the OpenRouter platform. The service provides access to multiple AI models including OpenAI GPT variants, with pricing based on usage patterns and model selection.

---

## 📦 Installation

### Environment Setup

```bash
# Clone the repository
git clone https://github.com/ManjunathDharappanavar/simple-chat-bot.git

# Navigate to project directory
cd simple-chat-bot

# Install required dependencies
pip install httpx

# Alternative: Install from requirements.txt (if available)
pip install -r requirements.txt
```

### Virtual Environment Configuration

```bash
# Create virtual environment (recommended)
python -m venv chatbot-env

# Activate virtual environment
# Windows
chatbot-env\Scripts\activate

# macOS/Linux
source chatbot-env/bin/activate

# Install dependencies in virtual environment
pip install httpx
```

### Dependency Information

The application utilizes httpx as the primary HTTP client library, chosen for its modern asynchronous capabilities and robust error handling features. This library provides superior performance compared to traditional requests libraries while maintaining simple integration patterns.

---

## ⚙️ Configuration

### API Key Setup

Replace the placeholder API key in the source code with your valid OpenRouter API key obtained from the platform dashboard.

```python
# Update this line with your actual API key
API_KEY = "your-actual-openrouter-api-key"
```

### HTTP Headers Configuration

The application requires specific HTTP headers for proper API communication with OpenRouter services.

```python
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "your-github-account",  # Replace with your GitHub URL
    "X-Title": "Command Line Chatbot"
}
```

### Model Selection Options

The chatbot supports multiple AI models through the OpenRouter platform. Users can modify the model parameter to access different language processing capabilities.

<div align="center">

| Model | Identifier | Capabilities |
|-------|------------|--------------|
| GPT-3.5 Turbo | openai/gpt-3.5-turbo | Fast, efficient conversations |
| GPT-4 | openai/gpt-4 | Advanced reasoning capabilities |
| Claude | anthropic/claude-v1 | Enhanced conversation quality |

</div>

---

## 🚀 Usage

### Basic Operation

Launch the chatbot application from the command line and engage in natural language conversations with the AI system.

```bash
# Execute the chatbot application
python chatbot.py

# Example interaction session
Chatbot: Hello! Type 'exit' to quit.
You: What is artificial intelligence?
Chatbot: Artificial intelligence (AI) refers to the simulation of human intelligence...
You: exit
Chatbot: Goodbye!
```

### Conversation Flow

The application maintains a continuous conversation loop until the user enters the exit command. Each user input is processed through the OpenRouter API, with responses displayed immediately in the terminal interface.

### Session Management

Users can conduct extended conversations with context maintained through individual message exchanges. The current implementation processes each message independently, with conversation history managed by the underlying AI model's capabilities rather than application-level state management.

---

## 🔧 API Reference

### Core Functions

#### Main Chatbot Function

<details>
<summary>chatbot()</summary>

**Description**: Primary application function managing user interaction loop and API communication

**Functionality**: Initializes conversation session, processes user input, communicates with OpenRouter API, displays AI responses, and handles session termination

**Implementation Pattern**:
```python
def chatbot():
    print("Chatbot: Hello! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        # API communication and response handling
```

</details>

### API Communication Structure

The application constructs JSON payloads for OpenRouter API communication with specific model selection and message formatting requirements.

```python
payload = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": user_input}
    ]
}
```

### Response Processing

API responses undergo JSON parsing to extract the AI-generated message content from the structured response format provided by OpenRouter services.

```python
response = httpx.post(BASE_URL, headers=HEADERS, json=payload)
result = response.json()
message = result["choices"][0]["message"]["content"]
```

---

## 🛡️ Error Handling

### Exception Management

The application implements comprehensive exception handling to manage network connectivity issues, API service availability problems, authentication failures, and response parsing errors.

```python
try:
    response = httpx.post(BASE_URL, headers=HEADERS, json=payload)
    result = response.json()
    message = result["choices"][0]["message"]["content"]
    print("Chatbot:", message)
except Exception as e:
    print("❌ Error:", e)
```

### Common Error Scenarios

Network connectivity problems may result in connection timeout errors or DNS resolution failures. API service issues can include rate limiting, service unavailability, or maintenance periods. Authentication problems typically manifest as HTTP 401 unauthorized responses when API keys are invalid or expired.

### Troubleshooting Guidelines

Users experiencing consistent errors should verify their API key validity, confirm internet connectivity, check OpenRouter service status, and ensure proper configuration of HTTP headers and referrer information.

---

## 🔒 Security Considerations

### API Key Protection

API keys represent sensitive authentication credentials and should never be committed to version control systems or shared in public repositories. Users should implement environment variable storage or secure configuration file management for production deployments.

### Environment Variable Implementation

```bash
# Set environment variable for API key
export OPENROUTER_API_KEY="your-actual-api-key"

# Update Python code to use environment variable
import os
API_KEY = os.getenv("OPENROUTER_API_KEY")
```

### Network Security

The application communicates exclusively through HTTPS protocols to ensure encrypted data transmission. All API communications utilize secure SSL/TLS connections provided by the OpenRouter platform infrastructure.

---

## 🤝 Contributing

### Development Guidelines

Contributors can enhance the application through additional model support, conversation history management, configuration file implementation, and user interface improvements. All contributions should maintain the existing simplicity and reliability standards while extending functionality appropriately.

### Enhancement Opportunities

Potential improvements include implementing conversation history persistence, adding support for conversation context management, developing configuration file management systems, creating user preference storage, and implementing advanced error recovery mechanisms.

### Code Quality Standards

Maintain consistent Python coding standards with proper documentation, implement comprehensive error handling for all external communications, ensure secure handling of authentication credentials, and follow established patterns for API integration and response processing.


---

## 📞 Contact

<div align="center">

**Project Developer**: Manjunath Dharappanavar

<p>
  <a href="mailto:manjunathdharappanavar@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
  </a>
  <a href="https://github.com/ManjunathDharappanavar">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
  <a href="https://linkedin.com/in/manjunathdharappanavar">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
</p>

**Repository**: [https://github.com/ManjunathDharappanavar/simple-chat-bot](https://github.com/ManjunathDharappanavar/simple-chat-bot)

</div>

---

## 🙏 Acknowledgments

<div align="center">

Recognition to the open-source development community and AI service providers who have enabled accessible artificial intelligence integration for developers and researchers.

</div>

**Technical Resources**: OpenRouter platform for providing unified API access to multiple AI language models, httpx development team for reliable HTTP client library development, and Python community for comprehensive documentation and development resources.

**Service Providers**: OpenAI for advanced language model development and research contributions to conversational AI capabilities.

---

<div align="center">

### ⭐ Project Support

Demonstrate your interest in AI development by starring this repository.

<p>
  <a href="https://github.com/ManjunathDharappanavar/simple-chat-bot">
    <img src="https://img.shields.io/badge/⭐-Star%20Repository-2E86AB?style=for-the-badge" alt="Star Repository"/>
  </a>
</p>

</div>

---

<div align="center">
  <sub>Developed to demonstrate practical AI integration using modern Python development practices</sub>
</div>
