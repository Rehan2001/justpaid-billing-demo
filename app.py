from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
from datetime import datetime
import io
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

def process_invoices(df):
    today = datetime.today()
    results = []
    for _, row in df.iterrows():
        due = pd.to_datetime(row['due_date'])
        days_overdue = (today - due).days
        status = 'Paid' if str(row.get('paid','')).lower()=='yes' else (
                 'Overdue' if days_overdue > 0 else 'Upcoming')
        amount = float(str(row['amount']).replace('$','').replace(',',''))
        results.append({
            'customer': row['customer'],
            'amount': amount,
            'due_date': due.strftime('%b %d, %Y'),
            'status': status,
            'days_overdue': max(0, days_overdue) if status=='Overdue' else 0
        })
    return results

@app.route('/api/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400
    df = pd.read_csv(io.StringIO(file.read().decode('utf-8')))
    invoices = process_invoices(df)
    total = sum(i['amount'] for i in invoices)
    overdue = sum(i['amount'] for i in invoices if i['status']=='Overdue')
    paid = sum(i['amount'] for i in invoices if i['status']=='Paid')
    return jsonify({'invoices': invoices,
                    'summary': {'total': total, 'overdue': overdue, 'paid': paid,
                                'count': len(invoices)}})

@app.route('/api/health')
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)