import webbrowser

welcome = "Welcome to My First HTML Program Using Python!"
name = "My name is King Aj Magalona!"
thanks = "Thank you!"

htmlScript = f"<html> <head> <body> <h1> {welcome} </h1> <h2> {name}</h2> <p> {thanks} </p> </body> </head></html>"

with open('helloworld.html', 'w') as html:
    html.write(htmlScript)
    print("File Created Succesfully!")

webbrowser.open_new_tab('helloworld.html')
