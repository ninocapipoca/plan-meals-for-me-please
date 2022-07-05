# plan-meals-for-me-please
A python script to take some recipes from a BBC goodfood page and plan meals for the week based on those recipes. Done as a first (personal) webscraping project.

The idea was to create a script to facilitate life at home. Webscraping is a very useful skill that I've been interested in learning for a while, and I don't like planning meals so I thought this was a win-win situation! I wrote this initially for my own learning, but anyone is welcome to take my code and improve it.

### How it works
Run the main file using `python3 main.py` and you will be asked for user input for the following options:
- What BBC goodfood page you want to get your recipes from
- How many meals you want to plan in the week
- Whether you want to plan only lunches, only dinners or both

Based on this, recipes are extracted from the webpage used as input and an excel file is generated with the recipes randomly assigned to a meal / day of the week. Another file with the ingredients and link to each recipe is generated as well. The idea is that this could act as a kind of shopping list.

### Issues
I wrote this as a personal project, and rather quickly, so as of yet I have not had the opportunity to get rid of all the bugs and optimize as much as I would like - it was really a beginner project. Thus, there are a number of issues at the moment. These are only the ones I have found so far, based on a quick glance and a few simple tests.
- I capped the number of meals that the program is able to plan at max 1 week's worth of meals (i.e. 14) but I did not cap the number for dinners only or lunches only (i.e., there will be an error if you choose more than 7 meals and "dinner only" or "lunch only")
- I did not check whether there are sufficient recipes on the webpage to satisfy the number of meals desired
- The excel cells are too small for the recipe names

### Improvements
This is what I would like to improve when revisiting this project, apart from the necessary debugging:
- Add the ability to use recipes from not only one, but multiple webpages
- Scrape only the number of recipes desired, rather than all of them and then selecting a few
- Generate a proper shopping list taking into consideration duplicates & quantities (this is particularly challenging due to the way ingredients are written)
- Create a proper user-friendly interface rather than just using the terminal

If you would like to make this a bigger project, I'd be very happy to work on this with you, so feel free to contact me.

# Installation guides
## Installing Python & pip
### Mac OS
1. Check if you have Python installed with `python --version`. If you don't have at least Python 2.7, you can install it by following an online tutorial such as [this one](https://www.dataquest.io/blog/installing-python-on-mac/).
2. Install pip on your machine: If you don't have homebrew, do `python -m ensurepip` or `python3 -m ensurepip` and you should be done. If you do, you can simply do `brew install python` followed by `brew unlink python && brew link python`. In both cases it is advisable to check that the installation was successful using `pip --version`.

### Windows
1. Check if you have Python installed with `python --version`. If you don't have at least Python 2.7, you can install it by following an online tutorial such as [this one](https://phoenixnap.com/kb/how-to-install-python-3-windows).
2. Install pip on your machine: You can check if it is already installed using `pip help` or `pip --version`, if it responds, you don't need to do anything. Otherwise, get the file with `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py` then type `python get-pip.py`. Verify whether you have installed it successfully. If not, you may want to look at [this page](https://phoenixnap.com/kb/install-pip-windows).

### Linux (Ubuntu)
1. Check if you have Python installed with `python --version`. If you don't have at least Python 2.7, you can install it by following an online tutorial such as [this one](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu).
2. Install pip on your machine: You can check whhether it is installed using `pip help` or `pip --version` as in Windows. If it isn't, it is recommended that you update first with `sudo apt-get update`, then install pip with `sudo apt-get -y install pip`, and check whether it was successful. If not, you may want to look at [this page](https://www.educative.io/answers/installing-pip3-in-ubuntu) carefully.


## Required libraries
The following libraries are required to run this program. They can be installed using pip or another method of your choice, if they are not already installed on your machine.
- requests 
- pandas
- openpyxl
- random
- math
- beautifulsoup (beautifulsoup4)
They can be installed with the command `pip install` followed by the library name, eg `pip install beautifulsoup4`.
