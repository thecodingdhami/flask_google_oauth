# 🔑 Flask Google OAuth

A simple Flask application that demonstrates how to implement **Google OAuth 2.0 authentication**.  
This project helps you integrate Google login into your Flask apps securely and easily.

---

## 🚀 Features

- Google OAuth 2.0 authentication  
- User login with Google account  
- Fetch and display user profile information (name, email, profile picture)  
- Flask session management  
- Beginner-friendly and easy to extend  

---

## 📂 Project Structure

```
flask_google_oauth/
│── app.py              # Main Flask application
│── client_secret.json  # Google OAuth credentials (keep this private!)
│── templates/          # HTML templates
│    ├── index.html
│    ├── profile.html
│── static/             # Static files (CSS, JS, images)
│── venv/               # Virtual environment (not uploaded to GitHub)
│── requirements.txt    # Project dependencies
│── README.md           # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/flask_google_oauth.git
cd flask_google_oauth
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Google OAuth Credentials
1. Go to [Google Cloud Console](https://console.cloud.google.com/).  
2. Create a new project (or select an existing one).  
3. Navigate to **APIs & Services → Credentials**.  
4. Create **OAuth 2.0 Client ID** for a **Web Application**.  
5. Add the following Authorized redirect URI:  
   ```
   http://127.0.0.1:5000/callback
   ```
6. Download the `client_secret.json` file and place it in the project root.

### 5️⃣ Run the Application
```bash
python app.py
```
Now open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## ✅ Example Usage

1. Open the app in the browser.  
2. Click **"Login with Google"**.  
3. Authenticate with your Google account.  
4. See your profile information displayed on the profile page.  

---

## 📦 Dependencies

```txt
Flask==3.0.3
google-auth==2.34.0
google-auth-oauthlib==1.2.1
google-auth-httplib2==0.2.0
requests==2.32.3
```

Install via:
```bash
pip install -r requirements.txt
```

---

## 🛡️ Security Notes

- Never upload your `client_secret.json` to GitHub.  
- Use environment variables or secret managers in production.  
- Restrict OAuth credentials in Google Cloud Console to trusted domains only.  

---

## 🤝 Contributing

Pull requests are welcome!  
If you’d like to improve this project, please fork the repo and submit a PR.

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
