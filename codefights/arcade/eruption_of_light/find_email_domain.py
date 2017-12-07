def findEmailDomain(address):
    address_list = list(address)
    at = len(address_list) - address_list[::-1].index('@')
    return address[at:]


# top voted from codefights - more elegant than mine!  Split the input into a list at the '@' symbols, return the last
# element of the list.

def findEmailDomain_cf(address):
    a = address.split('@')
    return a[-1]


print(findEmailDomain("prettyandsimple@example.com"))
