def linear_searchproduct(productlist, targetproduct): 
 indices = []
 for index,product in enumerate (productlist):
  if product == targetproduct:
    indices.append(index)
 return indices
products=["shoes","boot","loafer","shoes","sandal","shoes"]
target="shoes" 
target2="apple"
result = linear_searchproduct(products,target)
print(result)


  
