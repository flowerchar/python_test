
记录Python生态的测试技术，包括pytest, selenium, requests

1. 除开get以外的请求方法，其实也可以使用params参数，只是不太常用，因为这些请求方法的参数都是在请求体中传递的，而不是在url中传递的。
2. ![image-20240624161848877](README.assets/image-20240624161848877.png)
3. 生成allure测试报告指令：`pytest -vs 02-petstore.py --alluredir=./report --clean-alluredir`
4. 生成allure测试报告：`allure serve ./report`
5. 
6. | 符号        | 描述                                                       |
   | :---------- | :--------------------------------------------------------- |
   | $           | 查询的根节点对象，用于表示一个 json 数据，可以是数组或对象 |
   | @           | 过滤器（filter predicate）处理的当前节点对象               |
   | `*`         | 通配符                                                     |
   | .           | 获取子节点                                                 |
   | `..`        | 递归搜索，筛选所有符合条件的节点                           |
   | ?()         | 过滤器表达式，筛选操作                                     |
   | [start:end] | 数组片段，区间为[start,end),不包含 end                     |
   | [A]或[A,B]  | 迭代器下标，表示一个或多个数组下标                         |

7. jsonPath链接：`https://jsonpath.hogwarts.ceshiren.com/` 

8. ```xml
   数据
   {
     "store": {
       "book": [
         {
           "category": "reference",
           "author": "Nigel Rees",
           "title": "Sayings of the Century",
           "price": 8.95
         },
         {
           "category": "fiction",
           "author": "Evelyn Waugh",
           "title": "Sword of Honour",
           "price": 12.99
         },
         {
           "category": "fiction",
           "author": "Herman Melville",
           "title": "Moby Dick",
           "isbn": "0-553-21311-3",
           "price": 8.99
         },
         {
           "category": "fiction",
           "author": "J. R. R. Tolkien",
           "title": "The Lord of the Rings",
           "isbn": "0-395-19395-8",
           "price": 22.99
         }
       ],
       "bicycle": {
         "color": "red",
         "price": 19.95
       }
     },
     "expensive": 10
   }
   获取所有书籍的作者
   获取所有作者 $..author
   获取 store 下面的所有内容 $.store
   获取所有的价格 $..price
   获取第三本书 $..book[2]  $..book[0,2,3] $..book[0:3]
   获取所有包含 isbn 的书籍 $..book[?(@.isbn)]
   获取所有价格小于 10 的书 $..book[?(@.price<10)]
   获取所有书籍的数量 $..book.length
   ```

9. 注意xpath是从1计数，jsonpath是从0开始
10. 隐式等待只能解决元素查找的问题，显式等待可以解决元素交互问题