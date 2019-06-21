# PYBAT

##(Data over Ultrasonics)

## What it does ?

Connectionless ultrasonic message transfer.

Using ultrasonic communication as a covert channel in consumer electronics products.Researching into sustaining a transmission rate of 1 byte per second for arbitrary binary data, and to obtained up to 99.5% accuracy when broadcasting across 0 feet, and up to 81.6% accuracy when broadcasting across 10 feet.

This project demonstrates that for small messages ultrasonic communication is quite feasible using standard microphones and speakers shipped in consumer electronics.

We then are currenltly exploring the limitations of this type of communication as well as potential use cases for surveillance and countermeasures in a cyber security led research project.

The project is inspired from below mentioned articles and relative findings.

## Purpose

- Computer speakers and headphones make passable microphones and can be used to receive data via ultrasonic sound and send signals back, making the practice of air gapping sensitive computer systems less secure.

- Surveillance and Countermeasures

## What's here?

The repo contains examples following files which will interest you:

- sound_encoder.py: For encoding stuff.
- sound_decoder.py: For decoding stuff.
- demo.py: Running the demo will listen to ultrasonic sound as soon as another system sends a ultrasonic finger print based on the sound file it will press the up or down arrow key with help of pygui.This way you can control any games or presentation slides over ultrasonic.

## Requirements

numpy>=1.11.2
PyAudio>=0.2.9
scipy>=0.18.1
reedsolo>=0.3

## How to Use

1. Ultrasonic data sending over two computers :

- Just makes sure the volume or sound permissions are given and you will have to run reciver_example.py or sender_example.py on either of one laptops/machines.
- You can either manipulate what string you wish to send or generate a wav file with your data in it.

2. Using Android app to establish Ultrasonic Data sharing:

- Run the android project in android studio
- Make sure when you run the apk the permissions are enabled
- After the app is started press the Floating Action button to send ultrasonic message to any reciver. (You will have to run a receiver_example.py in the laptop to view what's been send via android device)
- WIP - We have a naive implementation of flashlight trigger code
  - Currently we do have implemented automatic flash light switching when a phone recieves the ultrasonic sound.
  - Due to the Android O background service limitations the app has to be in foreground to make it work.This experimental example explains that the phones can be used to control and send data evading users privacy or even taking actual control of phone without user knowledge (See the Reference SilverPush)

## Our Inspiration :

- Real world Inspiration

  - [Instagram microphone tapping](https://www.vox.com/the-goods/2018/12/28/18158968/facebook-microphone-tapping-recording-instagram-ads)
  - [Turning Speakers into listening Devices](https://www.theregister.co.uk/2018/03/12/turning_speakers_into_covert_listening_devices/)
  - [Apps are listening you](https://www.zdnet.com/article/hundreds-of-apps-are-using-ultrasonic-sounds-to-track-your-ad-habits/)

  - [SilverPush Unmasked Repo](https://github.com/MAVProxyUser/SilverPushUnmasked/blob/master/SilverPushDocumentation.pdf)

- Frictional Inspiration

  - [Ultrasonic Bat Beacon](https://batman.fandom.com/wiki/Ultrasonic_Bat_Beacon)

- Codec Libray Credits Implementations
  - [Ultrasonic Encoder/Decoder for Python](https://github.com/bonniee/ultrasonic)
  - [Sonicky ](https://github.com/egglang/sonicky)
