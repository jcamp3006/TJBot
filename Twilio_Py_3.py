from twilio.rest import Client

#account_sid = ''
account_sid = 'AC118379df8b7b7c6e3626019f3f3093bd'

#auth_token = ''
auth_token = '2076a2d4f6c553ada439b9ab966cf624'

class User:
  def __init__(self, Name, PhoneNumber, AreaOfInterest):  
    self.Name = Name
    self.PhoneNumber = PhoneNumber
    self.AreaOfInterest = AreaOfInterest
    
user0 = User( "John", '+19723227678', 'CLOUD')
user1 = User("Monique", "+16549873215", "IoT")
user2 = User("Corey", "+16498711346", "Quantum")
user3 = User("Adib", "+12145679834", "AI")
user4 = User("Rahat", "+4693127965", "Watson")
user5 = User("Dom", "+18174687931", "Analytics")

users = [user0, user1, user2, user3, user4, user5]

#print(users[0].Name)
#print(users[0].AreaOfInterest)

#if users[1].Name == "John":        
#        print("Hi, John!");        
#else:         
#        print("I don't know you!");
        
#if users[0].AreaOfInterest == "CLOUD":        
#        print("You like CLOUD!");        
#else:         
#        print("I don't know what you like!");

for user in users:
    
    if user.AreaOfInterest == "CLOUD":   
        #print(user.AreaOfInterest + user.PhoneNumber)
        client = Client(account_sid, auth_token)

        message = client.api.account.messages.create(
                        to = user.PhoneNumber,
                        from_='+12029315873',
                        body = '%s is interested in %s'% (user.Name, user.AreaOfInterest)

        )
        
    else:
        print("Something Else!")