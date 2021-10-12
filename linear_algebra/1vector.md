# Vector란
벡터란 물리학에서 '크기와 방향으로 정의되는 값'이다. 이것은 기하학적인 벡터의 특성을 잘 반영하고 있는 정의이다.  
> 수학에선 모든 벡터들의 시작이 원점이어야 한다.   

벡터는 좌표계의 변환에 대한 불변적이다. 이는 아래 그림과 같이 좌표계가 변하더라도 벡터 그 자체는 가만히 있다는 것을 의미한다.
![](https://raw.githubusercontent.com/angeloyeo/angeloyeo.github.io/master/pics/2020-09-07-basic_vector_operation/pic1.png)

## 벡터란 숫자를 순서대로 나열한 것
벡터는 순서를 맞춰 숫자를 나열한 리스트라는 정의도 내릴 수 있다.  
이런 관점에서 벡터를 생각하면 숫자만 나열하면 점점 고차원의 벡터가 되므로 차원을 무한히 늘리는데에 부담이 없다.

## 벡터란 벡터 공간의 원소
사실 수학적으로 가장 의미있는 정의는 벡터란 그저 벡터 공간vector space의 원소라고 말하는 것이다. 즉, 이런 특성을 가진 것들은 벡터로 취급해서 다룰 수 있다는 것이다.   
예를 들어 함수나 행렬같은 개념들도 벡터에 적용할 수 있는 여러가지 기법들을 통해 응용할 수 있다.  
벡터 공간은 다음과 같은 세가지 요소가 정의되고 성립되어야 한다. <img src="https://render.githubusercontent.com/render/math?math=(V,+,\cdot)"> 여기서 V는 벡터, +는 덧셈 규칙, <img src="https://render.githubusercontent.com/render/math?math=\cdot">은 곱셈 규칙을 의미한다. 

# 벡터의 연산
## 벡터의 상수배scalar multipliation
임의의 집합 <img src="https://render.githubusercontent.com/render/math?math=V(\neq\varnothing)">에 대해 임의의 벡터 <img src="https://render.githubusercontent.com/render/math?math=x\in V">와 스칼라<img src="https://render.githubusercontent.com/render/math?math=k \in \mathbb{R}">에 대하여 다음이 성립해야 한다.   
<img src="https://render.githubusercontent.com/render/math?math=x\in V, k\in mathbb{R}\rightarrow kx\in V">  
주어진 화살표에 대해 스칼라값에 대응하여 화살표의 크기가 늘어나거나 줄어드는 것을 의미할 수 있다. 

## 벡터 간의 합
임의의 집합 <img src="https://render.githubusercontent.com/render/math?math=V(\neq\varnothing)">에 대해 임의의 벡터 <img src="https://render.githubusercontent.com/render/math?math=x,y\in V">에 대하여 다음이 성립해야 한다.   
<img src="https://render.githubusercontent.com/render/math?math=x,y\in V, \rightarrow x+y\in V">  
이는 주어진 두 화살표에 대해 화살표의 크기와 방향을 합해서 평행사변형 꼴을 이룰 수 있도록 합해진 벡터가 출력되면 된다. ![](https://raw.githubusercontent.com/angeloyeo/angeloyeo.github.io/master/pics/2020-09-07-basic_vector_operation/pic3.png)

### 상수배와 벡터 간의 합
기본적으로 상수배와 벡터 간의 합이 중요한 것은 이 두 연산이 잘 정의되는 것(entity)들은 선형성을 만족한다고 할 수 있기 때문이다.

## 데이터 변형 방법
‘벡터는 숫자들을 순서대로 나열한 것’이라는 관점에서 상수배와 벡터간의 합이 중요할 수 있다.  
즉 데이터를 벡터로 생각해 데이터를 처리한다고 본다.

예를 들어 5명의 국어 성적과 영어 성적의 평균을 구한다고 가정한다.   
국어 성적에 대한 정보를 벡터로 표현하면 <img src="https://render.githubusercontent.com/render/math?math=k=\begin{bmatrix}100\\ 70\\ 30\\ 45\\ 80\end{bmatrix}"> 와 같고 영어 점수에 대한 벡터는 <img src="https://render.githubusercontent.com/render/math?math=e=\begin{bmatrix}83\\ 50\\ 25\\ 30\\ 60\end{bmatrix}"> 와 같다.   
이 떄, 두 점수의 평균 점수를 매기는 법은   
<img src="https://render.githubusercontent.com/render/math?math=avg=\frac{1}{2}k=\frac{1}{2}e=\frac{1}{2}\begin{bmatrix}100\\ 70\\ 30\\ 45\\ 80\end{bmatrix}+\frac{1}{2} \begin{bmatrix}83\\ 50\\25\\30\\60 \end{bmatrix}"> 

