dict_list=[{'name': 'affirm', 'confidence': 0.9448149204254}, 
{'name': 'affirm', 'confidence': 0.944814920425415}, 
{'name': 'inform', 'confidence': 0.9842240810394287}, 
{'name': 'inform', 'confidence': 0.9842240810394287}]

final_dict_list= list(map(dict, set(tuple(i.items()) for i in dict_list)))

print(final_dict_list)