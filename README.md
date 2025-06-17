# Ascended Prototype - Escape the Lab Tech Edition

A web-based escape room game focused on technology and programming challenges.

## Prerequisites

- **Python 3.8+**
- **pip** (Python package installer)
- Modern web browser (Chrome, Firefox, Safari, Edge)

## Installation & Setup

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

### 4. Initialize Database
```bash
python app.py
```
The SQLite database will be created automatically on first run.

### 5. Run the Application
```bash
python app.py
```
The Flask development server will start on `http://127.0.0.1:5000`

## Running the Game

### Start the Application
1. Open terminal/command prompt
2. Navigate to project directory
3. Run: `python app.py`
4. Open browser to: `http://127.0.0.1:5000`

### Game Access Points
- **Main Game**: `http://127.0.0.1:5000/`
- **API Test**: `http://127.0.0.1:5000/api/data`
- **Database API**: `http://127.0.0.1:5000/api/database/table-status`

## Project Structure
```
ascended_prototype/
├── app.py                  # Main Flask application
├── models.py              # SQLAlchemy models
├── api.py                 # API routes
├── requirements.txt       # Python dependencies
├── database.db           # SQLite database (auto-created)
├── templates/
│   └── index.html         # Flask template
└── static/
    ├── css/               # Stylesheets
    └── js/                # JavaScript files
```

## Development

### Database Management
- **SQLite Browser**: Use DB Browser for SQLite to view/edit database
- **Reset Database**: Delete `database.db` and restart app
- **Migrations**: Use Flask-Migrate for schema changes

### API Endpoints
- `POST /api/database/connect` - Test database connection
- `POST /api/database/query` - Execute SQL query
- `GET /api/database/table-status` - Get table health status
- `POST /api/database/repair-table` - Repair/optimize table

## Troubleshooting

### Common Issues

1. **"Module not found" error**
   - Run: `pip install -r requirements.txt`
   - Ensure you're in the correct directory

2. **Database errors**
   - Delete `database.db` file
   - Restart the application
   - Database will be recreated automatically

3. **Port already in use**
   - Change port in app.py: `app.run(debug=True, port=5001)`
   - Or kill the process using port 5000
