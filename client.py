import requests
import random
import json

from matplotlib import pyplot as plt


def first():
    """
    This is a function that generates random values.
    """
    numbers = random.random()
    return numbers


def query(numbers):

    """
    This function is a function that gets a response to the server

    Args:
        numbers: value of x

    Return:
        y: value of y from server
    """

    url = "http://localhost:4000/jsonrpc"
    headers = {'content-type': 'application/json'}
    # Example echo method
    payload = {
	"method": "calculation",
	"params": {"x":numbers},
	"jsonrpc": "2.0",
	"id": 0,
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    y = response["result"]
    return y

def scatter_plot(x,y):

    """
    This is a function that plot a scatter diagram

    Args:
        x: list of x
        y: list of y
    """

    plt.scatter(x,y,c="steelblue")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig("result.eps")

def main():

    """
    main function
    """

    X_value = []
    Y_value = []

    # 1回目
    x = first()
    X_value.append(x)
    y = query(x)
    Y_value.append(y)

    # 449回
    for count in range(0,499):
        X_value.append(y)
        y = query(y)
        Y_value.append(y)

    scatter_plot(X_value,Y_value)


if __name__ == "__main__":
    main()
