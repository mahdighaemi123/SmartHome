class LoggerTool():
    def start_log(self):
        print("DataReader")
        print("- starting...")

    def log(self,**kwargs):
        print("LOG")

        for key,value in kwargs.items():
            print(f"- {key}:",value)

    def log_server_resp(self,url,response_code, response_text):
        print(url)
        print("- response_code:",response_code)