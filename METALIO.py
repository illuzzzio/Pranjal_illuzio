from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow,self).__init__()
   
    self.browser =QWebEngineView()
    self.browser.setUrl(QUrl("http://youtube.com"))
    self.setCentralWidget(self.browser)
    self.showMaximized()


    # here is my navbar//
    navbar = QToolBar()
    navbar.setStyleSheet("background-color:grey; ")
    self.addToolBar(navbar)
    backy_but = QAction("<<",self)
    backy_but.triggered.connect(self.browser.back)
    navbar.addAction(backy_but)
  

    # forward button
    GoForward_but = QAction(">>",self)
    GoForward_but.triggered.connect(self.browser.forward)
    navbar.addAction(GoForward_but)
    


    #reload button

    Reload_but = QAction("Reload", self)
    Reload_but.triggered.connect(self.browser.reload)
    navbar.addAction(Reload_but)

    #home button

    Home_but = QAction("Home/Google",self)
    Home_but.triggered.connect(self.mynavigation)
    navbar.addAction(Home_but)

    # for direct acces to chat gpt 

    AI_but = QAction("GPT-BOT",self)
    AI_but.triggered.connect(self.chatgpt)
    navbar.addAction(AI_but)


    # for direct access to leetcode 



    Coding_btn = QAction("Leetcode",self)
    Coding_btn.triggered.connect(self.leetcodegg)
    navbar.addAction(Coding_btn)
  # here are my function for getting url and calling them insode the navbar by using Add action

    self.MyURLbar =  QLineEdit()
    navbar.addWidget(self.MyURLbar) # here i am telling my navbar to add a functionality to add class names self MyURLbar into the navbar usign addWidget prebuilt funvtion used in python PYQt5
    self.MyURLbar.returnPressed.connect(self.navigate_to_url)
    self.browser.urlChanged.connect(self.update_url)

  def mynavigation(self):
   self.browser.setUrl(QUrl("http://google.com"))

  def chatgpt(self):
    self.browser.setUrl(QUrl("https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://chat.openai.com/chat&ved=2ahUKEwjz7OCP0veKAxVTxjgGHSCQDboQFnoECAQQAQ&usg=AOvVaw3lRPBLGecBrZ06Ha4HKic2"))
  def leetcodegg(self):
    self.browser.setUrl(QUrl("https://leetcode.com/"))
  def navigate_to_url(self):
    url = self.MyURLbar.text()
     # Check if the URL contains 'http://' or 'https://'
    if not  url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url  # Add http:// if the user doesn't specify it
    self.browser.setUrl(QUrl(url))

    
  def update_url(self,g):
    self.MyURLbar.setText(g.toString())
   ## with this we dont need to write https:/
    

    
    
    




application = QApplication(sys.argv)
QApplication.setApplicationDisplayName("METALIO BROWSER")
window = MainWindow()
application.exec_()