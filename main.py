import subprocess
import webbrowser
import smtplib
import instaloader
import geocoder
import requests
import os
import random
import pyttsx3
from bs4 import BeautifulSoup
import tweepy


def open_notepad():
    subprocess.run(["notepad.exe"])


def open_chrome():
    webbrowser.open("https://www.google.com")


def open_whatsapp():
    subprocess.run(["<path_to_whatsapp_executable>"])  # Replace with the actual path


def convert_to_example_email(name):
    return name.lower().replace(" ", ".") + "@example.com"


def send_sms():
    random_number = random.randint(1000, 9999)
    # Use SMS API to send the message with random_number


def open_chatgpt():
    webbrowser.open("https://www.openai.com/chatgpt")


def get_geolocation(address):
    try:
        location = geocoder.osm(address)
        latitude, longitude = location.latlng
        return latitude, longitude
    except Exception as e:
        print(f"Error getting geolocation: {e}")
        return None


def geolocation_interaction():
    address = input("Enter an address for geolocation: ")
    coordinates = get_geolocation(address)
    if coordinates:
        print(f"Latitude: {coordinates[0]}, Longitude: {coordinates[1]}")
    else:
        print("Geolocation not available.")


def get_twitter_trends():
    # Set up your Twitter API credentials
    consumer_key = "your_consumer_key"
    consumer_secret = "your_consumer_secret"
    access_token = "your_access_token"
    access_token_secret = "your_access_token_secret"

    # Authenticate with Twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth)

    try:
        # Get the available places (WOEID - Where On Earth IDentifier)
        places = api.available_trends()

        # Choose a place (e.g., Worldwide)
        woeid = 1  # WOEID for Worldwide
        trends = api.trends_place(id=woeid)

        # Extract and print the trends
        if trends:
            print("Current Twitter Trends:")
            for trend in trends[0]['trends']:
                print(f"- {trend['name']}")
        else:
            print("No trends available for the specified location.")

    except tweepy.TweepError as e:
        print(f"Error: {e}")


def get_instagram_posts_by_hashtag(hashtag, count=10):
    L = instaloader.Instaloader()
    try:
        # Retrieve posts with the given hashtag
        posts = instaloader.Hashtag.from_name(L.context, hashtag).get_top_posts()

        # Print the top N posts
        print(f"Top {count} posts for #{hashtag} on Instagram:")
        for i, post in enumerate(posts, 1):
            if i > count:
                break
            print(f"{i}. {post.url}")

    except instaloader.InstaloaderException as e:
        print(f"Error: {e}")


def get_wikipedia_data(topic):
    wikipedia_url = f"https://en.wikipedia.org/wiki/{topic}"
    response = requests.get(wikipedia_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.text
        paragraphs = soup.find_all('p')

        print(f"Title: {title}\n")

        for paragraph in paragraphs:
            print(paragraph.text)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")


def play_random_music():
    music_folder = "<path_to_music_folder>"  # Replace with the actual path
    music_files = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
    if music_files:
        random_music = os.path.join(music_folder, random.choice(music_files))
        subprocess.run(["<path_to_audio_player_executable>", random_music])


def play_video():
    try:
        video_path = input("Enter the path to the video file: ")
        subprocess.Popen([video_path], shell=True)
        input("Press Enter to stop playing...")
    except Exception as e:
        print(f"Error playing video: {e}")


def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def main():
    while True:
      print("1. Open Notepad"
            "2. Open Google Chrome"
            "3. Open WhatsApp"
            "4. Convert Name to Example Email"
            "5. Send SMS with Random Number"
            "6. Open ChatGPT Website"
            "7. Get Geolocation of a City"
            "8. Get Twitter Trends"
            "9. Get Top Posts with Hashtags"
            "10. Get Wikipedia Data"
            "11. Play Random Music"
            "12. Play Video"
            "13. Control Speaker Sound"
             "0. Exit"

      )

        choice = input("Enter your choice: ")

        if choice == "0":
            break
        elif choice == "1":
            open_notepad()
        elif choice == "2":
            open_chrome()
        elif choice == "3":
            open_whatsapp()
        elif choice == "4":
            name = input("Enter name: ")
            print(f"Example Email: {convert_to_example_email(name)}")
        elif choice == "5":
            send_sms()
        elif choice == "6":
            open_chatgpt()
        elif choice == "7":
            city = input("Enter city: ")
            geolocation_interaction()
        elif choice == "8":
            get_twitter_trends()
        elif choice == "9":
            hashtag = input("Enter hashtag: ")
            get_instagram_posts_by_hashtag(hashtag)
        elif choice == "10":
            topic = input("Enter topic: ")
            get_wikipedia_data(topic)
        elif choice == "11":
            play_random_music()
        elif choice == "12":
            play_video()
        elif choice == "13":
            text = input("Enter text to speak: ")
            speak_text(text)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
