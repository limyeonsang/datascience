## hyperplane(초평면)이란
두개의 변수로 만들어진 1차식 ax+by+c=0 는 직선의 방정식으로 2차원 평면에 그려진다.  
변수를 하나 추가해 ax+by+cz+d=0의 식이 되면 3차원 공간에 그려진다.  
변수를 하나 더 추가한 
<img src="https://render.githubusercontent.com/render/math?math=a_1x_1+a_2x_2+a_3x_3+a_4x_4+c">의 식은 4차원 공간에 그려진다.  
이를 일반화하여 초평면으로 부른다. 즉 1차식으로 만들어지는 도형은 전부 초평면이다. 각 초평면은 그려진 차원을 이용해 ~~차원의 초평면이라고 부른다. 

### hyperplane은 분할한다
초평면은 공간(데이터)을 분할하는 모형으로 차원(n)보다 한 차원 낮은(n-1) 차원의 평면을 이용해 목표변수를 분류한다.   
2차원 평면의 초평면은 1차원인 직선으로 평면을 분할한다. 

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbWq8yr%2FbtqyogoZm9t%2F4C3hCvJ8DKCkDje5TKPao1%2Fimg.png)

### hyperplane은 어떻게 찾는가
이분형 데이터로 분류하는 hyperplane은 여러개가 될 수 있다. hyperplane과 가장 가까운 점과의 수직선의 거리를 마진으로 정의하고, 마진이 가장 큰 것을 선택한다.  
하지만 두 집단이 완벽하게 분리되지 않는 경우가 일반적이므로 몇몇 점들은 hyperplane을 넘어가는 것을 허용해야 한다. 즉, 마진을 최대화 하며 몇몇 분류가 안된 점들의 거리를 최소화함으로써 가작 최적의 hyperplane을 찾는 것이다.(soft-margin)  

