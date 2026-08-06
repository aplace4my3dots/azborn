#!/usr/bin/env python3
"""
E-RUN Magazine — Automated Instagram Publisher Script
Connects to the official Meta Graph API (Instagram Content Publishing API)
to upload generated issue covers (`images/...`) and post captions (`captions/...`) daily.
"""

import os
import sys
import json
import time
import requests
from datetime import datetime

def post_to_instagram(image_url_or_path, caption_path):
    access_token = os.environ.get("INSTAGRAM_ACCESS_TOKEN")
    instagram_account_id = os.environ.get("INSTAGRAM_ACCOUNT_ID")
    
    if not access_token or not instagram_account_id:
        print("⚠️ [Notice] INSTAGRAM_ACCESS_TOKEN and/or INSTAGRAM_ACCOUNT_ID environment variables are not set.")
        print("💡 To enable 100% automated hands-free daily Instagram uploading:")
        print("   1. Go to your Meta/Facebook Developer Portal -> App -> Graph API -> Instagram Graph API.")
        print("   2. Generate a Long-Lived Access Token for your Instagram Business Account.")
        print("   3. Add INSTAGRAM_ACCESS_TOKEN and INSTAGRAM_ACCOUNT_ID to your GitHub Repository -> Settings -> Secrets and variables -> Actions.")
        print("   4. Once added, our daily GitHub Actions cron job will automatically publish every morning without any human intervention!")
        print(f"\n📁 Prepared Daily Assets Ready for Manual or Automated Post:")
        print(f"   🖼️ Image Path: {image_url_or_path}")
        print(f"   💬 Caption File: {caption_path}")
        return False

    if not os.path.exists(caption_path):
        print(f"❌ Error: Caption file {caption_path} not found.")
        return False
        
    with open(caption_path, "r", encoding="utf-8") as f:
        caption_text = f.read()

    print(f"🚀 Starting Instagram Upload Pipeline for Account ID: {instagram_account_id}...")
    
    # Step 1: Create Media Container using Meta Graph API
    # Note: Meta Graph API requires a publicly accessible image URL (e.g. hosted on GitHub Pages or S3/Raw GitHub link)
    create_media_url = f"https://graph.facebook.com/v19.0/{instagram_account_id}/media"
    payload = {
        "image_url": image_url_or_path,
        "caption": caption_text,
        "access_token": access_token
    }
    
    response = requests.post(create_media_url, data=payload)
    if response.status_code != 200:
        print(f"❌ Failed to create media container: {response.text}")
        return False
        
    creation_id = response.json().get("id")
    print(f"✅ Media container created successfully! Container ID: {creation_id}")
    
    # Step 2: Check status & Wait briefly for Meta servers to process the image
    time.sleep(10)
    
    # Step 3: Publish the Media Container
    publish_url = f"https://graph.facebook.com/v19.0/{instagram_account_id}/media_publish"
    publish_payload = {
        "creation_id": creation_id,
        "access_token": access_token
    }
    
    pub_response = requests.post(publish_url, data=publish_payload)
    if pub_response.status_code != 200:
        print(f"❌ Failed to publish media: {pub_response.text}")
        return False
        
    post_id = pub_response.json().get("id")
    print(f"🎉 SUCCESS! Daily E-RUN concept posted directly to Instagram! Post ID: {post_id}")
    return True

if __name__ == "__main__":
    today_str = datetime.now().strftime("%Y-%m-%d")
    caption_file = f"captions/{today_str}.txt"
    # When running via GitHub Actions, we pass the raw GitHub URL or image asset path
    image_file = os.environ.get("INSTAGRAM_IMAGE_URL", f"https://raw.githubusercontent.com/aplace4my3dots/azborn/arena/019f66d7-azborn/images/erun_new_concept_silkmoth.jpg")
    
    post_to_instagram(image_file, caption_file)
