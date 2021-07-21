from app import app

#invokes the run methon to start the server
app.secret_key = ",dYgK&N+yzEyfkf'U<eFNQyKR(tfE)^j%JgffL:v!dT&eQFYBB+69\@g!ge>'}>M"
if __name__ == "__main__":
    app.run(debug=True)
