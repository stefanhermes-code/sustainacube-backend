# 🌱 SustainaCube RAG System

A RAG-based ExpertCenter for sustainability research, following the PU ExpertCenter pattern.

## 📁 Directory Structure

```
SustainaCube_RAG/
├── sustainacube_rag.py          # Main RAG application
├── ms_forms_integration.py      # MS Forms webhook handler
├── requirements.txt             # Python dependencies
├── run_sustainacube.bat         # Easy startup script
├── env_example.txt              # Environment variables template
└── README.md                    # This file
└── USER_MANUAL.md               # Full user manual
```

## 🚀 Quick Start

### 1. Set up Environment
1. Copy `env_example.txt` to `.env`
2. Add your OpenAI API key to the `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the System
Double-click `run_sustainacube.bat` or run:
```bash
streamlit run sustainacube_rag.py
```

### 4. Process Documents
1. Open the web interface (http://localhost:8501)
2. Click "🔄 Process Documents" in the sidebar
3. Wait for all 602 documents to be processed

## 🔄 Workflow (Following PU ExpertCenter Pattern)

1. **MS Forms** → User submits sustainability questions
2. **SustainaCube** → Processes question through RAG system
3. **Outlook** → Sends formatted email response with sources

## 💡 Features

- **Document Processing**: Handles PDFs, Word docs, text files
- **Vector Search**: Semantic search through 602+ documents
- **AI Answers**: GPT-4 powered responses with citations
- **MS Forms Integration**: Webhook endpoint for form submissions
- **Email Responses**: Professional HTML email formatting
- **Source Citations**: Shows which documents were used

## 🔧 Configuration

### MS Forms Integration
To set up MS Forms integration:
1. Create a webhook in MS Forms
2. Point it to: `http://your-server:5000/webhook/sustainacube`
3. Configure email settings in `.env`

### Email Configuration
Add to your `.env` file:
```
OUTLOOK_EMAIL=your_email@domain.com
OUTLOOK_PASSWORD=your_app_password
```

## 📊 Cost Estimate

- **OpenAI API**: ~$5-10/month (based on usage)
- **Everything else**: Free (local processing)

## 🧪 Testing

Try these sample questions:
- "What are the CO2 savings from PU foam recycling in Thailand?"
- "Compare EPR frameworks across different countries"
- "What are the latest chemical recycling methods?"
- "How much CO2 can be saved through mattress recycling?"

## 📚 Document Types Supported

- PDF files (.pdf)
- Word documents (.docx)
- Text files (.txt)

## 🔍 How It Works

1. **Document Processing**: Extracts text from all supported files
2. **Chunking**: Splits text into manageable chunks for better retrieval
3. **Embedding**: Creates vector embeddings using OpenAI
4. **Storage**: Stores embeddings in ChromaDB vector database
5. **Retrieval**: Finds relevant chunks for user questions
6. **Generation**: Uses GPT-4 to generate comprehensive answers
7. **Response**: Formats and delivers answers via email

## 🛠️ Troubleshooting

### Common Issues
- **"No documents found"**: Run "Process Documents" first
- **API errors**: Check your OpenAI API key in `.env`
- **Email not sending**: Verify Outlook credentials in `.env`

### Logs
Check the console output for detailed error messages and processing status.

## 📞 Support

For issues or questions, check the console output and ensure all dependencies are properly installed.
