## DiscoStats
cool statistics generated using your discord data. <br><br>
![image](https://user-images.githubusercontent.com/61324615/162575845-50461c9a-1cb4-47b1-9cf4-fce863a9f79e.png)

### How?
DiscoStats is not a service that breaks the Discord Terms of Service or Community Guidelines. Discord has an option to request data which is what this entire application is based upon. It just scans through the lines of text of every message you have ever sent and generates statistics based upon that. As a forewarning, you need to request your data to use the application, which could potentially take up to 30 days.

### Installation
⚠️ make sure you have python 3.7+ installed.
- Clone the repository:
```bash
git clone https://github.com/ibra/DiscoStats
```
- Install the dependencies:
```bash
pip install -r requirements.txt
```
- Move your discord data inside the project directory, **make sure it is all dumped under one "package" folder.**
- run main file:
```bash
python main.py  
``` 
- optionally use the --dir flag to pinpoint the package location to a specific directory:
```bash 
python main.py --dir otherFolder/package
```


### Known Limitations

- the name of servers, channels, users etc. cannot be displayed as there is no way to do that without having a bot or some sort of authorization within the server itself
- the names of the emojis alone cannot be used because there could be conflicts between different servers, so its more convenient for them to be displayed in the `<:Emoji:12345678910>` format.
