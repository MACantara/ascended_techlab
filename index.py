from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# For Vercel deployment, we'll use a simple in-memory storage instead of SQLite
# In production, you'd want to use a proper database service like PlanetScale or Supabase

# Simple data storage (in production, use a proper database)
GAME_DATA = {
    'users': [],
    'sessions': [],
    'app_data': []
}

GAME_TABLES = {
    'users': {'status': 'healthy', 'rows': 1000, 'size': '50KB'},
    'sessions': {'status': 'corrupted', 'rows': 500, 'size': '25KB'},
    'app_data': {'status': 'healthy', 'rows': 200, 'size': '10KB'},
    'logs': {'status': 'slow', 'rows': 5000, 'size': '100KB'},
    'cache': {'status': 'healthy', 'rows': 300, 'size': '15KB'}
}

@app.route('/')
def index():
    return render_template('index.html')

# API Routes
@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    if request.method == 'POST':
        try:
            data = request.get_json()
            return jsonify({'status': 'success', 'data': data})
        except Exception as e:
            return jsonify({'status': 'error', 'error': str(e)}), 500
    else:
        return jsonify({'data': 'example', 'timestamp': datetime.now().isoformat()})

# Database API Routes
@app.route('/api/database/connect', methods=['POST'])
def database_connect():
    return jsonify({
        'success': True,
        'message': 'Database connected successfully',
        'connection_id': 1234
    })

@app.route('/api/database/query', methods=['POST'])
def database_query():
    try:
        data = request.get_json()
        sql = data.get('sql', '')
        
        if 'SELECT' in sql.upper():
            result = {
                'success': True,
                'data': [
                    {'id': 1, 'name': 'Sample Data 1'},
                    {'id': 2, 'name': 'Sample Data 2'}
                ],
                'execution_time': 120,
                'rows_affected': 2
            }
        else:
            result = {
                'success': True,
                'message': 'Query executed successfully',
                'execution_time': 80,
                'rows_affected': 1
            }
        
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/api/database/table-status', methods=['GET'])
def get_table_status():
    return jsonify({
        'success': True,
        'tables': GAME_TABLES
    })

@app.route('/api/database/repair-table', methods=['POST'])
def repair_table():
    try:
        data = request.get_json()
        table_name = data.get('tableName', '')
        
        if table_name in GAME_TABLES:
            GAME_TABLES[table_name]['status'] = 'healthy'
            return jsonify({
                'success': True,
                'message': f'Table {table_name} repaired successfully',
                'table_status': GAME_TABLES[table_name]
            })
        else:
            return jsonify({
                'success': False,
                'error': f'Table {table_name} not found'
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/api/database/optimize', methods=['POST'])
def optimize_database():
    return jsonify({
        'success': True,
        'message': 'Database optimized successfully',
        'performance_gain': 25,
        'new_query_time': 50
    })

@app.route('/api/database/create-index', methods=['POST'])
def create_index():
    data = request.get_json()
    table_name = data.get('tableName', '')
    column_name = data.get('columnName', '')
    
    return jsonify({
        'success': True,
        'message': f'Index created on {table_name}.{column_name}',
        'performance_improvement': 20
    })

# Export for Vercel
def handler(event, context):
    return app(event, context)

if __name__ == '__main__':
    app.run(debug=True)
