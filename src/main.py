from state import State
from machine import Machine
from direction import Direction


def teste_anbn():
    """Turing Machine for Context-Free Language a^nb^n"""
    print("\n=== Test 1: Context-Free Language { a^nb^n | n>=0 } ===")
    q0 = State("q0")
    q1 = State("q1")
    q2 = State("q2")
    q3 = State("q3")
    q4 = State("q4")
    qf = State("qf")
    qf.setFinal()

    q0.addTransition(q1, "a", "A", Direction.RIGHT)
    q0.addTransition(q3, "_", "_", Direction.LEFT)
    q0.addTransition(q4, "B", "B", Direction.RIGHT)

    q1.addTransition(q1, "a", "a", Direction.RIGHT)
    q1.addTransition(q1, "B", "B", Direction.RIGHT)
    q1.addTransition(q2, "b", "B", Direction.LEFT)

    q2.addTransition(q2, "a", "a", Direction.LEFT)
    q2.addTransition(q2, "B", "B", Direction.LEFT)
    q2.addTransition(q0, "A", "A", Direction.RIGHT)

    q4.addTransition(q4, "B", "B", Direction.RIGHT)
    q4.addTransition(q3, "_", "_", Direction.LEFT)

    q3.addTransition(q3, "A", "A", Direction.LEFT)
    q3.addTransition(q3, "B", "B", Direction.LEFT)
    q3.addTransition(qf, "_", "_", Direction.RIGHT)

    w = "aaabbb"
    mt = Machine(q0, w, 20, enable_logging=False)
    result = mt.run()
    print(f"Result: {'ACCEPTED' if result else 'REJECTED'}")
    return result


def teste_multiplo_3():
    """Turing Machine for binary numbers divisible by 3"""
    print(
        "\n=== Test 2: Binary multiples of 3 { w in Σ^* | w é um número binario multiplo de 3} ==="
    )
    q0 = State("q0")
    q1 = State("q1")
    q2 = State("q2")
    q0.setFinal()

    q0.addTransition(q0, "0", "0", Direction.RIGHT)
    q0.addTransition(q1, "1", "1", Direction.RIGHT)

    q1.addTransition(q0, "1", "1", Direction.RIGHT)
    q1.addTransition(q2, "0", "0", Direction.RIGHT)

    q2.addTransition(q2, "1", "1", Direction.RIGHT)
    q2.addTransition(q1, "0", "0", Direction.RIGHT)

    w = "0000110"
    mt = Machine(q0, w, 10, enable_logging=False)
    result = mt.run()
    print(f"Result: {'ACCEPTED' if result else 'REJECTED'}")
    return result


def teste_palindrome():
    """Turing Machine to recognize palindromes over {a, b}"""
    print("\n=== Test 3: Palindrome Recognition { w | w = w^R, w in {a,b}^* } ===")
    q0 = State("q0")
    q1 = State("q1")
    q2 = State("q2")
    q3 = State("q3")
    q4 = State("q4")
    q5 = State("q5")
    qf = State("qf")
    qf.setFinal()

    # From q0: mark first symbol and move right
    q0.addTransition(
        q1, "a", "X", Direction.RIGHT
    )  # Mark 'a' with X, look for matching 'a' at end
    q0.addTransition(
        q3, "b", "Y", Direction.RIGHT
    )  # Mark 'b' with Y, look for matching 'b' at end
    q0.addTransition(qf, "_", "_", Direction.RIGHT)  # Empty string is palindrome
    q0.addTransition(qf, "X", "X", Direction.RIGHT)  # Only marks left, palindrome
    q0.addTransition(qf, "Y", "Y", Direction.RIGHT)  # Only marks left, palindrome

    # q1: Skip to end to check for 'a'
    q1.addTransition(q1, "a", "a", Direction.RIGHT)
    q1.addTransition(q1, "b", "b", Direction.RIGHT)
    q1.addTransition(q1, "X", "X", Direction.RIGHT)
    q1.addTransition(q1, "Y", "Y", Direction.RIGHT)
    q1.addTransition(q2, "_", "_", Direction.LEFT)

    # q2: Check last symbol is 'a', then go back
    q2.addTransition(q5, "a", "X", Direction.LEFT)

    # q3: Skip to end to check for 'b'
    q3.addTransition(q3, "a", "a", Direction.RIGHT)
    q3.addTransition(q3, "b", "b", Direction.RIGHT)
    q3.addTransition(q3, "X", "X", Direction.RIGHT)
    q3.addTransition(q3, "Y", "Y", Direction.RIGHT)
    q3.addTransition(q4, "_", "_", Direction.LEFT)

    # q4: Check last symbol is 'b', then go back
    q4.addTransition(q5, "b", "Y", Direction.LEFT)

    # q5: Go back to beginning
    q5.addTransition(q5, "a", "a", Direction.LEFT)
    q5.addTransition(q5, "b", "b", Direction.LEFT)
    q5.addTransition(q5, "X", "X", Direction.LEFT)
    q5.addTransition(q5, "Y", "Y", Direction.LEFT)
    q5.addTransition(q0, "_", "_", Direction.RIGHT)

    w = "abba"
    mt = Machine(q0, w, 20, enable_logging=False)
    result = mt.run()
    print(f"Result: {'ACCEPTED' if result else 'REJECTED'}")
    return result


def teste_unary_addition():
    """Turing Machine for unary addition: 1^n + 1^m = 1^(n+m)"""
    print("\n=== Test 4: Unary Addition { 1^n+1^m | result is 1^(n+m) } ===")
    q0 = State("q0")
    q1 = State("q1")
    q2 = State("q2")
    qf = State("qf")
    qf.setFinal()

    # Skip to the + sign
    q0.addTransition(q0, "1", "1", Direction.RIGHT)
    q0.addTransition(q1, "+", "1", Direction.RIGHT)  # Replace + with 1

    # Skip to the end
    q1.addTransition(q1, "1", "1", Direction.RIGHT)
    q1.addTransition(q2, "_", "_", Direction.LEFT)

    # Remove last 1
    q2.addTransition(qf, "1", "_", Direction.LEFT)

    w = "111+11"
    mt = Machine(q0, w, 15, enable_logging=False)
    result = mt.run()
    print(f"Result: {'ACCEPTED' if result else 'REJECTED'}")
    return result


def run_all_tests():
    """Run all test cases"""
    print("=" * 60)
    print("Running Turing Machine Test Suite")
    print("=" * 60)

    results = []
    results.append(("Context-Free a^nb^n", teste_anbn()))
    results.append(("Binary Multiples of 3", teste_multiplo_3()))
    results.append(("Palindrome Recognition", teste_palindrome()))
    results.append(("Unary Addition", teste_unary_addition()))

    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    for name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{name:30s} {status}")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()
