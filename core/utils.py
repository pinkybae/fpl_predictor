class CustomLogger():
    level: int = None
    
    def __init__(self) -> None:
        self.level = 0
    
    def info(self, msg: str) -> None:
        print(self.level*'\t',msg)

    def start(self, msg: str) -> None:
        self.level += 1
        self.info(msg+' :: start')

    def end(self, msg: str) -> None:
        self.info(msg+' :: end')
        self.level -= 1

    def error(self, msg: str) -> None:
        self.info('[ERROR]'+msg)
