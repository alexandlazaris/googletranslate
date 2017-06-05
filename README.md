# googletranslate
First text, then voice. Then ... the world.

![alt text](/my-first-api-call.png)

List of languages:
```
https://cloud.google.com/translate/docs/languages
```
If developing on Windows with python 3.x, you'll find problems encode errors when running in cmd or Git Bash. Reference to diagnose is here https://stackoverflow.com/questions/32382686/unicodeencodeerror-charmap-codec-cant-encode-character-u2010-character-m. To fix, run this in cmd:
```
chcp 65001
```
Should output:
```
Active code page: 65001
```
