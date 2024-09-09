import pandas
import os


if __name__ == '__main__':
    if os.getenv('TEST_VAR') == 'mysecret':
        print("matched secret")

    print(os.getenv('TEST_VAR', "????"))
    print(pandas.__version__)
