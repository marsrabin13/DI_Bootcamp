# 🌟 Exercise 1 — Currencies

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    # Implement: __str__, __repr__, __int__, __add__, __iadd__

    def __str__(self):
      return f"{self.amount} {self.currency}s"


    def __add__(self, other):
      if isinstance(other, int):
        return self.amount + other # returns an integer
      if isinstance(other, Currency):
        if self.currency != other.currency:
          raise TypeError(
              f"Cannot add between Currency type "
              f"<{self.currency}> and <{other.currency}>"
          )
        return self.amount + other.amount # returns an integer

      raise TypeError(f"Cannot add Currency and {type(other)}")


    def __iadd__(self, other):
      if isinstance(other, int):
        self.amount += other # modifies THIS Currency's amount
        return self
      if isinstance(other, Currency):
        if self.currency != other.currency:
          raise TypeError(
              f"Cannot add between Currency type "
              f"<{self.currency}> and <{other.currency}>"
          )
        self.amount += other.amount # modifies THIS Currency's amount
        return self
      raise TypeError(f"Cannot add Currency and {type(other)}")

# Test
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)


print(c1 + 5)         # 10
print(c1 + c2)        # 15

c1 += 5 # c1 amount goes from 5 to 10
c1 += c2
print(c1)             # 20 dollars