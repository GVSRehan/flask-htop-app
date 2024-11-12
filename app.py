#install flask to run
from flask import Flask  
import os  
import datetime  
import subprocess  

app = Flask(__name__)  

@app.route('/htop')  
def htop():    
    server_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).isoformat()   
    username = os.getlogin()    
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')  

    return f"""  
    <html>  
        <body>  
            <h1>Name: Gurram Venkata Sai Rehan</h1>  
            <h2>Username: {sairehan}</h2>  
            <h3>Server Time (IST): {server_time}</h3>  
            <pre>TOP output:\n{top_output}</pre>  
        </body>  
    </html>  
    """  

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5000)