from src.split import split

def main():
    print("Hello from fraud-detection!")

    print()
    split("data/train.csv", nb_period=75)

if __name__ == "__main__":
    main()
