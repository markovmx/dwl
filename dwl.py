from dotenv import dotenv_values

import requests
import argparse
import os


config = dotenv_values(".env")
access_token = config.get("VK_ACCESS_TOKEN")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Your script description here")
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument(
        "--community", action="store_true", help="Run the script in community mode")
    mode_group.add_argument("--saved", action="store_true",
                            help="Run the script in saved mode")
    parser.add_argument(
        "--group_name", help="Specify the group name (required for community mode)")

    return parser.parse_args()


def parse_group_id(access_token, group_name):
    params = {
        'access_token': access_token,
        'v': '5.131',
        'screen_name': group_name
    }
    response = requests.get(
        'https://api.vk.com/method/utils.resolveScreenName', params=params)
    data = response.json()

    # Check if response contains an error
    if 'error' in data:
        print("Error:", data['error']['error_msg'])
        return None

    return data['response']['object_id']


def parse_user_id(access_token):
    params = {
        'access_token': access_token,
        'v': '5.131'
    }
    response = requests.get(
        'https://api.vk.com/method/users.get', params=params)
    data = response.json()

    # Check if response contains an error
    if 'error' in data:
        print("Error:", data['error']['error_msg'])
        return None

    return data['response'][0]['id']


def save_photo(url, filename):
    with open(filename, 'wb') as f:
        response = requests.get(url)
        f.write(response.content)


def download_community_photos(access_token, group_name):
    group_id = parse_group_id(access_token, group_name)

    if group_id is None:
        print("Error: Unable to resolve screen name.")
        return

    offset = 0
    total_posts = float('inf')
    downloaded_images = set()
    community_folder = f"./output/{group_name}_photos"

    while offset < total_posts:
        params = {
            'access_token': access_token,
            'v': '5.131',
            'owner_id': f'-{group_id}',
            'offset': offset
        }

        response = requests.get(
            'https://api.vk.com/method/wall.get', params=params)

        data = response.json()

        if 'error' in data:
            print("Error:", data['error']['error_msg'])
            return

        if offset == 0:
            total_posts = data['response']['count']

        if not os.path.exists(community_folder):
            os.makedirs(community_folder)

        for item in data['response']['items']:
            if 'attachments' in item:
                for attachment in item['attachments']:
                    if attachment['type'] == 'photo':
                        photo_id = attachment['photo']['id']
                        if photo_id in downloaded_images:
                            print(f"Skipped: {photo_id}. Already downloaded.")
                            continue

                        # Get the largest available size of the photo
                        photo_url = attachment['photo']['sizes'][-1]['url']
                        # Save photos with their ID as filenames
                        photo_name = os.path.join(
                            community_folder, f"{photo_id}.jpg")

                        # Check if file already exists
                        if os.path.exists(photo_name):
                            print(f"Skipped: {photo_name}. Already exists.")
                            continue

                        save_photo(photo_url, photo_name)
                        print(f"Downloaded: {photo_name}")
                        downloaded_images.add(photo_id)

        # Update offset for the next request
        offset += len(data['response']['items'])


def download_saved_photos(access_token):
    user_id = parse_user_id(access_token)

    if user_id is None:
        print("Error: Unable to retrieve user ID.")
        return

    offset = 0
    total_photos = float('inf')
    downloaded_images = set()
    user_folder = f"./output/user_{user_id}_photos"

    while offset < total_photos:
        params = {
            'access_token': access_token,
            'v': '5.131',
            'album_id': 'saved',
            'offset': offset
        }
        response = requests.get(
            'https://api.vk.com/method/photos.get', params=params)
        data = response.json()

        if 'error' in data:
            print("Error:", data['error']['error_msg'])
            return

        if offset == 0:
            total_photos = data['response']['count']

        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        for item in data['response']['items']:
            photo_id = item['id']
            if photo_id in downloaded_images:
                print(f"Skipped: {photo_id}. Already downloaded.")
                continue

            photo_url = item['sizes'][-1]['url']
            photo_name = f"{user_folder}/{photo_id}.jpg"
            save_photo(photo_url, photo_name)
            print(f"Downloaded: {photo_name}")
            downloaded_images.add(photo_id)

        offset += len(data['response']['items'])


def main():
    if not access_token:
        print("Access token is required for launch dwl.py.")
        return

    args = parse_args()

    if args.community:
        if not args.group_name:
            print("Group name is required for community mode.")
            return
        # Your community mode code here
        print(f"Running in community mode with group name: {args.group_name}")
        download_community_photos(access_token, args.group_name)
    elif args.saved:
        # Your saved mode code here
        print("Running in saved mode")
        download_saved_photos(access_token)
    else:
        print("Invalid mode selected")


if __name__ == "__main__":
    main()
