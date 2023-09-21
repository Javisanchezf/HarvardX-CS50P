class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("You exceeded the maximum capacity")
        else:
            self.size += n

    def get_available_space(self):
        return "🍪" * (self._capacity - self._size)

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies :(")
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("@capacity.setter error")
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("@size.setter error")
        else:
            self._size = size


def main():
    jar = Jar()
    print(jar)
    jar.deposit(12)
    print(f"Current: {jar}")
    print(f"Available: {jar.get_available_space()}")
    jar.withdraw(8)
    print(f"Current: {jar}")
    print(f"Available: {jar.get_available_space()}")


if __name__ == "__main__":
    main()
