import pandas as pd


def main():
    df = pd.DataFrame(
        {"a": [1, 2, 3], "b": [4, 5, 6]}, columns=["a", "b"]
    )  # Create a DataFrame with specified columns
    df.to_csv("output.csv", index=False)
    print(df)


if __name__ == "__main__":
    main()
