## Pan-Tilt Cam

This project is a fun experiment with WebRTC and IoT. It uses WebRTC to control
remotely a "homemade" Raspberry Pi driven pan-tilt servo mechanism with a
night-vision camera.

![Pan-Tilt Cam](https://lucaong.github.io/pantiltcam/pantiltcam.png?x=1)

The project uses:

  - [Pan-Tilt HAT by Pimoroni](https://shop.pimoroni.com/products/pan-tilt-hat)

  - [Night-vision camera module for Raspberry Pi](https://shop.pimoroni.com/products/night-vision-camera-module-for-raspberry-pi?variant=12516582752339)

  - [Raspberry Pi Zero W](https://shop.pimoroni.com/products/raspberry-pi-zero-w)


## Disclaimer

This project is a prototype and experiment. Do not use it in privacy-sensitive
contexts. Even though this project establishes a peer-to-peer connection and no
video data is shared with any server, it is still designed for simplicity of
testing and not for security. In particular, it is using public signaling and
STUN servers, and there is no authentication apart from your choice of a
"secret" ID. For any serious application, one would have to at minimum run
private servers, and implement some secure authentication and authorization
mechanisms.


## Setup

### Hardware:

Assemble the Pan-Tilt HAT and the camera. I had to cut some of the plastic
pieces on the Pan-Tilt module, and get creative with double-sided tape and cable
ties. I also had to use a longer (30cm) camera cable, and some stand-offs and
bolts to make everything sturdy and stable.

### Software:

Install the latest Raspbian on the Raspberry Pi. Setup the WiFi network, enable
the camera module (find the instructions on the Raspberry Pi guides). Install
the Pimoroni Pan-Tilt HAT support software by following instructions
[here](https://github.com/pimoroni/pantilt-hat).

You will also have to setup the camera to be used as a webcam by running:

```
echo "bcm2835-v4l2" | sudo tee -a /etc/modules
```

Finally, clone or download this project onto the Raspberry Pi.


## Usage

Choose a unique ID. It should be a unique and URL-safe secret string. Anyone in
possession of this ID can view and control your camera.

### On the Raspberry Pi:

You can connect to the Pi via SSH, or plug it to a screen/keyboard. The
following instructions assume you are connecting via SSH, so you don't have a
display attached to the Pi.

Navigate to the project directory, then start the Python server and the headless
Chrome browser with (substitute YOUR-CHOSEN-ID with the ID you chose):

```
./start YOUR-CHOSEN-ID
```

### On your computer or smartphone:

Visit [https://lucaong.github.io/pantiltcam](https://lucaong.github.io/pantiltcam) and insert the ID you chose.

_Note: the project is currently using public STUN servers and no TURN server so,
depending on your router and firewall setup, it might not always be possible to
connect to the camera from outside your local network._


## Acknowledgement

The project uses the nice [PeerJS](https://peerjs.com) library to simplify
WebRTC connections. It is also using the public PeerJS signaling server.

The Python server uses the [Pimoroni Python
library](https://github.com/pimoroni/pantilt-hat) for the Pan-Tilt HAT, and is
adapted from one of the examples.
