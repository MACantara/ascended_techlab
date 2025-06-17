import json
import random
from datetime import datetime

def handler(event, context):
    path = event.get('path', '')
    method = event.get('httpMethod', 'GET')
    
    # Game tables simulation
    GAME_TABLES = {
        'users': {'status': 'healthy', 'rows': 1000, 'size': '50KB'},
        'sessions': {'status': 'corrupted', 'rows': 500, 'size': '25KB'},
        'app_data': {'status': 'healthy', 'rows': 200, 'size': '10KB'},
        'logs': {'status': 'slow', 'rows': 5000, 'size': '100KB'},
        'cache': {'status': 'healthy', 'rows': 300, 'size': '15KB'}
    }
    
    if path == '/api/database/table-status':
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'success': True, 'tables': GAME_TABLES})
        }
    
    elif path == '/api/database/connect' and method == 'POST':
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'success': True,
                'message': 'Database connected successfully',
                'connection_id': random.randint(1000, 9999)
            })
        }
    
    # Default response
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'message': 'API endpoint working'})
    }
