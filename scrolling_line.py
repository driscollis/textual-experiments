class ScrollingLine(Static):
    # Edward Jazzhands

    def on_mount(self):
        self.counter = 0
        self.max = 3
        self.set_interval(1 / 15, self.asciiscroll)

    def asciiscroll(self):
        asciifoo = (" " * self.counter) + "+" + (" " * ((self.counter - self.max)*-1))
        self.update(asciifoo * (self.screen.size.width//4))
        self.counter += 1
        if self.counter > self.max:
            self.counter = 0