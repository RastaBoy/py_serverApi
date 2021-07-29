from server import create_app


def main():
    create_app().run(host="0.0.0.0", port=5555)

if __name__ == "__main__":
    main()