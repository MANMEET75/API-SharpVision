# API-SharpVision

# How to Deploy Streamlit app on EC2 instance

## 1. Login with your AWS console and launch an EC2 instance

## 2. Run the following commands

### Note: Do the port mapping to this port:- 8000

```bash
sudo apt update
```

```bash
sudo apt upgrade -y
```

```bash
sudo apt-get install curl
```
```bash
cd /tmp
curl -O https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
```
```bash
bash Anaconda3-2020.11-Linux-x86_64.sh
```
```bash
source ~/anaconda3/bin/activate
```
```bash
conda create -p venv python==3.11 -y
```
```bash
conda activate venv/
```
```bash
sudo apt install git curl unzip tar make sudo vim wget -y
```
```bash
git clone https://github.com/MANMEET75/API-SharpVision.git
```

```bash
sudo apt install python3-pip
```


```bash
pip3 install -r requirements.txt
```

```bash
sudo apt-get install python3-opencv
```

```bash
conda install opencv
```

```bash
#Temporary running
uvicorn main:app --host 0.0.0.0 --reload
```

```bash
#Permanent running
nohup uvicorn main:app --host 0.0.0.0 --reload
```

Note: fastapi runs on this port: 8000
#### Enjoy Coding!
