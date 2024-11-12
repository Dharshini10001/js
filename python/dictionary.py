# python dictionary
# collections items store 
# {}, compare to other collections - only items - but it have 
# keys:values pair 
# creating dictionay using {}
my_dict1={
    "name":"python", #name-key : python-value
    "usage":"prglang"
}
print(my_dict1)
print(type(my_dict1))
#accessing items and values, keys
print(my_dict1.keys())
print(my_dict1.values())
print(my_dict1.items())
# using key index
print(my_dict1["name"])
#modify or update dictionaries
my_dict1["usage"]="trendy lang"
my_dict1["why"]="develop sw"
print(my_dict1)
# update
my_dict2={"1":"one",
          "2":"two"}
my_dict1.update(my_dict2)
print(my_dict1)

print(my_dict1)
# comperhensive method
my_dic3={x :x**2 for x in range(5)} #0 -4 
print(my_dic3)
# constructor
my_dict4=dict(name="python",age="5",cl="2")
print(my_dict4)
# create list in dict
# nested dictionary
my_dict5={
    "name":{
        "name":"python",
        "age":3
    },
    "job":{
        "job":"developer"
    }
  }
print(my_dict5)
# update
my_dict5.update({"job":"testing"})
print(my_dict5)