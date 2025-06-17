from flask import Blueprint, request, jsonify
from models import User, UserSession, AppData
from database import db
from datetime import datetime
import json

api_bp = Blueprint('api', __name__)

@api_bp.route('/database/connect', methods=['POST'])
def database_connect():
    try:
        # Test database connection
        db.session.execute('SELECT 1')
        return jsonify({
            'success': True,
            'message': 'Database connected successfully',
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api_bp.route('/database/query', methods=['POST'])
def database_query():
    try:
        data = request.get_json()
        sql = data.get('sql', '')
        params = data.get('params', [])
        
        # Execute query (be careful with raw SQL in production)
        result = db.session.execute(sql, params)
        
        # Check if it's a SELECT query
        if sql.strip().upper().startswith('SELECT'):
            rows = result.fetchall()
            return jsonify({
                'success': True,
                'data': [dict(row) for row in rows],
                'rowCount': len(rows)
            })
        else:
            db.session.commit()
            return jsonify({
                'success': True,
                'affectedRows': result.rowcount,
                'message': 'Query executed successfully'
            })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api_bp.route('/database/table-status', methods=['GET'])
def table_status():
    try:
        tables = ['user', 'user_session', 'app_data']
        status = {}
        
        for table in tables:
            try:
                # Check table exists and is accessible
                result = db.session.execute(f'SELECT COUNT(*) FROM {table}')
                count = result.scalar()
                status[table] = {
                    'status': 'healthy',
                    'row_count': count,
                    'last_check': datetime.now().isoformat()
                }
            except Exception:
                status[table] = {
                    'status': 'corrupted',
                    'last_check': datetime.now().isoformat()
                }
        
        return jsonify({
            'success': True,
            'tables': status
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api_bp.route('/database/repair-table', methods=['POST'])
def repair_table():
    try:
        data = request.get_json()
        table_name = data.get('tableName', '')
        
        # Allowed tables for security
        allowed_tables = ['user', 'user_session', 'app_data']
        if table_name not in allowed_tables:
            return jsonify({
                'success': False,
                'error': f"Table '{table_name}' is not allowed for repair"
            }), 400
        
        # Simulate repair (SQLite doesn't have REPAIR TABLE)
        # In SQLite, you might use VACUUM or REINDEX
        db.session.execute('VACUUM')
        db.session.commit()
        
        return jsonify({
            'success': True,
            'tableName': table_name,
            'status': 'OK',
            'message': f"Table {table_name} repair completed"
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api_bp.route('/data', methods=['GET', 'POST'])
def api_data():
    if request.method == 'POST':
        try:
            data = request.get_json()
            # Process data here
            return jsonify({'status': 'success', 'data': data})
        except Exception as e:
            return jsonify({'status': 'error', 'error': str(e)}), 500
    else:
        return jsonify({'data': 'example', 'timestamp': datetime.now().isoformat()})
