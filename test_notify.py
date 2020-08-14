import notify2
notify2.init('app name')
# n = notify2.Notification('title', 'message')
n = notify2.Notification("Icon Test", "Testing stock icon", icon="/static/images/Sad.png")
n.show()