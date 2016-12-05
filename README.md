# EXAM: Python Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
- You can use any resource online, but **please work individually**
- **Don't just copy-paste** your answers and solutions, use your own words instead.


# Tasks
## 1-5. Complete the tasks seen in the first-fifth.py files! (~120 mins)
### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently, after each task, with descriptive commit messages [1p]
- The solution follows [styleguide](https://github.com/greenfox-academy/teaching-materials/blob/master/styleguide/python.md) [1p]

## 6. Question time! (~30 mins) [6p]

### Explain the algorithm seen in `third.py`. Use a flowchart, structogram or pseudo code. [2p]
#### Your answer:

### How can you create a graphical user interface and draw a rectangle on it in python? What are the tools needed for it? [2p]

For drawing a rectangle in Python you should use Tkinter, which is the interface to the Tk GUI toolkit shipped with Python. The main steps:
- Import the Tkinter module
- Create your mainloop (base/root) --> this will keep the window open, until you quit
- Import the canvas widget, and define your canvas' width/height (you can also add a bakckground color)
- Draw a wonderful rectangle! (You can fill this with any color too, same goes for its borders).

Example:

root = Tk()

canvas = Canvas(root, width=2560, height=1600)
canvas.pack()
canvas.create_rectangle(800, 800, 1300, 1300, fill="green")

root.mainloop()

### What does V stand for in MVC? [2p]

It stands for View (as the others stand for Model and Controller). The View element provides the user interface of a program. View is the visual representation of the Model, and it can also send user actions to the Controller. View can be independent from both the Model and the Controller too.
