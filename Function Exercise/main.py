class Exercise:

    def __init__(self):
        pass

    def gramsToOunce(self, grams):
        # grams / 28.35
        return grams / 28.35

    def fahrToCels(self, fahr):
        # (32 °F − 32) × 5/9
        return (fahr - 32) * 5 / 9

    # Calculate the amount obtained by investing the principal(P)
    # for (N) years at the rate of (R).The following formula
    # is used for the conversion: A = P * (1 + R) ^ N
    def compound_interest(self, r, n, p):
        return p * (1+r) ** n


exe = Exercise()

print(exe.gramsToOunce(32))
print(exe.fahrToCels(90))
print(exe.compound_interest(5, 5, 5))