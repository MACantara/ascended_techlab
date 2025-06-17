# Ascended Prototype - Escape the Lab Tech Edition

A web-based escape room game focused on technology and programming challenges.

## Prerequisites

- **Python 3.8+**
- **pip** (Python package installer)
- Modern web browser (Chrome, Firefox, Safari, Edge)

## Local Development

### 1. Install Python
- Download from [https://python.org/downloads/](https://python.org/downloads/)
- Ensure Python is added to PATH during installation

### 2. Clone/Download Project
- Place this project in `c:\ascended_prototype\`

### 3. Install Dependencies
```bash
cd c:\ascended_prototype
pip install -r requirements.txt
```

### 4. Run Local Development Server
```bash
python app.py
```
The Flask development server will start on `http://127.0.0.1:5000`

## Deployment to Vercel

### Prerequisites
- Node.js installed
- Vercel CLI: `npm install -g vercel`
- Vercel account

### Deployment Steps

1. **Prepare for deployment**:
   ```bash
   cd c:\ascended_prototype
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy**:
   ```bash
   vercel --prod
   ```

4. **Follow prompts**:
   - Set up and deploy: `Y`
   - Which scope: Select your account
   - Link to existing project: `N` (first time)
   - Project name: `ascended-prototype`
   - Directory: `./`

### Live Demo
Once deployed, your game will be available at: `https://ascended-prototype.vercel.app`

## Project Structure
```
ascended_prototype/
├── api/
│   └── index.py           # Serverless API for Vercel
├── app.py                 # Local development server
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel configuration
├── static/
│   ├── index.html        # Main game file
│   ├── css/              # Stylesheets
│   ├── js/               # JavaScript files
│   └── data/             # Game data
└── templates/            # Flask templates (local dev)
```

## API Endpoints
- `GET /api/data` - Get game data
- `POST /api/database/connect` - Test database connection
- `GET /api/database/table-status` - Get table status
- `POST /api/database/repair-table` - Repair table simulation

## Troubleshooting

### Local Development Issues

1. **"Module not found" error**
   - Run: `pip install -r requirements.txt`
   - Ensure you're in the correct directory

2. **Port already in use**
   - Change port in app.py: `app.run(debug=True, port=5001)`

### Deployment Issues

1. **Vercel deployment fails**
   - Check `vercel.json` is in root directory
   - Ensure `api/index.py` exists
   - Check Vercel function logs in dashboard

2. **JavaScript errors**
   - Check browser console for syntax errors
   - Ensure all file paths are correct
   - Verify ES6 module imports are properly formatted

3. **API not working**
   - Check Vercel function logs
   - Verify API routes in `/api/index.py`
   - Test endpoints individually
