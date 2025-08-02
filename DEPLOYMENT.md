# 🚀 GitHub Deployment Guide

## Step-by-Step GitHub Deployment

### 1. Initialize Git Repository

```bash
# Initialize git in your project folder
git init

# Add all files to git
git add .

# Make your first commit
git commit -m "Initial commit: Personal chatbot with Ollama and Flask"
```

### 2. Create GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click the **"+"** button → **"New repository"**
3. Name it: `ollama-chatbot`
4. Make it **Public** or **Private** (your choice)
5. **Don't** initialize with README (we already have one)
6. Click **"Create repository"**

### 3. Connect and Push to GitHub

```bash
# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/ollama-chatbot.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 4. Verify Deployment

1. Go to your GitHub repository
2. You should see all your files:
   - `app.py`
   - `templates/index.html`
   - `me.csv`
   - `requirements.txt`
   - `README.md`
   - `.gitignore`

### 5. Share Your Repository

Your chatbot is now on GitHub! Share the link:
```
https://github.com/YOUR_USERNAME/ollama-chatbot
```

## 📁 Files Being Deployed

✅ **Included in GitHub:**
- `app.py` - Main Flask application
- `templates/index.html` - Web interface
- `me.csv` - Your personal data
- `requirements.txt` - Dependencies
- `README.md` - Documentation
- `.gitignore` - Git ignore rules

❌ **Excluded from GitHub:**
- `chroma_me_db/` - Database files (auto-generated)
- `__pycache__/` - Python cache
- Virtual environment folders
- IDE files

## 🔧 Post-Deployment

### For Others to Use Your Chatbot:

1. **Clone your repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ollama-chatbot.git
   cd ollama-chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Ollama:**
   ```bash
   ollama serve
   ollama pull mxbai-embed-large
   ollama pull llama3
   ```

4. **Run the chatbot:**
   ```bash
   python app.py
   ```

## 🌐 Optional: Web Deployment

If you want to deploy to the web (not just GitHub), consider:

- **Heroku** - Easy deployment
- **Railway** - Simple hosting
- **Render** - Free hosting
- **Vercel** - Fast deployment

## 📝 Repository Customization

### Update Personal Information:
1. Edit `me.csv` with your data
2. Update `README.md` with your details
3. Commit and push changes:
   ```bash
   git add .
   git commit -m "Update personal information"
   git push
   ```

### Add Features:
1. Make your changes
2. Test locally
3. Commit and push:
   ```bash
   git add .
   git commit -m "Add new feature: [description]"
   git push
   ```

## 🎯 Best Practices

1. **Keep commits small and focused**
2. **Write clear commit messages**
3. **Update README when adding features**
4. **Test before pushing**
5. **Use meaningful branch names**

## 🆘 Troubleshooting

### If push fails:
```bash
# Pull latest changes first
git pull origin main

# Then push again
git push origin main
```

### If files are too large:
```bash
# Check what's being tracked
git status

# Remove large files if needed
git rm --cached large_file.db
```

---

🎉 **Congratulations! Your chatbot is now on GitHub!** 