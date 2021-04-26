# Catalan Number

위키백과 : 조합론에서, 카탈랑 수(Catalan數, 영어: Catalan number)는 이진 트리의 수 따위를 셀 때 등장하는 수열이다.   
<img src="https://user-images.githubusercontent.com/61103343/112749932-760e9900-9000-11eb-8e35-3dcd0b27b062.png" width="100px" height="70px" title="1"></img>   

## 96. Unique Binary Search Trees
* n = 2일때
  Root로는 1, 2이 될 수 있다.
  - Root = 1일때   
    <img src="https://user-images.githubusercontent.com/61103343/112746167-36d44e00-8fe8-11eb-8008-d901b04217da.png" width="300px" height="250px" title="1"></img>   
    다음과 같이 오른쪽 자식 노드에 Root보다 큰 2가 들어갈 수 있고 왼쪽 자식 노드에는 Root보다 작은 값이 들어가야하는데 당연히 들어갈 수 있는 노드가 없다.
  - Root = 2일때   
    <img src="https://user-images.githubusercontent.com/61103343/112746313-f32e1400-8fe8-11eb-808b-961706ad0d28.png" width="300px" height="250px" title="2"></img>   
    똑같이 왼쪽 자식 노드에 Root 보다 작은 1이 들어갈 수 있고 오른쪽 자식 노드에는 들어갈 수 있는 것이 없다.

* n = 3일때
  Node로는 1, 2, 3이 될 수 있다.
  - Root = 1일때   
    <img src="https://user-images.githubusercontent.com/61103343/112746475-fb3a8380-8fe9-11eb-9fda-ec5c8173829f.png" width="300px" height="250px" title="3"></img>   
    오른쪽 자식 노드로 2, 3이 들어갈 수 있고 왼쪽 자식 노드에는 Root보다 작은 값이 없으므로 들어 갈 수 있는 값이 없다.
    따라서 다음과 같이 두 가지의 트리가 만들어질 수 있다.   
    <img src="https://user-images.githubusercontent.com/61103343/112746556-6edc9080-8fea-11eb-9b18-b706ec80c70c.png" width="300px" height="250px" title="4"></img>   
  - Root = 2일때   
    <img src="https://user-images.githubusercontent.com/61103343/112746572-96cbf400-8fea-11eb-805a-68d49392825d.png" width="300px" height="250px" title="5"></img>   
    오른쪽 자식 노드로 3이 들어갈 수 있고 왼쪽 자식 노드에는 1이 들어갈 수 있다. 따라서 한 가지의 트리가 만들어질 수 있다.
  - Root = 3일때   
    <img src="https://user-images.githubusercontent.com/61103343/112746642-1659c300-8feb-11eb-937f-9f8852829c48.png" width="300px" height="250px" title="6"></img>   
    왼쪽 자식 노드로 1, 2가 들어갈 수 있고 오른쪽 자식 노드로는 Root보다 큰 값이 없으므로 들어 갈 수 있는 값이 없다.
    따라서 다음과 같이 두 가지의 트리가 만들어질 수 있다.   
    <img src="https://user-images.githubusercontent.com/61103343/112746673-68024d80-8feb-11eb-9a18-89abf980259f.png" width="300px" height="250px" title="7"></img>   
   
* 위와 같은 과정을 다음과 같이 정의할 수 있다.
  G(3) = F(1, 3) + F(2, 3) + F(3, 3)
  그리고 F(1, 3), F(2, 3), F(3, 3)을 다시 Sub Problem으로 나누면 다음과 같다.   
  <img src="https://user-images.githubusercontent.com/61103343/112747956-af8cd780-8ff3-11eb-954a-ebc1bfc6b606.png" width="300px" height="250px" title="8"></img>   
  F(1, 3)은 Node가 3개가 있고 Root = 1일때 오른쪽 자식 노드에 나머지 두 개의 노드가 들어갈 수 있다. 그리고 이 오른쪽 자식 노드는 n = 2일때와 같은 트리의 개수가 생긴다. 즉, G(2)와 같다.
  마찬가지로 F(2, 3)은 Node가 3개있고 Root = 2, 왼쪽 자식 노드에는 Root인 2보다 작은 하나의 노드 1이 들어갈 수 있고 오른쪽 자식 노드도 2보다 큰 하나의 노드 3이 들어갈 수 있다. 따라서 왼쪽 자식 노드 = G(1), 오른쪽 자식 노드 = G(1)이 된다.
  F(3, 3)도 왼쪽 자식 노드 = G(2), 오른쪽 자식 노드 = G(0)이 될 것이다.
  
  예를 들어서 하나 더 보자.
  F(3, 6)일 때는 Root = 3이고 자식 노드로는 1, 2, 4, 5, 6이 될 수 있다. 여기서 왼쪽 자식 노드로는 3보다 작은 1, 2 총 2개의 노드가 들어갈 수 있고 오른쪽 자식 노드로는 3보다 큰 4, 5, 6 총 3개의 노드가 들어갈 수 있다. 이것은 G(2), G(3)으로 표현할 수 있다.
  또한 F(3, 6) = G(3-1), G(6-3) -> F(i, n) = G(i - 1), G(n - i)로 표현할 수 있을 것이다.
  결론적으로 F(n - i)의 개수는 G(i - 1) * G(n - i)이 될 것이다.
