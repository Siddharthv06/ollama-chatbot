# 🤖 Siddharth's Personal Chatbot

A web-based chatbot that answers questions about Siddharth Vishwakarma using Ollama and LangChain.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)
![Ollama](https://img.shields.io/badge/Ollama-AI-orange.svg)

## 🌟 Features

- **Web Interface**: Clean black & white theme
- **Real-time Chat**: Instant question and answer
- **Mobile Responsive**: Works on all devices
- **AI-Powered**: Uses Ollama and LangChain
- **Vector Search**: Smart document retrieval

## 📁 Project Structure

```
ollama-chatbot/
├── app.py              # Flask web server
├── templates/
│   └── index.html      # Chatbot web interface
├── me.csv              # Personal data
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+** installed
2. **Ollama** installed and running
3. **Required models** downloaded

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ollama-chatbot.git
   cd ollama-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Ollama**
   ```bash
   # Start Ollama service
   ollama serve
   
   # Download required models (in another terminal)
   ollama pull mxbai-embed-large
   ollama pull llama3
   ```

4. **Run the chatbot**
   ```bash
   python app.py
   ```

5. **Open in browser**
   Go to: `http://localhost:5000`

## 📝 Data Format

Update `me.csv` with your information:

```csv
paragraph
"My name is Siddharth Vishwakarma. I live in Nashik and love working on AI projects."
"I studied Computer Science and enjoy ASCII art and programming."
"I am currently in third year at Sandip University pursuing Computer Science Engineering."
"I am 19 years old."
"My hobbies are outdoor sports and coding."
```

## 🔧 Configuration

### Models
- **Embedding Model**: `mxbai-embed-large`
- **Language Model**: `llama3`
- **Retrieval**: Top 6 most relevant documents

### Customization
- Edit `templates/index.html` for UI changes
- Modify `app.py` for backend logic
- Update `me.csv` for personal data

## 🌐 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main chat interface |
| `/ask` | POST | Ask a question |
| `/health` | GET | Health check |

### Example API Usage
```bash
curl -X POST http://localhost:5000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What are my hobbies?"}'
```

## 🛠️ Troubleshooting

### Common Issues

1. **"ModuleNotFoundError"**
   ```bash
   pip install -r requirements.txt
   ```

2. **"Ollama service not running"**
   ```bash
   ollama serve
   ```

3. **"Model not found"**
   ```bash
   ollama pull mxbai-embed-large
   ollama pull llama3
   ```

4. **"CSV file not found"**
   - Ensure `me.csv` exists in project directory
   - Check it has a "paragraph" column

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
For production, use a WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Siddharth Vishwakarma**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai) for AI models
- [LangChain](https://langchain.com) for AI framework
- [Flask](https://flask.palletsprojects.com) for web framework

---

⭐ **Star this repository if you found it helpful!** 