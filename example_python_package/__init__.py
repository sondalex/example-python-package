def hello_world() -> str:
    return "Hello World"


def main() -> int:
    print(hello_world())
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
