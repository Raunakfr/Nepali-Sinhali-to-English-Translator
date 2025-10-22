# Nepali-Sinhali-to-English-Translator
A project made for the solution to the problem statement number 240.<br>
Upon opening the locally hosted website, the user is shown a GUI of sorts in which he can select either Nepali or Sinhali, basically the language which needs to be translated.<br>
Uses tessaract OCR module to effectively "see" characters from any uploaded image or pdf and produce them as text output.<br>
Currently it supports files upto 200mb, which should be enough for most of the images or pdfs.<br>
After succesfully extracting the text from the image, it can translate either Nepali or Sinhali to English.<br>
For translation of Nepali to English, it uses an independently developed public translation module from HuggingFace.<br>
For Sinhalese,  the model isn't available on huggingface, so a seperate model will need to be trained over data to be able to provide meaningful results.<br>

For V2:<br>
⭐ Sinhalese support<br>
⭐ Auto cropping and enhancing of images<br>
⭐ Support for many more file types
