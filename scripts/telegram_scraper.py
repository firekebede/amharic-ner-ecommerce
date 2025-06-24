from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import json
import os

# Replace with your own credentials
api_id = 29970930  # e.g., 123456
api_hash = '0eb7aedcd5659359f54dd43d12f2359a'
phone_number = '+251936642440'  # e.g., +2519XXXXXXXX

# Define the channel you want to scrape (public)
channel_username = '@ZemenExpress', '@nevacomputer', '@meneshayeofficial', '@ethio_brand_collection', '@Leyueqa'


client = TelegramClient('amharic_ner', api_id, api_hash)

async def fetch_messages(channel_username, limit=100):
    await client.start(phone_number)
    entity = await client.get_entity(channel_username)
    messages = await client(GetHistoryRequest(
        peer=entity,
        limit=limit,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0
    ))

    result = []
    for msg in messages.messages:
        if msg.message:  # Only fetch text messages
            result.append({
                "sender_id": msg.from_id.user_id if msg.from_id else None,
                "timestamp": str(msg.date),
                "message": msg.message
            })

    # Save to JSON
    os.makedirs('../data/raw', exist_ok=True)
    with open('../data/raw/messages.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(result)} messages saved to data/raw/messages.json")

with client:
    client.loop.run_until_complete(fetch_messages(channel_username))
