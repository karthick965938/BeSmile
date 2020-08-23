# BeSmile

**BeSmile** - A Python Web App for Facial Emotion Recognition using PyTorch. BeSmile is developed and using [PyEmotion](https://github.com/karthick965938/PyEmotion)


**Author**: Karthick Nagarajan

**Email**: karthick965938@gmail.com

## Run
We can create local database using this command. Database is mandatory one, without DB we can't store the details.

```sh
python db.py
```
We can run this application using this command

```sh
python main.py
```

## Requirements
```sh
pytorch >= 1.5.1
torchvision >= 0.6.1
pyemotion >= 0.0.5
facenet-pytorch >= 2.3.0
sqlite >= 3.32.3
flask-apscheduler >= 1.11.0
notify2 >= 0.3.1
```


## Contributing
All issues and pull requests are welcome! To run the code locally, first, fork the repository and then run the following commands on your computer:

```sh
git clone https://github.com/<your-username>/BeSmile.git
cd BeSmile
# Recommended creating a virtual environment before the next step
pip3 install -r requirements.txt
```
When adding code, be sure to write unit tests where necessary.

## Contact
PyEmotion was created by [Karthick Nagarajan](https://stackoverflow.com/users/6295641/karthick-nagarajan?tab=profile). Feel free to reach out on [Twitter](https://twitter.com/Karthick965938) or through [Email!](karthick965938@gmail.com)
