### References
 - https://medium.com/slanglabs/how-to-build-python-transcriber-using-mozilla-deepspeech-5485b8d234cf

###Install dependencies
  - sudo apt-get install -y sox
    - Error faced :
      - Could not get lock /var/lib/dpkg/lock-frontend - open (11: Resource temporarily unavailable)
        ```
        sudo lsof /var/lib/dpkg/lock-frontend
        sudo kill -9 <pid>
        ```
   - sudo apt-get install -y libgomp1
   - sudo apt-get install -y libpthread-stubs0-dev     
   - sudo apt-get install libstdc++6
    
### Download pretrained model
``` 
wget https://github.com/mozilla/DeepSpeech/releases/download/v0.6.1/deepspeech-0.6.1-models.tar.gz
tar xvfz deepspeech-0.6.1-models.tar.gz 
```

### Record sound
```
arecord test.wav --rate 16000 -f S16_LE 
```
