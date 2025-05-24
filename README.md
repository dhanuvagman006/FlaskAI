<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>

  <div class="center">
    <h1>AI Redirectional Flask Server</h1>
    <img src="https://github.com/user-attachments/assets/f98e9efa-f266-4afe-8947-393ae7e0c0af" width="200" height="150" alt="Project Logo">
    <h4>This is a simple AI-based page redirection project where the server intelligently maps user queries to the most relevant webpage using either local logic or an external AI model.</h4>
  </div>

  <h2>🔍 Overview</h2>
  <p>This project is a Flask web server that uses AI or fuzzy logic to understand user queries and redirect them to the correct web page route. It can use either a lightweight offline matching algorithm or a powerful AI model via OpenRouter API.</p>

  <h2>✨ Features</h2>
  <ul>
    <li>AI-powered query redirection</li>
    <li>Supports both local fuzzy matching and remote AI via OpenRouter</li>
    <li>Modular and easy-to-extend Flask application</li>
    <li>Fallback to custom "not found" page when query is unmatched</li>
  </ul>

  <h2>🛠️ Technologies Used</h2>
  <ul>
    <li>Python</li>
    <li>Flask</li>
    <li>difflib (for fuzzy matching)</li>
    <li>Requests (for API calls)</li>
  </ul>

  <h2>📁 Project Structure</h2>
  <pre><code>.
├── app.py            # Main Flask application
├── airedirect.py     # AI/fuzzy logic redirection handler
└── README.html       # This file
  </code></pre>

  <h2>🚀 Getting Started</h2>
  <h3>1. Clone the Repository</h3>
  <pre><code>git clone https://github.com/yourusername/ai-redirector.git
cd ai-redirector</code></pre>

  <h3>2. Install Dependencies</h3>
  <pre><code>pip install flask requests</code></pre>

  <h3>3. Run the Server</h3>
  <pre><code>python app.py</code></pre>

  <h3>4. Access the App</h3>
  <p>Visit <a href="http://localhost:5000/query">http://localhost:5000/&lt;your-query&gt;</a> in your browser. For example: <code>http://localhost:5000/where can i find contact page</code></p>

  <h2>💡 Example Queries</h2>
  <ul>
    <li><code>/contact</code> → Contact Page</li>
    <li><code>/about</code> → About Page</li>
    <li><code>/reset my password</code> → Redirects to Create Account Page (via fuzzy/AI matching)</li>
  </ul>

  <h2>🔐 Using AI Mode (Optional)</h2>
  <p>To enable AI-based redirection using OpenRouter, uncomment and set the following in <code>app.py</code>:</p>
  <pre><code>api_key = "&lt;your-api-key&gt;"
model = "google/gemini-2.0-flash-001"
path_to_redirect = airedirect.ask_ai(query, api_key, model, urls_disc)</code></pre>

  <h2>📄 License</h2>
  <p>MIT License</p>

  <h2>📬 Contact</h2>
  <p>For questions or collaboration, feel free to reach out at <strong>youremail@example.com</strong>.</p>

</body>
</html>
