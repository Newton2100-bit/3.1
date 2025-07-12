import Pyro4, time
# Connect to the server using the URI 
uri = "PYRONAME:example.greeting" 
greeting = Pyro4.Proxy(uri) 
# Call remote method 
for _ in range(10,100,2):
    time.sleep(0.5)
    print(greeting.say_hello("Alice")) 

