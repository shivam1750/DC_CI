import xmlrpc.client

def main():
    server = xmlrpc.client.ServerProxy('http://localhost:8000')
    number = int(input("Enter a number to calculate its factorial: "))
    result = server.factorial(number)
    print(f"The factorial of {number} is {result}")

if __name__ == "__main__":
    main()