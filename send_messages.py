import json
import asyncio
import os
from datetime import datetime
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
SESSION_NAME = os.getenv('SESSION_NAME', 'my_session')
MESSAGE_DELAY = float(os.getenv('MESSAGE_DELAY', '1.5'))


async def send_messages():
    with open('messages.json', 'r', encoding='utf-8') as f:
        messages_data = json.load(f)

    report = []
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

    try:
        await client.start()
        print(f"Logged in successfully. Starting to send {len(messages_data)} messages...")

        for idx, message_info in enumerate(messages_data, 1):
            user_id = message_info['user_id']
            text = message_info['text']

            try:
                await client.send_message(user_id, text)
                print(f"[{idx}/{len(messages_data)}] ✓ Sent to {user_id}")

                report.append({
                    "user_id": user_id,
                    "status": "success"
                })

            except Exception as e:
                print(f"[{idx}/{len(messages_data)}] ✗ Failed to send to {user_id}: {str(e)}")

                report.append({
                    "user_id": user_id,
                    "status": "failed"
                })

            if idx < len(messages_data):
                await asyncio.sleep(MESSAGE_DELAY)

        print(f"\nCompleted! Successfully sent: {sum(1 for r in report if r['status'] == 'success')}/{len(messages_data)}")

    finally:
        await client.disconnect()

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_filename = f'report_{timestamp}.json'

    with open(report_filename, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"Report saved to {report_filename}")


if __name__ == '__main__':
    asyncio.run(send_messages())
