# Driver Code


customers = {
    0: {
        "name": "Haseeb",
        "age": "23",
        5: "fav no",
    },
    1: {
        "name": "Addan",
        "age": "17",
        "discounts": {1:"golden"},
    }
}

if "Golden".lower() in customers[1]["discounts"].values():
    print(True)


