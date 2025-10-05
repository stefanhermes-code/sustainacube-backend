# 🌱 SustainaCube Streamlit Apps

Streamlit-based applications for sustainability research and analysis.

## 📁 Directory Structure

```
SustainaCube_Development/
├── app_corporate.py             # Corporate Streamlit application
├── app.py                       # Internal Streamlit application
├── Corporate Users.csv          # User authentication data
├── requirements.txt             # Python dependencies
├── main.py                      # FastAPI backend (optional)
├── users.csv                    # API user data (optional)
└── README.md                    # This file
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Corporate App
```bash
streamlit run app_corporate.py
```

### 3. Run Internal App
```bash
streamlit run app.py
```

## 💡 Features

- **User Authentication**: Email/password login system
- **Document Analysis**: PDF and document processing
- **AI-Powered Responses**: OpenAI integration for sustainability insights
- **Usage Tracking**: Monitor user activity and costs
- **API Integration**: Optional FastAPI backend for data management

## 🔧 Configuration

### Environment Variables
Create a `.env` file with:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### User Management
- **Corporate Users**: Edit `Corporate Users.csv` to add/remove users
- **API Users**: Use `create_users_csv.py` to generate hashed passwords

## 📊 Applications

### Corporate App (`app_corporate.py`)
- Corporate user interface
- Enhanced authentication
- Usage analytics
- Professional reporting

### Internal App (`app.py`)
- Internal team interface
- Advanced document processing
- Research tools
- Collaboration features

## 🔄 API Integration (Optional)

The FastAPI backend (`main.py`) provides:
- User authentication endpoints
- Usage logging and analytics
- Data management APIs
- Health monitoring

## 🛠️ Troubleshooting

### Common Issues
- **Authentication errors**: Check user credentials in CSV files
- **API errors**: Verify OpenAI API key in environment variables
- **Import errors**: Ensure all dependencies are installed

### Deployment
- **Streamlit Cloud**: Upload files and configure secrets
- **Local Development**: Use `streamlit run` commands
- **API Backend**: Deploy separately to cloud platforms

## 📞 Support

For issues or questions, check the console output and ensure all dependencies are properly installed.
