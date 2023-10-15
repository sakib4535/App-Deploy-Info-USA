import requests
import json

response = requests.get('http://api.stackexchange.com/2.3/posts?order=desc&sort=activity&site=stackoverflow')

print(response.json())
print(response.json()['items'])


for data in response.json()['items']:
    print(data['owner'])


print(response.json()['items'])

# Iterate through each item in the 'items' list and print the 'owner' information for each post
print("\nOwner Information:")
for data in response.json()['items']:
    print("Owner:", data['owner'])

# Print the 'items' list again, which was already printed earlier
print("\nItems (Again):")
print(response.json()['items'])


if response.status_code == 200:
    data = response.json()

    items = data.get('items', [])


    for item in items:
        owner = item.get('owner', {})
        reputation = owner.get('reputation', None)
        user_type = owner.get('user_type', None)

        print("Owner: ")
        print(f"Reputation: {reputation}")
        print(f"User Type: {user_type}")

else:
    print(f"Error")


register_count = 0
unregister_count = 0

for item in items:
    owner = item.get('owner', {})
    reputation = owner.get('reputation', None)
    user_type = owner.get('user_type', None)

    if user_type == 'registered':
        register_count += 1
    elif user_type == 'unregistered':
        unregister_count += 1

print("Registered Users:", register_count)
print("Unregistered Users:", unregister_count)
