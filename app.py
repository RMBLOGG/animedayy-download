from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Configuration
API_BASE = "https://www.mediafire.com/file/gfe8fxvs2owh71h/𝘼𝙣𝙞𝙢𝙚𝘿𝙖𝙮𝙮.apk/file"

APP_CONFIG = {
    'name': '𝘼𝙣𝙞𝙢𝙚𝘿𝙖𝙮𝙮',
    'version': '2.0.0',
    'package': 'com.animestreaming.app',
    'download_url': 'https://www.mediafire.com/file/s75epqwe9pebllr/𝘼𝙣𝙞𝙢𝙚𝘿𝙖𝙮𝙮.apk/file',  # Ganti dengan link APK Anda
    'file_size': '10 MB',
    'min_android': '5.0',
    'api_endpoints': {
        'schedule': f'{API_BASE}/api/schedule',
        'ongoing': f'{API_BASE}/api/ongoing',
        'completed': f'{API_BASE}/api/completed',
        'anime_detail': f'{API_BASE}/api/anime/',
        'search': f'{API_BASE}/api/search'
    }
}

def get_app_stats():
    """Get real-time stats from API"""
    try:
        # Get ongoing anime count
        ongoing_response = requests.get(f"{API_BASE}/api/ongoing?page=1", timeout=5)
        ongoing_data = ongoing_response.json()
        ongoing_count = len(ongoing_data.get('data', {}).get('animeList', []))
        
        # Get schedule data
        schedule_response = requests.get(f"{API_BASE}/api/schedule", timeout=5)
        schedule_data = schedule_response.json()
        schedule_count = len(schedule_data.get('data', []))
        
        return {
            'ongoing_anime': ongoing_count if ongoing_count > 0 else '50+',
            'total_anime': '1000+',
            'daily_updates': schedule_count if schedule_count > 0 else '7',
            'servers': '4+'
        }
    except:
        # Fallback values if API fails
        return {
            'ongoing_anime': '50+',
            'total_anime': '1000+',
            'daily_updates': '7',
            'servers': '4+'
        }

@app.route('/')
def index():
    stats = get_app_stats()
    return render_template('index.html', config=APP_CONFIG, stats=stats)

@app.route('/api/info')
def app_info():
    stats = get_app_stats()
    return jsonify({
        **APP_CONFIG,
        'stats': stats
    })

if __name__ == '__main__':
    app.run(debug=True)
