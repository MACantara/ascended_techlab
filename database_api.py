from flask import Blueprint, request, jsonify
from database import db
from models import User, UserSession, AppData
import sqlite3
import os
import random
import time

database_bp = Blueprint('database', __name__)

# Sample tables for the game simulation
GAME_TABLES = {
    'users': {'status': 'healthy', 'rows': 1000, 'size': '50KB'},
    'sessions': {'status': 'corrupted', 'rows': 500, 'size': '25KB'},
    'app_data': {'status': 'healthy', 'rows': 200, 'size': '10KB'},
    'logs': {'status': 'slow', 'rows': 5000, 'size': '100KB'},
    'cache': {'status': 'healthy', 'rows': 300, 'size': '15KB'}
}

@database_bp.route('/connect', methods=['POST'])
def connect():
    """Simulate database connection for the game"""
    try:
        # Check if database file exists and is accessible
        db_path = 'database.db'
        if os.path.exists(db_path):
            # Simulate connection time
            time.sleep(0.5)
            return jsonify({
                'success': True,
                'message': 'Database connected successfully',
                'connection_id': random.randint(1000, 9999)
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Database file not found'
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@database_bp.route('/query', methods=['POST'])
def execute_query():
    """Execute SQL queries for the game"""
    try:
        data = request.get_json()
        sql = data.get('sql', '')
        params = data.get('params', [])
        
        # Simulate query execution time based on complexity
        query_time = random.randint(50, 300)
        time.sleep(query_time / 1000)  # Convert to seconds
        
        # Simple query simulation
        if 'SELECT' in sql.upper():
            result = {
                'success': True,
                'data': [
                    {'id': 1, 'name': 'Sample Data 1'},
                    {'id': 2, 'name': 'Sample Data 2'}
                ],
                'execution_time': query_time,
                'rows_affected': 2
            }
        elif 'INSERT' in sql.upper() or 'UPDATE' in sql.upper() or 'DELETE' in sql.upper():
            result = {
                'success': True,
                'message': 'Query executed successfully',
                'execution_time': query_time,
                'rows_affected': random.randint(1, 10)
            }
        else:
            result = {
                'success': False,
                'error': 'Invalid SQL query'
            }
        
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@database_bp.route('/table-status', methods=['GET'])
def get_table_status():
    """Get status of all tables for the game"""
    try:
        # Return the game tables with their status
        return jsonify({
            'success': True,
            'tables': GAME_TABLES
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@database_bp.route('/repair-table', methods=['POST'])
def repair_table():
    """Repair a corrupted table in the game"""
    try:
        data = request.get_json()
        table_name = data.get('tableName', '')
        
        if table_name in GAME_TABLES:
            # Simulate repair time
            time.sleep(1)
            
            # Update table status
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

@database_bp.route('/optimize', methods=['POST'])
def optimize_database():
    """Optimize database performance for the game"""
    try:
        data = request.get_json()
        optimization_type = data.get('type', 'general')
        
        # Simulate optimization
        time.sleep(2)
        
        performance_gain = random.randint(10, 30)
        
        return jsonify({
            'success': True,
            'message': f'Database optimized using {optimization_type} optimization',
            'performance_gain': performance_gain,
            'new_query_time': max(30, random.randint(50, 200))
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@database_bp.route('/create-index', methods=['POST'])
def create_index():
    """Create database index for the game"""
    try:
        data = request.get_json()
        table_name = data.get('tableName', '')
        column_name = data.get('columnName', '')
        
        # Simulate index creation
        time.sleep(0.5)
        
        return jsonify({
            'success': True,
            'message': f'Index created on {table_name}.{column_name}',
            'performance_improvement': random.randint(15, 25)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })
